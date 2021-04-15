import requests
from flask import Flask
from newsapi import NewsApiClient
import json

app = Flask(__name__)

@app.route('/')
def hello():
    
        # Init
    newsapi = NewsApiClient(api_key='966611677d694731833118dddf7bd7fc')

        # /v2/top-headlines
    forecast = newsapi.get_everything(q='forecast',
                                          sources='bbc-news,the-verge',
                                          domains='bbc.co.uk,techcrunch.com',
                                          from_param='2021-03-10',
                                          to='2021-12-11',
                                          language='en',
                                          sort_by='relevancy',
                                          page=1)
        # Find out what data type we are working with                                           
    print(type(forecast))
    
        # output buffer'
    output='{'
        # loop over the key and values in the dict
    for k, v in forecast.items():
        output = output + str(v) # add the value onto the buffer
    output = output + '}'
    json_format = json.dumps(output)
    jsnn = json.loads(json_format)
    print('type of output: ',type(jsnn))
    return jsnn # return buffer with data 
