from wsgiref.util import request_uri
from flask import Flask, request, render_template, redirect
from transformers import BartTokenizer, BartForConditionalGeneration

# preprocess input
# return input_ids matrix
tokenizer = BartTokenizer.from_pretrained("sshleifer/distilbart-cnn-6-6")
model = BartForConditionalGeneration.from_pretrained("sshleifer/distilbart-cnn-6-6")

def preprocess(inp):
    input_ids = tokenizer(inp, return_tensors="pt").input_ids
    return input_ids
def predict(input_ids):
    outputs = model.generate(input_ids=input_ids)
    res = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
    return res

# Set up flask
app = Flask(__name__)

# Set up flask routes:
# Get:
# Home page

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        inp = request.form['content']
        inp_ids = preprocess(inp)
        summary = predict(inp_ids)
        return render_template('index.html', summary=summary)
    else:
        print("GETTING get")
        return render_template('index.html', summary="Nothing to summarize")

# Post route: 
# Retrieve result



if __name__ == '__main__':
    app.run(debug=True)
