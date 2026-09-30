from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

loader = PyPDFLoader("check3.pdf")
documents = loader.load()
print("this is the first page data:")
print("/n" )

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
   
)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0
)

chunks = splitter.split_documents(documents)

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

query = "write summary short summary of this document in 50 words"
final=""
results = retriever.invoke(query)
for doc in results:
    final = final + doc.page_content
    final+= " "


print(final)

