from flask import Flask, request, jsonify
from docx import Document
from docx2pdf import convert
from simple_colors import *
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'This is my first API call!'

@app.route('/post', methods=["POST"])
def testpost():
      
    doc = Document('investordoc.docx')
    f = open('replacementData.json')
    
    # returns JSON object as 
    # a dictionary
    replacements = request.json
    for paragraph in doc.paragraphs:
        for key in replacements:
            paragraph.text = paragraph.text.replace(key, replacements[key])

    doc.save('abcdefg.docx')
    convert('abcdefg.docx', 'output.pdf')
    return "converted"