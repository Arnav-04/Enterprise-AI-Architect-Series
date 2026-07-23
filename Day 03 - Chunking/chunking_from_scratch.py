document = "Artificial Intelligence (AI) is a branch of computer science focused on building machines capable of performing tasks that typically require human intelligence. These tasks include learning from data, recognizing patterns, understanding human language, solving problems, and making decisions."

#length of the document
document_length=len(document)

#process of chunking
chunk_size=100

chunks=[]

for i in range(0,document_length,chunk_size):
    chunk=document[i:i+chunk_size]
    chunks.append(chunk)

#getting the chunks with index
for index,chunk in enumerate(chunks,start=1):
    print(f"\n Chunk {index}")
    print(chunk)