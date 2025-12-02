#requests
#import requests
#response = requests.get("https://api.github.com")
#print(response.status_code)  # HTTP status code
#print(response.json())  # Response data

#numpy
#import numpy as np
#array = np.array([1, 2, 3])
#print(array + 2)  # Element-wise addition

#pandas
#import pandas as pd
#data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
#df = pd.DataFrame(data)
#print(df)

#Matplotlib
#import matplotlib.pyplot as plt
#plt.plot([1, 2, 3], [4, 5, 6])
#plt.show()

#Flask
#from flask import Flask
#app = Flask(__name__)
#@app.route("/")
#def home():
#   return "Hello, Flask!"
#app.run(debug=True)

#django
    #django-admin startproject myproject

#tensorflow
#import tensorflow as tf
#x = tf.constant([[1, 2], [3, 4]])
#print(x)

#pytest
   # test_example.py
#def test_add():
 #   assert 1 + 1 == 2
#  #run in command:pytest test_example.py

#pyttsx3
#import pyttsx3
# Initialize the text-to-speech engine
#engine = pyttsx3.init()
# Set properties (optional)
#engine.setProperty('rate', 150)  # Speed (default: 200)
#engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
# Say something
#engine.say("Hello! I am a text-to-speech conversion tool.")
#engine.say("You can use me to read any text aloud.")
# Wait for the speaking to finish
#engine.runAndWait()
# Change voice to female/male (optional)
#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[1].id)  # 0 for male, 1 for female
#engine.say("This is a female voice.")
#engine.runAndWait()

#Wikipedia
#import wikipedia

# Set language (default is English)
#wikipedia.set_lang("en")

# Search for a term
#search_results = wikipedia.search("Python programming")
#print("Search Results:", search_results)

# Get summary of a specific topic
#try:
    #summary = wikipedia.summary("Python programming", sentences=2)
    #print("Summary:", summary)
#except wikipedia.DisambiguationError as e:
    #print("Disambiguation Error:", e.options)

# Get detailed content of a page
#try:
    #page = wikipedia.page("Python programming")
    #print("Page Title:", page.title)
    #print("Page URL:", page.url)
    #print("Page Content (first 500 characters):", page.content[:500])
#except wikipedia.DisambiguationError as e:
    #print("Disambiguation Error:", e.options)
#except wikipedia.PageError as e:
    #print("Page Error:", e)
