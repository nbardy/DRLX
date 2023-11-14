
from typing import Iterable
import numpy as np
import clip

from drlx.reward_modelling import RewardModel

import torch

import torch
from torch.nn.functional import cosine_similarity, cross_entropy

# Example usage
# x_input = torch.tensor(...) # Logits
# y_batch_target = torch.tensor(...) # Class indices
# mean_similarity = similarity(x_input, y_batch_target, "cross_entropy")
def similarity(x_input, y_batch_target, similarity_type="cosine"):
    if similarity_type == "cosine":
        x_expanded = x_input.expand_as(y_batch_target)
        cos_sim = cosine_similarity(x_expanded, y_batch_target, dim=-1)
        return cos_sim.mean()
    elif similarity_type == "cross_entropy":
        # Assumes x_input are logits and y_batch_target are class indices
        return cross_entropy(x_input.unsqueeze(0), y_batch_target, reduction='mean')
    else:
        raise ValueError("Invalid similarity type. Choose 'cosine' or 'cross_entropy'.")


# Calculates the cross entrop loss between the target style prompts
# and the generated prompts
class StylePromptReward(RewardModel):
    def __init__(self, style_prompts, device=None):
        super().__init__()
        self.device = device
        self.clip_model, self.preprocess = clip.load(
            "ViT-L/14", device=device if device is not None else "cpu"
        )
        self.target_prompts = style_prompts
        self.target_embeddings = self.preprocess(self.target_prompts).cuda()
        self.target_embeddings = self.clip_model.encode_text(self.target_embeddings)

    # Checks that the images are close to the target style promptsjA
    def forward(self, images: np.ndarray, prompts: Iterable[str], prepend_prompts=False, distance="cosine"):
        if prepend_prompts:
            target_prompts = [f"{prompt} {target_prompt}" for prompt, target_prompt in zip(prompts, self.target_prompts)]
        else:
            target_prompts = self.target_prompts

        target_embeddings = self.preprocess(target_prompts).cuda()
        target_embeddings = self.clip_model.encode_text(target_embeddings)
        image_features = self.clip_model.encode_image(images)

        return similarity(image_features, target_embeddings, distance)

# A reward function that accepts a function to transform a given prompt into a new prompt
# And calculates the reward distance
class PromptFunctionReward(RewardModel):
    def __init__(self, prompt_function, device=None):
        super().__init__()
        self.device = device
        self.clip_model, self.preprocess = clip.load(
            "ViT-L/14", device=device if device is not None else "cpu"
        )
        self.prompt_function = prompt_function

    def forward(self, images: np.ndarray, prompts: Iterable[str], distance="cosine"):
        new_prompts = [self.prompt_function(prompt) for prompt in prompts]
        new_embeddings = self.preprocess(new_prompts).cuda()
        new_embeddings = self.clip_model.encode_text(new_embeddings)
        image_features = self.clip_model.encode_image(images)

        return similarity(image_features, new_embeddings, distance)

    



