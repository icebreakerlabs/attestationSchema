from langfuse_handler import DatasetGenerator
import json


data = json.load(open("../data/sample_inputs.json"))


dataset_generator = DatasetGenerator(env_path="../.env")

dataset_generator.generate_dataset("generated_attestations", data=data)