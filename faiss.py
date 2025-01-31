# OpenAIEmbddings is deprecated and needs to be resolved

from langchain_community.embeddings import OpenAIEmbeddings # Deprecated import statement
from langchain_community.vectorstores import FAISS

# Step 1: Read the extracted text from the file
def read_extracted_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Step 2: Split the text into smaller chunks
def split_text_into_chunks(text, chunk_size=500, overlap=50):
    """
    Splits the text into chunks of a specified size with overlap.
    :param text: The input text to split.
    :param chunk_size: The size of each chunk (in characters).
    :param overlap: The number of overlapping characters between chunks.
    :return: A list of text chunks.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap  # Overlap chunks for context continuity
    return chunks

# Step 3: Load embeddings and create the FAISS vector store
def create_vector_store(text_chunks):
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_texts(text_chunks, embeddings)
    return vector_store

# Main execution
if __name__ == "__main__":
    # Path to the extracted text file
    extracted_text_file = "extracted_text.txt"

    # Step 1: Read the extracted text
    extracted_text = read_extracted_text(extracted_text_file)

    # Step 2: Split the text into chunks
    text_chunks = split_text_into_chunks(extracted_text)

    # Step 3: Create the FAISS vector store
    vector_store = create_vector_store(text_chunks)

    # Save the vector store to disk for later use
    vector_store.save_local("cfa_vector_store")
    print("FAISS vector store created and saved successfully!")