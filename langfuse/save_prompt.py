from langfuse_handler import PromptRunner
import json

prompt_runner = PromptRunner("attestation-schema", env_path="../.env")

with open("../data/prompt.json", "w") as f:
    json.dump(prompt_runner.get_prompt(), f, indent=4)