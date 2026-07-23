document = """
Artificial Intelligence is transforming enterprises.

Large Language Models have limited context windows.

Recursive chunking preserves complete ideas.

It improves retrieval accuracy.
"""

#declaring the function for recursive chunking
def recursive_chunk(text, chunk_size):
    if len(text)<=chunk_size:
        return [text]
    return text.split(".")

#testing
chunks=recursive_chunk(document,80)

for index,chunk in enumerate(chunks, start=1):
    print(f"\n Chunk {index}")
    print(chunk)