import json
import os
import openai
import pandas as pd

openai.api_key = os.getenv("OPENAI_API_KEY")
with open('prompts.json', 'r') as f:
    prompts = json.load(f)
print(prompts)
df = pd.DataFrame()
for prompt in prompts:
	for i in range(3):
		response = openai.Completion.create(
    	    # model="davinci:ft-personal:metapath-2023-03-28-02-42-17",
    	    model="davinci:ft-personal:metapath-2023-03-28-02-42-17",
    	    prompt=prompt,
    	    temperature=1,
    	    max_tokens=500,
    	    top_p=1,
    	    frequency_penalty=0,
    	    presence_penalty=0,
    	    stop=[" END"]
    	)
		finish_reason = response['choices'][0]['finish_reason']
		response_txt = response['choices'][0]['text']
		new_row = {
    	    'prompt': prompt,
    	    'completion': response_txt,
    	    'finish_reason': finish_reason}
		new_row = pd.DataFrame([new_row])
		df = pd.concat([df, new_row], axis=0, ignore_index=True)
df.to_csv("out_openai_completion_gpt3.csv")
