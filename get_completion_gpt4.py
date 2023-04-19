import json
import os
import openai
import pandas as pd
import time

openai.api_key = os.getenv("OPENAI_API_KEY")
with open('prompts.json', 'r') as f:
    prompts = json.load(f)
print(prompts)
df = pd.DataFrame()
for prompt in prompts:
    for i in range(3):
        start_time = time.perf_counter()
        response = openai.ChatCompletion.create(
            # model="davinci:ft-personal:metapath-2023-03-28-02-42-17",
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=1
        )
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time} s")
        finish_reason = response['choices'][0]['finish_reason']
        response_txt = response['choices'][0]['message']["content"]
        response_role = response['choices'][0]['message']["role"]
        new_row = {
            'prompt': prompt,
            'completion': response_txt,
            'finish_reason': finish_reason,
            'role': response_role
        }
        new_row = pd.DataFrame([new_row])
        df = pd.concat([df, new_row], axis=0, ignore_index=True)
        df.to_csv("out_openai_completion_gpt4.csv")
