import os
os.environ['OLLAMA_HOST'] = '127.0.0.1'
from vision_parse import VisionParser

parser = VisionParser(
    model_name="minicpm-v:latest",
    temperature=0.4,
    top_p=0.6,
    # num_ctx=8132,
    image_mode="path",
    # detailed_extraction=True,
    # custom_prompt=custom_prompt,
    detailed_extraction=False,
    ollama_config={
        "OLLAMA_NUM_PARALLEL": 1,
        "OLLAMA_REQUEST_TIMEOUT": 180,
    },


)

parser.convert_pdf("tests/4.pdf")