import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
# 获取当前目录
current_directory = os.getcwd()

# 定义要读取的文件名
file_name = "prompts.txt"

# 拼接当前目录和文件名
file_path = os.path.join(current_directory, file_name)

# 使用open()函数以读取模式打开文件
with open(file_path, 'r', encoding='utf-8') as file:
    # 读取文件内容
    prompts = file.read()
print(prompts)
response = openai.ChatCompletion.create(
    # model="davinci:ft-personal:metapath-2023-03-28-02-42-17",
    model="gpt-4",
    # messages=[{"role": "user", "content": prompts}],
	messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ],
    temperature=1
)
finish_reason = response['choices'][0]['finish_reason']
response_txt = response['choices'][0]['message']["content"]
response_role = response['choices'][0]['message']["role"]
print(response_txt)