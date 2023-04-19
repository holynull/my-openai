import json
import os
import openai
import pandas as pd
from transformers import GPT2TokenizerFast 
from nltk.tokenize import sent_tokenize

tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

max_token_len = 2048


def count_tokens(text: str) -> int:
    """count the number of tokens in a string"""
    return len(tokenizer.encode(text))


def reduce_long(
    long_text: str, long_text_tokens: bool = False, max_len: int = 590
) -> str:
    """
    Reduce a long text to a maximum of `max_len` tokens by potentially cutting at a sentence end
    """
    if not long_text_tokens:
        long_text_tokens = count_tokens(long_text)
    if long_text_tokens > max_len:
        sentences = sent_tokenize(long_text.replace("\n", " "))
        ntokens = 0
        for i, sentence in enumerate(sentences):
            ntokens += 1 + count_tokens(sentence)
            if ntokens > max_len:
                return ". ".join(sentences[:i]) + "."

    return long_text


openai.api_key = os.getenv("OPENAI_API_KEY")
with open('data/data.json', 'r') as f:
    data = json.load(f)
df = pd.DataFrame()
for d in data:
    if count_tokens(d["completion"])+4 < max_token_len:
        t = count_tokens(d["completion"])+4
        c = d["completion"]
    else:
        c = reduce_long(d["completion"])
        t = count_tokens(d['completion'])
    new_row = {
        "title": "MetaPath",
        "heading": d["prompt"],
        "content": c,
        "tokens": t,
        "context": "MetePath\n"+d["prompt"]+"\n"+c
    }
    new_row = pd.DataFrame([new_row])
    df = pd.concat([df, new_row], axis=0, ignore_index=True)
df.to_csv("data/data.csv")
