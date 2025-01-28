
# **Isolating and Deploying a Large Language Model in Azure**

This project demonstrates how to isolate a pre-trained Large Language Model (LLM) from Hugging Face, upload it to Azure Blob Storage, and use it directly from our Azure environment without relying on external platforms.


## **Overview**

The goal of this project is to:
1. Select and isolate a pre-trained LLM.
2. Save the model and tokenizer files locally.
3. Upload the model to an Azure Blob Storage container.
4. Fetch the model from Azure Blob Storage and use it for inference.

This approach gives us full control over the model within our Azure cloud environment.

---

## **What Makes an LLM an LLM?**
To isolate a Large Language Model (LLM), it's important to first understand what an LLM is. LLMs are deep learning models trained on vast amounts of text data for tasks like language understanding, generation, translation, and other natural language processing (NLP) tasks. They have the following key characteristics:

Architecture: Most LLMs like BERT, GPT, etc., are based on transformer architecture.
Pretrained Weights: LLMs are trained on massive text datasets, so the most important part of the model is its pretrained weights.
Tokenizer: LLMs require a tokenizer, which is a piece of software that converts text into tokens (smaller pieces like words, sub-words, or characters) that the model can understand and process.


Model Files: The model itself consists of weights, architecture configuration, and the tokenizer.
Minimal Files to Capture an LLM:
Model Weights: A file that contains the trained parameters of the model. In the case of Hugging Face models, these are often stored as pytorch_model.bin.
Model Configuration: A configuration file that defines the architecture of the model (e.g., config.json).
Tokenizer Files: These files allow the model to interpret text, typically consisting of files like vocab.txt, tokenizer_config.json, and special_tokens_map.json.
These files are usually hosted on Hugging Face or similar platforms and can be downloaded.



## **Steps**

### **1. Isolating the Model**
- **Model Used**: `bert-large-uncased-whole-word-masking-finetuned-squad`, a BERT model fine-tuned for question answering.
- The model and tokenizer were downloaded from Hugging Face using the `transformers` library and saved locally in the `bert_model` directory.

### **2. Uploading the Model to Azure Blob Storage**
- **Storage Details**:
  - **Azure Container Name**: `ml-poc-container`
  - **Files Uploaded**:
    - `tokenizer_config.json`
    - `model.safetensors`
    - `config.json`
    - `tokenizer.json`
    - `special_tokens_map.json`
    - `vocab.txt`
- The files were uploaded using the Azure Python SDK (`azure.storage.blob`).

### **3. Fetching and Using the Model from Azure**
- The uploaded model files were retrieved from Azure Blob Storage using a Python script.
- A temporary directory was created to store the downloaded files during runtime.
- The model and tokenizer were loaded directly from the temporary directory for inference.

### **4. Performing Inference**
- A **question-answering pipeline** was created using the transformers library's pipeline API.
- Example Input:
  - **Context**: _Large Language Models (LLMs) are deep learning algorithms..._
  - **Question**: _What is LLM?_
- The pipeline return a precise answer from the given context.

---

## **Requirements**

- Python 3.8+
- Azure Storage Account

---

## **How to Run**

1. **In VS Code, Create and Activate a Virtual Environment**  
   It’s recommended to use a virtual environment to manage dependencies.  
   - On macOS/Linux:  
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - On Windows:  
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

2. **Install Required Libraries**  
   Install the necessary Python libraries specified in the `requirements.txt` file:  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the python script**  
   Copy and paste the Azure storage access key Connection String to "AZURE_STORAGE_CONNECTION_STRING" in the .env file.
   Execute the `upload_model_to_azure.py` file to download the model from Hugging Face, isolate it locally, and upload it to Azure Blob Storage:  
   ```bash
   python upload_model_to_azure.py
   ```

4. **Run the Inference Notebook**  
   Open the `call_azure_model.ipynb` Jupyter notebook and execute the cells to:  
   - Download the model files from Azure Blob Storage to a temporary directory.  
   - Load the model and tokenizer directly from the isolated environment.  
   - Perform inference using the question-answering pipeline.  

---

## **Outcome**

By following this process, the model is successfully isolated within your Azure cloud environment. You can now perform inference without relying on external model repositories like Hugging Face, giving you full control over the model.




