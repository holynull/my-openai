import os
import openai

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
response = openai.Completion.create(
  	    # model="davinci:ft-personal:metapath-2023-03-28-02-42-17",
  	    model="text-davinci-003",
  	    prompt=prompts,
  	    temperature=1,
  	    max_tokens=500,
  	    top_p=1,
  	    frequency_penalty=0,
  	    presence_penalty=0,
  	    stop=[" END"]
  	)
finish_reason = response['choices'][0]['finish_reason']
response_txt = response['choices'][0]['text']
print(response_txt)