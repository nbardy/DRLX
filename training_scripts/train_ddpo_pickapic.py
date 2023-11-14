# Trains a model on the PickScore reward model
# Trained on human preference data from PickAPic

from drlx.trainer.ddpo_trainer import DDPOTrainer
from drlx.configs import DRLXConfig
from drlx.pipeline.pickapic_prompts import PickAPicPrompts
from drlx.reward_modelling.pickscore import PickScoreModel
from drlx.utils import get_latest_checkpoint

pipe = PickAPicPrompts()
resume = False

config = DRLXConfig.load_yaml("configs/ddpo_sd_pickapic.yml")
trainer = DDPOTrainer(config)

if resume:
    cp_dir = get_latest_checkpoint(f"checkpoints/{config.logging.run_name}")
    trainer.load_checkpoint(cp_dir)

trainer.train(pipe, PickScoreModel())