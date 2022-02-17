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
        - Look for different options: Google Cloud Platform, AWS, Azure, etc.

- 17th Feb 2022: there are several options for hosting and serving ML models. Depending on the stage of development and deployment, different options can be utilize. 
    - Demo and sharing results: Huggingface Space 
        - #### Link for the demo ####: https://huggingface.co/spaces/SophieTr/TextSummarizationDemo
    - Own model serving: TorchServe (TODO: add link)
    - Controlling dependency: Dockers
    - Scaling: Kubernetes
    - Cloud deploy: GoogleCloud (free 300$), Azure, AWS SageMaker (or other products) --> can be quite pricy (link for comparison: https://pankajconnect.medium.com/aws-azure-and-google-cloud-which-free-tier-is-best-1139e7abf49a)
    - Automated CI/CD pipeline: DataRobot
    - Reading source: 
        - https://www.freecodecamp.org/news/deploy-your-machine-learning-models-for-free/
        - https://towardsdatascience.com/3-steps-to-build-and-deploy-your-nlp-model-as-a-microservice-on-azure-426ca77c66df
        - https://medium.com/microsoftazure/azure-functions-for-ml-4440bee58621
        - https://medium.com/pytorch/efficient-serverless-deployment-of-pytorch-models-on-azure-dc9c2b6bfee7
        - https://www.freecodecamp.org/news/what-we-learned-by-serving-machine-learning-models-using-aws-lambda-c70b303404a1/
    
## NOTE: 
Should probably move this into my own blog 