import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.Model.list()
for model in response["data"]:
	print(model.id)