# This file impliments reward functions for training adapters to
# maintain the luminance of the original image via reward modeling
from drlx.reward_modelling import RewardModel
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

    def compute_masked_luminance_score(
        self, luminance: np.ndarray, luminance_feature: np.ndarray, mask: np.ndarray
    ):
        diff = np.abs(luminance - luminance_feature)
        score = np.sum((diff <= self.tolerance) * mask)
        return score

    def forward(
        self, images: np.ndarray, luminance_features: np.ndarray, masks: np.ndarray
    ):
        scores = []
        for image, luminance_feature, mask in zip(images, luminance_features, masks):
            luminance = self.calculate_luminance(image)
            score = self.compute_masked_luminance_score(
                luminance, luminance_feature, mask
            )
            scores.append(score)
        return np.array(scores)