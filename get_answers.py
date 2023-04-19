import pandas as pd
import openai
import time
df = pd.read_csv('data/data_q_35.csv')

def get_answers_from_gpt35(row)->str:
    start_time = time.perf_counter()
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Write answer based on the text below\n\nText: {row.context}\n\nQuestions:\n{row.questions}\n\nAnswers:\n1.",
        temperature=0,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"API Elapsed time: {elapsed_time} s")
    txt=response['choices'][0]['text']
    print(f"Response:\n1. {txt}")
    return txt


df['answers']= df.apply(get_answers_from_gpt35, axis=1)
df['answers'] = "1." + df.answers
df = df.dropna().reset_index().drop('index',axis=1)
df.to_csv('data/data_qa_35.csv', index=False)
