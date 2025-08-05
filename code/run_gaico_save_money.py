import json
from gaico.experiment import Experiment

with open(r"C:\Users\kanav\OneDrive\Desktop\Gaico Test Case\kanav_save_money_testcase.json", "r", encoding="utf-8") as f:
    testcase = json.load(f)

with open(r"C:\Users\kanav\OneDrive\Desktop\Gaico Test Case\chatgpt_save_money_response.json", "r", encoding="utf-8") as f:
    response_data = json.load(f)
    response = response_data["response"]

experiment = Experiment(llm_responses={"chatgpt": response}, reference_answer=testcase["reference_answer"])
df = experiment.to_dataframe()
print(df)
