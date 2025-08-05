Kanav Kapur AI Testcases Summer 2025
Overview
This repository contains AI test cases focused on finance topics, developed as part of the Summer 2025 project. The goal is to evaluate how well large language models (LLMs) like ChatGPT respond to realistic financial questions using programmatic metrics from the GAICO evaluation toolkit.

Repository Structure
data/
Contains JSON files defining test cases. Each file includes the test case ID, question, reference answers, ideal answer features, and harm risks.

code/
Includes Python scripts and notebooks for running the GAICO evaluation on the test cases, calling LLM APIs, and processing the results.

results/
Markdown or text files summarizing the model responses, evaluation metrics (e.g., BLEU, ROUGE, BERTScore), and explanations for each test case.

How to Use
The test cases in the data folder can be loaded into the GAICO framework to evaluate model responses.

The code in the code folder demonstrates how to call an LLM, collect responses, and run the evaluation.

The results folder contains detailed summaries and interpretations of the evaluation metrics for each test case.

Requirements
Python 3.10 - 3.12 (compatible with GAICO)

GAICO library installed (pip install gaico)

Additional dependencies for optional metrics (e.g., pip install gaico[bertscore])

Contact
Kanav Kapur
Email: kanavk14@gmail.com
