from flask import Flask, jsonify, render_template, request
import os,yaml,datetime

bio=Flask(__name__)

def openyml(filename):
    stuff=open(filename,'r')
    datadictionary=yaml.load(stuff)
    return datadictionary

@bio.route("/")
def home():
    filename='links.yaml'
    data=openyml(filename)
    links=[]
    for k,v in data.items():
        if k=='picture':
            picture=v
        if k=='name':
            name=v
        if k=='shortbio':
            shortbio=v
        if k=='links':
            links=v
    date=datetime.datetime.now()
    date=str(date)
    return render_template('layout.html',picture=picture,name=name,shortbio=shortbio,links=links,date=date)

if __name__=="__main__":
    bio.run(host="0.0.0.0",debug=False)