import json
from gaico.experiment import Experiment
import pprint

# Load LLM responses
with open(r"C:\Users\kanav\OneDrive\Desktop\Gaico Test Case\chatgpt_creditcard_response.json", "r") as f:
    llm_responses = json.load(f)

# Reference answer string you wrote manually
reference_answer = (
    "It depends on your financial habits and goals. "
    "Generally, 1 to 3 credit cards is recommended to maintain a good credit score while avoiding debt risks."
)

# Create Experiment object
experiment = Experiment(llm_responses, reference_answer)

# Run comparison (evaluation)
result = experiment.compare()

# Print results
pprint.pprint(result)
