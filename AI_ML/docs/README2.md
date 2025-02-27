# User Story: Evaluating Model Performance on CPU vs. GPU

## Overview
This document outlines my exploration of different question-answering models, comparing their responses and inference times when run on CPU and GPU. The goal is to determine the practical benefits of using GPU power for running machine learning models.

## Models Tested
I initially ran various models, including:
- BERT
- T5
- distilbert
- RoBERTa
- ALBERT

### Reason for Model Selection
I chose these models because they are relatively small and can be easily run on my local machine. However, I struggled to identify significant differences in effectiveness between running them on GPU versus CPU.

## Transition to Larger Models
To gain clearer insights, I switched to larger models like LLaMA and Phi. This change allowed for a more pronounced evaluation of performance differences.

## GPU Utilization
I set up GPU computing on Azure ML Studio and executed the inference scripts in a Jupyter Notebook environment. 

### Results
The difference in inference times between CPU and GPU was very noticeable. The GPU significantly outperformed the CPU in handling larger models, highlighting the advantages of GPU acceleration for computationally intensive tasks.

## Conclusion
This experience emphasized the importance of GPU power in modern machine learning applications, especially for larger models. The need for GPU resources becomes increasingly critical as models grow in complexity and size, enabling faster processing and better overall performance.
