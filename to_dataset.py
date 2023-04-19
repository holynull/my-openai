import pandas as pd
import openai
import time
df_qa = pd.read_csv('data/data_qa_35.csv')
df=pd.DataFrame()

def get_prompt_completion(row):
    questions=row["questions"].split("\n")
    questions = [s[2:] for s in questions]
    answers=row["answers"].split("\n")
    answers = [s[2:] for s in answers]
    result=[]
    for i,q in enumerate(questions):
        new_row = {
            'prompt': q+"\n\n###\n\n",
            'completion': answers[i]+"\n\n===\n\n",
        }
        result.append(new_row)
    return result 

for i,row in df_qa.iterrows():
    nrow=get_prompt_completion(row=row)
    nr = pd.DataFrame(nrow)
    df = pd.concat([df, nr], axis=0, ignore_index=True)

df.to_csv('data/dataset_35.csv', index=False)
