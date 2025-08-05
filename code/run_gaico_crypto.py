import json
from gaico import Experiment

# Load the test case JSON
with open(r"C:\Users\kanav\OneDrive\Desktop\Gaico Test Case\kanav_crypto_testcase.json", "r") as f:
    testcase = json.load(f)

# Load the LLM response JSON (AI's actual output to test)
with open(r"C:\Users\kanav\OneDrive\Desktop\Gaico Test Case\chatgpt_crypto_response.json", "r") as f:
    llm_response = json.load(f)

# GAICO expects llm_responses as a dict with model names as keys
llm_responses = {
    "chatgpt": llm_response["response"]
}

# Create experiment instance
experiment = Experiment(llm_responses=llm_responses, reference_answer=testcase["reference_answer"])

# Run the comparison
result = experiment.compare()

# Print or process results
print(result)

# Optionally, save results to CSV or JSON for your report
result.to_csv(r"C:\Users\kanav\OneDrive\Desktop\Gaico Test Case\crypto_experiment_results.csv")
