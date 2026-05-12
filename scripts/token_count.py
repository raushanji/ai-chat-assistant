import tiktoken

encoding = tiktoken.encoding_for_model(
    "gpt-4"
)

text = "AI agents are powerful"

tokens = encoding.encode(text)

print(tokens)

print("Token count:", len(tokens))