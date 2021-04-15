import requests
from flask import Flask, request, jsonify
import xmlrpc.client
from newsapi import NewsApiClient
import http.client
import logging
from datetime import date, datetime
from gql import gql, Client
from python_graphql_client import GraphqlClient
from gql.transport.aiohttp import AIOHTTPTransport
import hprose
import json


app = Flask(__name__)

@app.route('/')
def hello_world():
    date = datetime.now()
    logs = open('calls.log','a')
    log_value = ''+str(date)+'-'+ request.path + '\n'
    logs.write(log_value)
    return 'Hello World!'

@app.route('/justweather')
def just_weather():
    date = datetime.now()
    logs = open('calls.log','a')
    log_value = ''+str(date)+'-'+ request.path + '\n'
    logs.write(log_value)
	
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
    json_format = jsonify(forecast)
    return json_format # return buffer with data 


@app.route('/getTemp')
def callClient():
    date = datetime.now()
    logs = open('calls.log','a')
    log_value = ''+str(date)+'-'+ request.path + '\n'
    logs.write(log_value)
    # calling the RPC server
    with xmlrpc.client.ServerProxy("http://localhost:8001/") as proxy:
        res = proxy.get_temp(3)
        print(res)
    return "Temperature :" + res
    
@app.route('/updates')
def justupdates_call():
    date = datetime.now()
    logs = open('calls.log','a')
    log_value = ''+str(date)+'-'+ request.path + '\n'
    logs.write(log_value)
	
	
    f = open('updates.txt', 'r')
    x = f.readlines()
    output = '{'

    print(type(x))
    print(x)

    for item in x:
    #   "line1": "item1",
        output = output + '"line": "'+ item + '",'
    f.close()

    # remove the last trailing comma.
    output = output[:-1]

    output = output + '}'
    return output

i
@app.route('/insertStudent')
def insert_record():
    firstname = request.args.get('firstname')
    lastname = request.args.get('secondname')
    stuNum= request.args.get('studentNumber')

    insert = open('students.log', 'a')
    date = datetime.now()
    insert_val =  ''+str(date)+ '-' + firstname+ '-' + lastname + '-' + stuNum +'\n'
    insert.write(insert_val) 
	
    date = datetime.now()
    logs = open('calls.log','a')
    log_value = ''+str(date)+'-'+ request.path + '\n'
    logs.write(log_value)
    
    insert.close()

    return "NAME :" + firstname + ' ' + lastname + ' STUDENT NUMBER: ' + stuNum + ' DATE: ' + str(date)


@app.route('/ping')
def ping():
    
    date = datetime.now()
    logs = open('calls.log', 'a')
    log_value =  ''+str(date)+ '-' + request.path +'\n'
    logs.write(log_value)

    return 'pong'

@app.route('/students')
def graph_ql():
    date = datetime.now()
    logs = open('calls.log', 'a')
    log_value =  ''+str(date)+ '-' + request.path +'\n'
    logs.write(log_value)

    # Select your transport with a defined url endpoint
    transport = AIOHTTPTransport(url="http://localhost:4000/graphql")
    
    # Create a GraphQL client using the defined transport
    client = Client(transport=transport, fetch_schema_from_transport=True)

    stId = request.args.get('studentID')

    # Provide a GraphQL query
    query = gql(
        """
       query findStudent($studentid: String)
       { studentQueryById(studentid: $studentid) {
          studentid
          studentname
          studentdob
        }

    }
    """
    )

    variables = {"studentid": stId}
    
    # Execute the query on the transport
    result = client.execute(query, variables)
    return (result)
    
	
@app.route('/ip')
def ip_address():
	date = datetime.now()
	logs = open('calls.log', 'a')
	log_value =  ''+str(date)+ '-' + request.path +'\n'
	logs.write(log_value)
	
	client = hprose.HttpClient("http://127.0.0.1:8080/");
	
	return client.getIp()
	
	
	
	
