from langfuse_handler import PromptGenerator
import json

with open("../data/updated_prompt.json", "r") as f:
    prompt = json.load(f)

prompt_generator = PromptGenerator(env_path="../.env")

prompt_generator.generate_prompt(
    prompt_name="attestation-schema",
    prompt=prompt,
    type="chat",
    config={
        "model": "gpt-4.1-nano",
        "temperature": 0
    },
    labels=['production'],
)