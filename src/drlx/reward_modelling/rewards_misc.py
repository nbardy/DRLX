
from typing import Iterable
import numpy as np

from drlx.reward_modelling import RewardModel

from .aesthetics import Aesthetics
from .prompts import  StylePromptReward, PromptFunctionReward
from prompt_sets import simple_sharp_realistic_prompts, generic_hq_photography_keywords, random_cinematic_prompt

from drlx.reward_modelling.pickscore import PickScoreModel

# Combines the photorealism and aesthetics reward models
class PhotoRealisticRewardModel(RewardModel):
    def __init__(self, device=None):
        super().__init__()
        self.aesthetic_model = Aesthetics(device=device)
        self.realistic_reward = StylePromptReward(simple_sharp_realistic_prompts, device=device)
        self.photography_reward = StylePromptReward(generic_hq_photography_keywords, device=device)

        self.pick_score_model = PickScoreModel()
    
    def forward(self, 
                images: np.ndarray, 
                prompts: Iterable[str],
                realistic_weight=0.6,
                aesthetic_weight=0.3,
                pick_score_weight=0.5,
                photography_weight=1.2):

        aesthetic_reward = self.aesthetic_model(images, prompts)
        realistic_reward = self.style_model(images, prompts)
        pick_score_reward = self.pick_score_model(images, prompts)

        # Include the prepended prompts to prevent too much drift away from the initial target
        # We don't want the reward model to overfit and forget the style qualitie
        photography_scores = self.style_model(images, prompts, prepend_prompt=True)

        return (realistic_weight * realistic_reward +
                aesthetic_weight * aesthetic_reward + 
                pick_score_weight * pick_score_reward +
                photography_weight * photography_scores)
    
class CinematicReward(RewardModel):
    def __init__(self, device=None):
        super().__init__()
        self.style_reward = PromptFunctionReward(random_cinematic_prompt, device=device)
    
    def forward(self, images: np.ndarray, prompts: Iterable[str]):
        return self.style_reward(images, prompts)


