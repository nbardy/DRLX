import random

generic_exciting_photgraphy = [
    "ultra-high resolution, clarity",
    "vibrant saturation, dynamic range",
    "subtle shading, soft contrast",
    "rich texture, fine detail",
    "dramatic lighting, strong shadows",
    "balanced composition, symmetry",
    "sharp focus, depth perception",
    "bold colors, vivid expression",
    "minimalist, clean lines",
    "abstract forms, creative patterns",
    "elegant simplicity, understated beauty",
    "high contrast, stark differences",
    "ambient mood, atmospheric effect",
    "intricate patterns, complex design",
    "fluid motion, kinetic energy",
    "layered depth, spatial complexity",
    "naturalistic tones, organic feel",
    "surreal elements, dreamlike quality",
    "refined elegance, sophisticated style",
    "innovative perspective, unique angle"
]

wordy_photography_descriptions = [
    "extreme clarity, precise detail, refined sharpness, high fidelity, impeccable resolution, photorealistic quality",
    "vivid color palette, saturated hues, dynamic range, bold expressions, striking vibrancy, rich saturation",
    "subtle gradation, soft lighting, nuanced shading, gentle contrast, delicate tones, understated textures",
    "textural richness, fine granularity, detailed surfaces, intricate patterns, realistic touch, tactile quality",
    "dramatic illumination, powerful shadows, intense highlights, stark lighting, contrasting brightness, moody ambiance",
    "symmetrical balance, harmonious composition, orderly arrangement, proportional elements, structured layout",
    "crisp focus, clear depth, realistic perception, sharp imagery, focused details, distinct foreground",
    "expressive colors, vivid imagery, bold chromaticity, intense saturation, lively palette, color dynamism",
    "minimalist design, clean aesthetics, simple lines, uncluttered composition, elegant simplicity, spartan beauty",
    "abstract concepts, creative formations, unusual patterns, imaginative designs, artistic abstraction, non-representational",
    "understated elegance, simple beauty, clean lines, minimalist design, subtle charm, elegant simplicity",
    "stark contrast, dramatic differences, high contrast, bold separation, contrasting elements, clear distinction",
    "ambient atmosphere, moody tones, atmospheric quality, environmental mood, immersive ambiance, subtle aura",
    "complex patterning, intricate design, detailed motifs, elaborate textures, sophisticated structures, ornate complexity",
    "sense of motion, dynamic flow, kinetic energy, fluid movement, rhythmic patterns, lively dynamism",
    "layered composition, spatial depth, multidimensional layout, complex depth, intricate layering, depth illusion",
    "organic tones, naturalistic colors, earthy textures, organic feel, nature-inspired hues, natural color palette",
    "surreal atmosphere, dreamlike quality, imaginative elements, fantasy-like ambiance, ethereal mood, otherworldly feel",
    "sophisticated elegance, refined style, polished aesthetics, upscale design, classy presentation, high-end quality",
    "unique perspectives, innovative angles, unusual viewpoints, creative outlooks, distinctive approach, novel framing"
]

wordy_photography_descriptions_2 = [
    "photorealistic, ultra-sharp, high fidelity, detailed textures, true-to-life colors, crisp clarity, advanced resolution",
    "4K resolution, vibrant accuracy, lifelike detail, superior quality, high dynamic range, impressive clarity, ultra-realistic",
    "high resolution, award-winning standard, exceptional clarity, fine detail, sophisticated color grading, precision focus",
    "award-winning photography, world-class quality, unparalleled resolution, artistic excellence, vivid realism, impeccable detail",
    "ultra-high definition, groundbreaking clarity, vibrant realism, sharp focus, high-end quality, dynamic lighting, vivid portrayal",
    "vivid color accuracy, true-to-life hues, professional color grading, high-quality saturation, precise chromaticity, rich vibrancy",
    "sharp focus, precise detail, high-resolution imaging, crystal-clear quality, professional standard, meticulous sharpness",
    "dynamic range, deep contrast, striking tonal depth, nuanced lighting, rich shadows, vibrant highlights, color depth",
    "deep contrast, bold shadows, striking highlights, vibrant clarity, intense tonal range, high-quality imaging, photorealistic portrayal",
    "crisp clarity, ultra-precise detail, high-end resolution, lifelike portrayal, superior imaging, professional-grade quality, clear definition",
    "rich textures, fine granularity, detailed surfaces, realistic touch, tactile realism, high-definition texture, photographic quality",
    "fine details, micro-level precision, high-resolution clarity, intricate portrayal, sophisticated imaging, detailed realism, precise rendering",
    "balanced composition, harmonious layout, professional framing, artistic arrangement, sophisticated design, expertly composed",
    "artistic excellence, creative mastery, innovative design, professional artistry, superior craftsmanship, leading-edge creativity",
    "innovative lighting, advanced illumination techniques, professional lighting, high-quality effects, dynamic shadows, vivid highlights",
    "subtle tones, nuanced shading, sophisticated palette, gentle contrasts, refined colors, understated elegance, artistic subtlety",
    "sophisticated style, refined aesthetics, elegant design, high-class portrayal, upscale quality, stylish presentation, professional elegance",
    "elegant simplicity, minimalist design, clean lines, understated beauty, sophisticated minimalism, refined simplicity, artistic purity",
    "professional standard, industry-leading quality, top-tier resolution, expert-grade craftsmanship, high-end portrayal, elite performance",
    "cutting-edge quality, advanced technology, leading-edge clarity, innovative resolution, futuristic imaging, next-generation portrayal"
]

simple_sharp_realistic_prompts = [
    "photorealistic",
    "4K resolution",
    "high resolution",
    "award winning photography",
    "hyper-realistic",
    "RAW photo",
]

exaggerated_photo_prompts = [
    "hyper-realistic, ultra-detailed snapshot",
    "white balance ensures accurate colors. Super-resolution techniques capture intricate details with remarkable clarity. The Pro Photo RGB color space enriches vibrancy, while lighting techniques create a stunning scene",
    "400-megapixel resolution and unparalleled image quality",
    "With a shutter speed of 1/1000 and an aperture of F/22, the lighting is balanced beautifully. The carefully calibrated white balance ensures accurate colors in the 32k resolution.",
    "Shot on a 25mm lens, depth of field and tilt blur create a compelling narrative. With settings like 1/1000 shutter speed, F/22 aperture, and calibrated white balance, the breathtaking 32k resolution reveals remarkable details.",
]

camera_phrases_short = [
    "Taken with meticulous precision using a high-end Sony α7R IV camera, renowned for its exceptional image quality",
    "Utilizing a high-end Nikon D850 camera with a 50mm lens",
    "With calibrated white balance and precise color grading, every detail is faithfully captured",
    "Harnessing the power of advanced high-tech cameras, such as the Sony α7R IV and the Nikon Z9, every aspect is captured with remarkable precision.",
    "Leica M10-R and the Canon EOS R5 capture each detail with utmost precision",
    "remarkable capabilities of the revered Canon EOS R5 camera, coupled with a premium 100mm lens opened wide to an alluring F 1.2 aperture",
]

camera_phrases_long = [
    "Taken with meticulous precision using a high-end Sony α7R IV camera, renowned for its exceptional image quality",
    "Utilizing a high-end Nikon D850 camera with a 50mm lens",
    "With calibrated white balance and precise color grading, every detail is faithfully captured",
    "Harnessing the power of advanced high-tech cameras, such as the Sony α7R IV and the Nikon Z9, every aspect is captured with remarkable precision.",
    "the image is taken b yLeica M10-R and the Canon EOS R5 capture each detail with utmost precision",
    "This images explores the remarkable capabilities of the revered Canon EOS R5 camera, coupled with a premium 100mm lens opened wide to an alluring F 1.2 aperture",
    "Photography enhanced with The unparalleled resolution of the Fujifilm GFX 100 ensures every image is a masterpiece of clarity",
    "taken with Canon EOS-1D X Mark III - synonymous with speed and precision in the world of professional photography",
    "taken with the Panasonic Lumix S1R delivers stunning images with its high-resolution sensor and exceptional dynamic range",
    "photography with Olympus OM-D E-M1X, an engineering marvel, offers unmatched stabilization and speed",
    "RAW photo shot with Hasselblad X1D II 50C - a paradigm of medium format photography, renowned for its unparalleled image quality",
    "Stunning cinematography with a Phase One XT, a high-end camera system offering extreme resolution and superb color accuracy",
    "Capturing the essence of professionalism with the Sony α9 II, known for its blazing fast autofocus and high-speed continuous shooting",
    "award winning photography with The Nikon Z7 II, with its high resolution and dual processors, ensures unmatched image quality and speed",
    "perfect photo from a Pentax K-1 Mark II, distinguished by its robust build and exceptional image stabilization capabilities",
    "Utilizing the advanced medium format Hasselblad H6D-100c for images with extraordinary detail and dynamic range",
    "The precision of the Leica SL2, a masterpiece of design and engineering in the world of professional cameras",
    "captured with a Sigma fp L, a compact yet powerful camera offering stunning image quality and versatility",
    "Bringing the power of medium format in a compact form with the Fujifilm GFX 50S II",
    "The dynamic range and image quality of the Canon EOS R3 set a new standard in the world of professional photography"
]



generic_hq_photography_keywords = [
    "ultra-high definition",
    "vivid color accuracy",
    "perfect sharp focus",
    "stunning dynamic range",
    "deep contrast",
    "crisp clarity",
    "balanced composition",
    "artistic excellence",
    "innovative lighting",
    "elegant simplicity",
    "professional standard",
    "cutting-edge quality"
]

## Cinematic modifiers


cinematic_shot_types = [ 
    "Aerial shot",
    "Close-up shot",
    "Crowd shot",
    "Establishing shot",
    "Extreme close-up",
    "Low angle shot",
    "over-the-shoulder shot",
    "Handheld shot",
]

cinematic_film_types = [
    "16mm",
    "35mm",
    "70mm",
    "prores",
    "Super 8mm",
    "8mm",
    "4k resolution",
    "28mm",
]

cinematic_color_grading = [
    "cool-toned color grading",
    "pastel color grading",
    "bright color grading",
    "vibrant color grading",
    "muted color grading",
    "neon color grading",
    "warm color grading",
    "duotone color grading",
]

cinematic_effects = [
    "cgi",
    "chromatic aberrations",
    "cinemascope",
    "light leaks",
    "bokeh",
    "depth of field",
    "rear projection",
    "starbursts",
]

cinematic_genres = [
    "adventure",
    "b-horror",
    "epic fantasy",
    "film noir",
    "horror",
    "indie",
    "western",
    "thriller",
]

cinematic_style_activator = [
    "cinematic shot"
]

# Random Cinematic prompt
# Given a base prompt, append a prompt from each cinematic category
def random_cinematic_prompt(base_prompt):
    cinematic_prompt = cinematic_style_activator
    cinematic_prompt += f" {base_prompt}"
    cinematic_prompt += f" {random.choice(cinematic_shot_types)}"
    cinematic_prompt += f" {random.choice(cinematic_film_types)}"
    cinematic_prompt += f" {random.choice(cinematic_color_grading)}"
    cinematic_prompt += f" {random.choice(cinematic_effects)}"
    cinematic_prompt += f" {random.choice(cinematic_genres)}"
    return cinematic_prompt