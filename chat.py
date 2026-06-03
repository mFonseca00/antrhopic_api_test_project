"""
Chat com contexto e system prompt usando o Flow Gateway.
Mantém histórico da conversa para respostas contextuais.
"""
from dotenv import load_dotenv
load_dotenv()

import os
from anthropic import Anthropic

# token = os.environ["ANTHROPIC_AUTH_TOKEN"]
# client = Anthropic(
#     base_url=os.environ["ANTHROPIC_BASE_URL"],
#     api_key="placeholder",
#     default_headers={"Authorization": f"Bearer {token}"},
# )
client = Anthropic()
model = os.environ["ANTHROPIC_MODEL"]


def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})


def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})


def chat(messages, system=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }

    if system:
        params["system"] = system

    response = client.messages.create(**params)
    return response


# System prompt define o comportamento do assistente
system_prompt = """
You are a helpful AI assistant connected through the CI&T Flow Gateway.
Be concise, friendly and respond in the same language as the user.
"""

print("🤖 Chat com Claude via Flow Gateway")
print(f"   Modelo: {model}")
print("   Digite 'sair' para encerrar.\n")

messages = []
total_in = 0
total_out = 0

while True:
    prompt = input("Você: ").strip()
    if not prompt or prompt.lower() == "sair":
        print(f"\n📊 Total da sessão: {total_in} tokens in / {total_out} tokens out")
        print("👋 Até mais!")
        break

    add_user_message(messages, prompt)
    response = chat(messages, system=system_prompt)
    reply = response.content[0].text
    add_assistant_message(messages, reply)

    total_in += response.usage.input_tokens
    total_out += response.usage.output_tokens

    print(f"\nClaude: {reply}")
    print(f"📊 Tokens: {response.usage.input_tokens} in / {response.usage.output_tokens} out | Total: {total_in} in / {total_out} out\n")