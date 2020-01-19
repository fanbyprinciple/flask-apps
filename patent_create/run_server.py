from flask import Flask, render_template, request
import requests

from new_utils import generate_random_start, generate_from_seed

from wtforms import (Form, TextField, validators, SubmitField, DecimalField, IntegerField)

from keras.models import load_model
import tensorflow as tf

def load_keras_model():
    global model
    model = load_model('train-embeddings-rnn-bidirectional.h5')

    global graph
    graph = tf.get_default_graph()

load_keras_model()

class ReusableForm(Form):
    seed = TextField("Enter a seed string or 'random' : ", validators=[validators.InputRequired()])
    diversity = DecimalField('Enter Diversity:', default=0.8, validators=[validators.InputRequired(), validators.NumberRange(min=0.5, max=0.5,message='Diversity must be between 0.5 and 5.0')])
    words = IntegerField('Enter the number of word to generate: ',default=50, validators=[validators.InputRequired(), validators.NumberRange(min=10, max=100, message='NUmber should be between 10 and 100')])

    submit = SubmitField("Enter")


app =Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
    form = ReusableForm(request.form)

    if request.method == 'POST' and form.validate():
        seed = request.form['seed']
        diversity = float(request.form['diversity'])
        word = int(request.form)

        if seed == 'random':
            return render_template('random.html',input=generate_random_start (model = model, graph=graph,new_words=word, diversity=diversity))
        else: 
            return render_template('seeded.html', input=generate_from_seed(model=model, graph=graph,new_words=words, diversity=diversity))
    return render_template('index.html', form=form)

app.run(host="127.0.0.1", port=4555, debug=True)