# pip install fastembed langchain langchain-ollama PyMuPDF chromadb --trusted-host pypi.org --trusted-host files.pythonhosted.org


from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")
# response = llm.invoke("Hola, ¿quién eres?")
# print(response)

"""
    RAG
"""
# from langchain.document_loaders import PyMuPDFLoader
from langchain_community.document_loaders import PyMuPDFLoader

loader = PyMuPDFLoader("./src/HAI_2024_AI-Index-Report.pdf")
data_pdf = loader.load()

# el nº coincide con la pagina del pdf
# print(data_pdf[1])

# SPLIT: Debemos hacer split del texto, esto mejora el rendimiento del LLM
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=500)
docs = text_splitter.split_documents(data_pdf)
# print(docs[0])
# print(docs[1])

# EMBEDDINGS
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
embed_model = FastEmbedEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma

vs = Chroma.from_documents(
    documents=docs,
    embedding=embed_model,
    persist_directory="chroma_db_dir",  # Local mode with in-memory storage only
    collection_name="stanford_report_data"
)

# Guardar el vectorstore en disco y al consultarlo cargar 3 documentos
vectorstore = Chroma(embedding_function=embed_model,
                     persist_directory="chroma_db_dir",
                     collection_name="stanford_report_data")
retriever=vectorstore.as_retriever(search_kwargs={'k': 3})


# Creamos el prompt para el LLM
from langchain.prompts import PromptTemplate

custom_prompt_template = """Usa la siguiente información para responder a la pregunta del usuario.
Si no sabes la respuesta, simplemente di que no lo sabes, no intentes inventar una respuesta.

Contexto: {context}
Pregunta: {question}

Solo devuelve la respuesta útil a continuación y nada más y responde siempre en español
Respuesta útil:
"""
prompt = PromptTemplate(template=custom_prompt_template,
                        input_variables=['context', 'question'])


# Creamos la cadena de RAG
from langchain.chains import RetrievalQA

qa = RetrievalQA.from_chain_type(llm=llm,
                                 chain_type="stuff",
                                 retriever=retriever,
                                 return_source_documents=True,
                                 chain_type_kwargs={"prompt": prompt})


response = qa.invoke({"query": "Cual es el comportamiento de los modelos fundacionales?"})
response['result']

response = qa.invoke({"query": "que es QLoRA?, explicamelo en detalle"})
response
response['result']


metadata = []
for _ in response['source_documents']:
    metadata.append((_.metadata['page'], _.metadata['file_path']))
metadata
# # EMBEDDINGS
# from langchain.embeddings import FastEmbed
# from langchain.vectorstores import Chroma
# embedding = FastEmbed(model="all-MiniLM-L6-v2")
# vectorstore = Chroma.from_documents(docs, embedding)
# query = "¿Cuántas páginas tiene el informe?"
# docs = vectorstore.similarity_search(query)
# print(docs[0].page_content)
# # LLM
# from langchain.chains import RetrievalQA
# retriever = vectorstore.as_retriever(search_kwargs={"k": 1})                