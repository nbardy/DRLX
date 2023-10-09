from typing import Iterable

import torch
from torch import nn
import numpy as np
import requests
import os
import clip
from PIL import Image

from drlx.reward_modelling import RewardModel

class MLP(nn.Module):
    def __init__(self, input_size, xcol='emb', ycol='avg_rating'):
        super().__init__()
        self.input_size = input_size
        self.xcol = xcol
        self.ycol = ycol
        self.layers = nn.Sequential(
            nn.Linear(self.input_size, 1024),
            #nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(1024, 128),
            #nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(128, 64),
            #nn.ReLU(),
            nn.Dropout(0.1),

            nn.Linear(64, 16),
            #nn.ReLU(),

            nn.Linear(16, 1)
        )

    def forward(self, x):
        return self.layers(x)

def load_aesthetic_model_weights(cache="."):
    """
    Load aesthetic model weights

    :param cache: Stores the downloaded weights here
    :type cache: str
    """
    weights_fname = "sac+logos+ava1-l14-linearMSE.pth"
    loadpath = os.path.join(cache, weights_fname)

    if not os.path.exists(loadpath):
        url = (
            "https://github.com/christophschuhmann/"
            f"improved-aesthetic-predictor/blob/main/{weights_fname}?raw=true"
        )
        r = requests.get(url)

        with open(loadpath, "wb") as f:
            f.write(r.content)

    weights = torch.load(loadpath, map_location=torch.device("cpu"))
    return weights

def aesthetic_model_normalize(a, axis=-1, order=2):
    """
    Normalize output from aesthetics model
    """
    l2 = np.atleast_1d(np.linalg.norm(a, order, axis))
    l2[l2 == 0] = 1
    return a / np.expand_dims(l2, axis)

def aesthetic_scoring(imgs, preprocess, clip_model, aesthetic_model):    
    imgs = torch.stack([preprocess(Image.fromarray(img)).cuda() for img in imgs])
    with torch.no_grad(): image_features = clip_model.encode_image(imgs)
    im_emb_arr = aesthetic_model_normalize(image_features.cpu().detach().numpy())
    prediction = aesthetic_model(torch.from_numpy(im_emb_arr).float().cuda())
    return prediction

class Aesthetics(RewardModel):
    """
    Reward model that rewards images with higher aesthetic score. Uses CLIP and an MLP (not put on any device by default)

    :param device: Device to load model on
    :type device: torch.device
    """
    def __init__(self, device = None):
        super().__init__()
        self.model = MLP(768)
        self.model.load_state_dict(load_aesthetic_model_weights())
        self.clip_model, self.preprocess = clip.load("ViT-L/14", device=device if device is not None else 'cpu')

        if device is not None:
            self.model.to(device)

    def forward(self, images : np.ndarray, prompts : Iterable[str]):
        return aesthetic_scoring(
            images,
            self.preprocess,
            self.clip_model,
            self.model
        )


from typing import Iterable
import torch
import numpy as np

class MaskedLuminance(RewardModel):
    def __init__(self, tolerance: float, device=None):
        super().__init__()
        self.tolerance = tolerance
        if device is not None:
            self.device = device
        else:
            self.device = torch.device("cpu")

    def calculate_luminance(self, image: np.ndarray):
        R, G, B = image[:, :, 0], image[:, :, 1], image[:, :, 2]
        luminance = 0.299 * R + 0.587 * G + 0.114 * B
        return luminance

    def compute_masked_luminance_score(self, luminance: np.ndarray, luminance_feature: np.ndarray, mask: np.ndarray):
        diff = np.abs(luminance - luminance_feature)
        score = np.sum((diff <= self.tolerance) * mask)
        return score

    def forward(self, images: np.ndarray, luminance_features: np.ndarray, masks: np.ndarray):
        scores = []
        for image, luminance_feature, mask in zip(images, luminance_features, masks):
            luminance = self.calculate_luminance(image)
            score = self.compute_masked_luminance_score(luminance, luminance_feature, mask)
            scores.append(score)
        return np.array(scores)
