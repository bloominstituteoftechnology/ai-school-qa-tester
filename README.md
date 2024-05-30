# AI For Developer Productivity: Tester Agent

## Overview

In this project, we developed a Tester Agent designed to enhance developer productivity by generating and running unit tests on any Python code. The project includes a script (`tester.py`) for building and testing, as well as fine-tuning the Davinci model to see if it can perform as effectively as GPT-4 when creating unit tests.

## Now It's Your Turn!

Dive into this project and see how the Tester Agent can revolutionize your workflow by automatically generating unit tests. Here’s a step-by-step guide to get you started and help you customize the project to your needs:

### Understand how `tester.py` works
- Familiarize yourself with the tester.py script to understand its functionality and how it integrates with the AI model to generate unit tests.

### Run the agent with GPT-3.5 or GPT-4
- Execute the Tester Agent using GPT-3.5 or GPT-4 models and evaluate the generated unit tests to see how well they perform.

### Fine-tune Davinci using provided data in `data.py`
- Use the provided training data in data.py to fine-tune the Davinci model. You can also generate additional data if needed to improve the model’s performance.

### Change the LLM in `tester.py`
- Replace the existing language model in tester.py with the fine-tuned Davinci model and assess if it performs as well as a chat model in creating unit tests.

## Minimum Requirements

1. **Fine-tune a Smaller Model**: Fine-tune a smaller model using OpenAI or leverage Hugging Face with PeFT/QLoRA to fine-tune.
2. **Integrate the Fine-tuned Model**: Use the fine-tuned model inside the agent and evaluate its performance in generating unit tests.

## Stretch Goals

- **Generate More Synthetic Data**: Create a substantial amount of synthetic data to fine-tune a model that matches the performance of GPT.
- **Implement Evaluation Metrics**: Develop evaluation metrics to assess which model performs better in generating unit tests.

## Privacy and Submission Guidelines

- **Submission Requirements**: Submit a link to your public repository with your implementation or a Loom video showcasing your work on the BloomTech AI Platform.
- **Sensitive Information**: If your implementation involves sensitive information, you can submit a detailed review of your project through a Loom video, demonstrating the functionality and discussing the technologies used without exposing confidential data.