from langfuse_handler import ExperimentRunner

def evaluator(response, item, root_span):
    match = response == item.expected_output
    root_span.score_trace(
        name="match",
        value=match,
        comment=f"Expected: {item.expected_output}, Got: {response}" if not match else None
    )

experiment_runner = ExperimentRunner(env_path="../.env")

experiment_runner.run_experiment(
    experiment_name="get-schema-test4",
    prompt_name="attestation-schema",
    dataset_name="generated_attestations",
    evaluator=evaluator,
    test_count=100
)