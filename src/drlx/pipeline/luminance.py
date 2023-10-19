from datasets import load_dataset
import torch

from drlx.pipeline import PromptPipeline

class LuminancePairs(PromptPipeline):
    """
    Prompt pipeline consisting of prompts from the `PickAPic dataset <https://arxiv.org/abs/2305.01569>`_ training set.
    """
    def __init__(self, *args):
        super().__init__(*args)

        self.dataset = load_dataset("Nbardy/Synthetic-V5")["train"]

    def __getitem__(self, index):
        # TODO: Generate luminance feature
        return self.dataset[index]
    
    def __len__(self):
        return len(self.dataset)
