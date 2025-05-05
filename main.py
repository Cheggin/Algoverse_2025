from openai import OpenAI
import json
import re
import os 
client = OpenAI()

all_questions = ""
all_responses = {}
with open('./GAIA/2023/test/metadata.jsonl') as f:
    data = [json.loads(line) for line in f if line.strip()]
    all_questions = data
"""
all_questions: list of dictionaries; keys: 'task_id', 'Question', 'Level', 
'file_name', 'Final answer', 'Annotator Metadata'
"""    
for question in all_questions:
    response = client.responses.create(
        model="gpt-4.1-nano",
        input="You will be given a task. Break it down into the minimal number of optimal logically necessary steps that would allow someone to complete the task without skipping reasoning. Focus on optimal step granularity—not too detailed, but not too vague. Output the steps as a comma-separated list with no explanations. Task: " + question["Question"]
    )
    all_responses[question["task_id"]] = response.output_text

"""
all_responses: dictionary of task id keys, comma-separated values as paths
"""

responses_path = "all_responses.json"
with open(responses_path, 'w') as f:
    json.dump(all_responses, f)
