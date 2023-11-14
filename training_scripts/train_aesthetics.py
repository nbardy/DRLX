from drlx.reward_modelling.aesthetics import Aesthetics
from drlx.pipeline.pickapic_prompts import PickAPicPrompts
from drlx.trainer.ddpo_trainer import DDPOTrainer
from drlx.configs import DRLXConfig

# We import a reward model, a prompt pipeline, the trainer and config

pipe = PickAPicPrompts()
config = DRLXConfig.load_yaml("configs/ddpo_sd_pickapic_sdxl.yml")
trainer = DDPOTrainer(config)

trainer.train(pipe, Aesthetics())
