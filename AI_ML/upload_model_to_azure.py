from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient
from transformers import AutoModelForQuestionAnswering, AutoTokenizer
import os

load_dotenv()  # Load the environment variables from .env file
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

blob_service_client = BlobServiceClient.from_connection_string(connection_string)
containers = blob_service_client.list_containers()

for container in containers:
    print(container.name)


# Specify the model you want to capture (e.g., BERT for QA)
model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"

# Download and load the pre-trained model and tokenizer
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Save the model locally to isolate it (i.e., save all necessary files)
model.save_pretrained("./bert_model")
tokenizer.save_pretrained("./bert_model")


container_name = "ml-poc-container"  # Replace with your container name
container_client = blob_service_client.get_container_client(container_name)

# Specify the local directory containing the isolated model files
model_directory = './bert_model'

# Upload files from the local directory to Azure Blob Storage
for filename in os.listdir(model_directory):
    file_path = os.path.join(model_directory, filename)
    
    # Create a BlobClient for each file
    blob_client = container_client.get_blob_client(filename)
    
    # Upload the file to Azure Blob Storage
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
    print(f"File '{filename}' uploaded successfully.")
