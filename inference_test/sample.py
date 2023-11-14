# make sure you're logged in with `huggingface-cli login`
from diffusers import StableDiffusionPipeline

from accelerate import Accelerator

gc_steps = 4

accelerator = Accelerator(
    log_with = "wandb",
    gradient_accumulation_steps = gc_steps,
)

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
#pipe = pipe.to("mps")
pipe = pipe.to(accelerator.device)

prompt = "a photo of an astronaut riding a horse on mars"

# First-time "warmup" pass (see explanation above)
_ = pipe(prompt, num_inference_steps=1)

# Results match those from the CPU device after the warmup pass.
image = pipe(prompt).images[0]

# Save PIL Image to disk
image.save("test.jpeg")
