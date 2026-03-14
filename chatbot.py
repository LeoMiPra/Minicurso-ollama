
from __future__ import annotations

from typing import Generator

import ollama

# --------- Customize this line to change the system prompt --------- #
SYSTEM_PROMPT = "You are a helpful assistant that provides concise and accurate answers to user questions. Always respond in brazilian portuguese. If you don't know the answer, say you don't know instead of making something up."
# ------------------------------------------------------------------ #

MODEL_NAME = "llama3.2:3b"


def stream_chat_response(messages: list[dict[str, str]]) -> Generator[str, None, None]:
    """Yield incremental text chunks from the model."""

    client = ollama.Client()
    # `stream=True` makes this return a generator of ChatResponse chunks.
    for chunk in client.chat(model=MODEL_NAME, messages=messages, stream=True):
        # Each chunk is a ChatResponse Pydantic model; its `message.content` field contains
        # the next piece of text (may be None for non-token chunks).
        if chunk.message and chunk.message.content:
            yield chunk.message.content


def main() -> None:
    print(f"Using model: {MODEL_NAME}")
    print("Type something and press ENTER. (Empty input to exit.)\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            print("Exiting.")
            return

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input},
        ]

        print("Assistant:", end=" ", flush=True)
        for chunk in stream_chat_response(messages):
            # Print each chunk as it arrives (streaming display)
            print(chunk, end="", flush=True)
        print("\n")


if __name__ == "__main__":
    main()
