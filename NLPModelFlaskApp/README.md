# Simple Text Summarization App

## Goal
This repo is a personal experiment for me to learn different ways to deploy a NLP model. The final goal is: 

- Hosting a text summarization model based on Pegasus (model size >= 2GB) (https://huggingface.co/SophieTr/fine-tune-Pegasus)

- Serving the model with minimal latency 

- Minimal hosting cost 

## Experiment
- 14th Feb 2022: first trial deploying a small NLP model (https://huggingface.co/sshleifer/distilbart-cnn-6-6) from HuggingFace
    - Model: this model is fine-tuned for text summarization with facebook BART algorithm. 
    - Host: Heroku
    - Result: the web app couldn't be deployed due ro R15 error - "- Memory quota vastly exceeded". This is because the size of dependencies and NLP model exceeded the 500MB limit of Heroku
    - Test performance on local host: clone the repo and run ```python3 app.py```
    - TO DO:
        - What if I don't call model.generate(...) but model(...)?
        - Look for different options: Google Cloud Platform, AWS and compare
    