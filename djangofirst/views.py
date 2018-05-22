from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json
import time
import urllib.request  as urllib2
import requests
import mysql.connector
config = {
  'user': 'root',
  'password': 'qwerty',
  'host': 'localhost',
  'port': '3306',
  'database': 'user',
  'raise_on_warnings': True,
}


def index(request):
    return render(request, 'index.html', {})

@csrf_exempt
def listuser(request):
    js = json.loads(request.body.decode('utf-8'))
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(buffered=True)
    query = """SELECT name, surname FROM user"""
    cursor.execute(query)
    d = cursor.fetchall()
    data = {'list': []}
    i = 0
    name = ""
    surname = ""
    for row in d:
        for x in row:

            if i == 0:
                i = i + 1
                name = x
            else:
                if i == 1:
                    surname = name + " " + x
                    data['list'].append("'" + surname + "'")
                    i = 0
    print(data)
    cursor.close()
    cnx.close()
    mydata = {'result': "valid" ,'data': data}
    return HttpResponse(json.dumps(mydata), content_type="application/json")

@csrf_exempt
def readj(request):
    js = json.loads(request.body.decode('utf-8'))
    suname = js['surname']
    name = js['name']
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(buffered=True)
    query = """SELECT surname FROM user"""
    cursor.execute(query)
    data=cursor.fetchall()
    b="true";
    for item in data:
        x=item.__str__()
        if(x=="('"+suname+"',)"):
            b="false"

    if b=="true":
        add_user = "INSERT INTO user (name, surname) VALUES (%s, %s)"
        data_user = (name, suname)
        cursor.execute(add_user, data_user)
        cnx.commit()
        cursor.close()
        cnx.close()
        mydata = {'result': "valid"}
        return HttpResponse(json.dumps(mydata), content_type="application/json")
    else:
        mydata = {'result': "notValid"}
        return HttpResponse(json.dumps(mydata), content_type="application/json")
        cursor.close()
        cnx.close()

@csrf_exempt
def createJsonList(request):
    js = json.loads(request.body.decode('utf-8'))
    value = js['value']
    list =selectWords(value,selectAll())
    mydata = {'result': list}
    return HttpResponse(json.dumps(mydata), content_type="application/json")



@csrf_exempt
def prova(request):

    method()
    return render(request, 'prova.html', {})


def method():
    mydata = {'id': '4.0', 'content': "mezzosangue"}
    print("asd")
    url = 'http://192.168.98.227:8080/Orchestrator/rest/greeting'
    r=requests.post("http://192.168.98.227:8080/Orchestrator/rest/greeting", json={'id': '4', 'content': "alfino5"})
    jsons = json.loads(r.text)
    print(jsons['id'])
    i=0
    id=100
    while True:
        time.sleep(50)
        i=i+1
        data="richiesta "
        datas= data + str(i)
        print(datas)
        r = requests.post("http://192.168.98.227:8080/Orchestrator/rest/greeting",
                          json={'id': (id/2), 'content': str(id)})

        jsons = json.loads(r.text)
        id= jsons['id']
        print(jsons['id'])
        if(i>5000):
            break

def selectAll():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(buffered=True)
    query = """SELECT name, surname FROM user"""
    cursor.execute(query)
    d = cursor.fetchall()
    data =  []
    i = 0
    name = ""
    surname = ""
    for row in d:
        for x in row:

            if i == 0:
                i = i + 1
                name = x
            else:
                if i == 1:
                    surname = name + " " + x
                    data.append("'" + surname + "'")
                    i = 0
    cursor.close()
    cnx.close()
    return data


def selectWords(value, listSql):
    i = 0
    data = []

    for i in range(len(listSql)):
        word = listSql[i]
        x=word.count(value)
        if(x>0):
             data.append(word)
        i = i+1;
    print(data)
    return data

