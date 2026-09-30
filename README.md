<h1>🔎 Retriever using LangChain</h1>

<p>
This project demonstrates how to create a <strong>Retriever</strong>
using LangChain, OpenAI Embeddings, and Chroma Vector Store.
</p>

<h2>📌 What I Learned</h2>

<ul>
    <li>Created document chunks using <strong>RecursiveCharacterTextSplitter</strong>.</li>
    <li>Converted text chunks into vector embeddings using <strong>OpenAI Embeddings</strong>.</li>
    <li>Stored embeddings in <strong>Chroma Vector Store</strong>.</li>
    <li>Converted the vector store into a <strong>Retriever</strong>.</li>
    <li>Used the retriever to search for relevant documents based on a query.</li>
    <li>Learned the difference between a <strong>Vector Store</strong> and a <strong>Retriever</strong>.</li>
</ul>

<h2>🔄 RAG Retrieval Flow</h2>

<pre>
Documents
    ↓
Document Loader
    ↓
Text Splitter
    ↓
Chunks
    ↓
OpenAI Embeddings
    ↓
Chroma Vector Store
    ↓
Retriever
    ↓
Relevant Documents
</pre>

<h2>🧠 Key Concepts</h2>

<h3>Embeddings</h3>

<p>
Embeddings convert text into numerical vectors that represent
the semantic meaning of the text.
</p>

<h3>Vector Store</h3>

<p>
A vector store stores embeddings and allows similarity searches
to find relevant documents.
</p>

<h3>Retriever</h3>

<p>
A retriever searches the vector store and returns the most
relevant documents for a user query.
</p>

<h2>💻 Example</h2>

<pre>
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

results = retriever.invoke(
    "What is the Constitution of India?"
)

for doc in results:
    print(doc)
</pre>

<h2>📦 Technologies Used</h2>

<ul>
    <li>Python</li>
    <li>LangChain</li>
    <li>OpenAI Embeddings</li>
    <li>Chroma</li>
    <li>Vector Search</li>
    <li>RAG</li>
</ul>

<h2>🎯 Key Takeaway</h2>

<p>
The <strong>Vector Store</strong> stores the embedded documents,
while the <strong>Retriever</strong> uses the vector store to
find relevant documents for a given query.
</p>
