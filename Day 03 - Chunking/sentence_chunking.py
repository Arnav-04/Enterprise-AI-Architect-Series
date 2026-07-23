document = """
Artificial Intelligence is transforming enterprises.

Large Language Models have limited context windows.

Recursive chunking preserves complete ideas.

It improves retrieval accuracy.
"""

#splitting the sentence
sentences=document.split(".")
print(sentences)

for index,sentence in enumerate(sentences,start=1):
    print(f"\n Sentence {index}")
    print(sentence)

#declaring chunks
chunks=[]

for sentence in sentences:
    sentence=sentence.strip()
    
    if sentence:
        chunks.append(sentence)

for index, chunk in enumerate(chunks, start=1):
    print(f"\n Chunks {index}")
    print(chunk)