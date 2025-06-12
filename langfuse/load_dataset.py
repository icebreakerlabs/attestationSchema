import json
from langfuse import get_client
from langfuse_handler import ExperimentRunner
import os
import dotenv
import asyncio

# dotenv.load_dotenv()

# os.environ["LANGFUSE_PUBLIC_KEY"] = os.getenv("LANGFUSE_PUBLIC_KEY")
# os.environ["LANGFUSE_SECRET_KEY"] = os.getenv("LANGFUSE_SECRET_KEY")
# os.environ["LANGFUSE_HOST"] = os.getenv("LANGFUSE_HOST")

# langfuse = get_client()

# dataset = langfuse.get_dataset("generated_attestations")

# items = dataset.items
# print(items[50].expected_output)

# print(items[0].run(run_name="get-schema-test4"))

experiment_runner = ExperimentRunner(env_path="../.env")

run_data = asyncio.run(
    experiment_runner.get_dataset_run(
        "generated_attestations",
        "get-schema-test4",
        trace_info=['input', 'output', 'scores'],
        dataset_item_info=['expected_output'],
        limit=10,
        requests_per_minute=500,
        )
    )

with open("../data/run_data.json", "w") as f:
    json.dump(run_data, f, indent=4)




