import pandas as pd
import openai
import time
df = pd.read_csv('data/data.csv')
df['context'] = df.title + "\n" + df.heading + "\n\n" + df.content
df.head()


def get_questions_from_gpt35(context):
    start_time = time.perf_counter()
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Write questions based on the text below\n\nText: {context}\n\nQuestions:\n1.",
        temperature=0,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n\n"]
    )
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"API Elapsed time: {elapsed_time} s")
    # txt = response['choices'][0]['message']["content"]
    txt = response['choices'][0]['text']
    print(f"Response:\n1. {txt}")
    return txt 

def get_questions_from_gpt40(context):
    start_time = time.perf_counter()
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": f"Write questions based on the text below\n\nText: {context}\n\nQuestions:\n1."}],
        temperature=0,
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n\n"]
    )
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"API Elapsed time: {elapsed_time} s")
    txt = response['choices'][0]['message']["content"]
    print(f"Response:\n1. {txt}")
    return txt 

df['questions'] = df.context.apply(get_questions_from_gpt35)
df['questions'] = "1." + df.questions
df.to_csv('data/data_q_35.csv', index=False)
