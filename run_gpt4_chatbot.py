import itertools
import os
import openai
from dotenv import load_dotenv
import asyncio
import json
import sys
import argparse

load_dotenv()
parser = argparse.ArgumentParser(description='Chat to GPT4')
parser.add_argument('-c', '--conversation_ctx',
                    help='Conversation context file')
args = parser.parse_args()
conversation_ctx = args.conversation_ctx


def print_colored_text(text, color):
    color_code = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "reset": "\033[0m",
    }
    print(f"{color_code[color]}{text}{color_code['reset']}")


async def spinning_slash():
    # 定义一个斜杠列表
    spinning_chars = itertools.cycle('/-\|')
    # spinning_chars = itertools.cycle('....')
    # 不停地输出旋转斜杠
    while True:
        print_colored_text(next(spinning_chars), "yellow")
        # print_colored_text("Loading....","yellow")
        sys.stdout.flush()
        await asyncio.sleep(0.1)
        sys.stdout.write('\b')

openai.api_key = os.getenv("OPENAI_API_KEY")
context = [{"role": "system", "content": "You are a helpful assistant."}]
if conversation_ctx != None:
    with open(conversation_ctx, "r") as file:
        context = json.load(file)


async def chatToGPT4(_ctx):
    response = openai.ChatCompletion.create(
        # model="davinci:ft-personal:metapath-2023-03-28-02-42-17",
        model="gpt-4",
        messages=_ctx,
        temperature=1
    )
    finish_reason = response['choices'][0]['finish_reason']
    response_txt = response['choices'][0]['message']["content"]
    response_role = response['choices'][0]['message']["role"]
    sys.stdout.flush()
    print_colored_text("GPT-4:", "green")
    print(response_txt)
    context.append({"role": response_role, "content": response_txt})


async def main():
    while True:
        print_colored_text("Input:", "green")
        user_input = input("")
        if user_input == "exit":
            with open("conversation_ctx.json", "w") as json_file:
                json.dump(context, json_file)
            break
        context.append({"role": "user", "content": user_input})
        spinner_task = asyncio.create_task(spinning_slash())
        gpt4_task = asyncio.create_task(chatToGPT4(context))
        await gpt4_task
        # await asyncio.sleep(10)
        spinner_task.cancel()
asyncio.run(main())
