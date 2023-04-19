import json
import os
import openai
import pandas as pd

openai.api_key = os.getenv("OPENAI_API_KEY")
with open('prompts.json', 'r') as f:
    prompts = json.load(f)
print(prompts)
df = pd.DataFrame()
response = openai.ChatCompletion.create(
    # model="davinci:ft-personal:metapath-2023-03-28-02-42-17",
    model="gpt-4",
    messages=[{"role": "user", "content": prompts[0]}],
    temperature=1
)
finish_reason = response['choices'][0]['finish_reason']
response_txt = response['choices'][0]['message']["content"]
response_role = response['choices'][0]['message']["role"]
new_row = {
    'prompt': prompts[0],
    'completion': response_txt,
    'finish_reason': finish_reason,
    'role': response_role
}
new_row = pd.DataFrame([new_row])
df = pd.concat([df, new_row], axis=0, ignore_index=True)
df.to_csv("out_openai_completion_gpt4_1.csv")
