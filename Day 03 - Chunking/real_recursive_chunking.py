document = """
Artificial Intelligence is transforming enterprises by automating repetitive tasks, improving decision making, optimizing supply chains, enhancing customer experiences, reducing operational costs, increasing productivity, enabling innovation, supporting business growth, improving forecasting, and helping organizations compete globally.
"""

#use of the recursive chunking

def recursive_chunk(text,chunk_size):
    if len(text)<=chunk_size:
        return [text]

    sentences=text.split(".")
    chunks=[]

    for sentence in sentences:
        sentence=sentence.strip()

        if sentence:
            chunks.extend(recursive_chunk(sentence,chunk_size))

    return chunks

chunks=recursive_chunk(document,80)

for index,chunk in enumerate(chunks, start=1):
    print(f"\n Chunk {index}")
    print(chunk)