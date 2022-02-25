#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:18:04 2021

@author: laxmi vora
"""
import requests
import pandas as pd
import sys
import uuid
import json
import gzip
from datetime import datetime


def orient(actisens_dict,in_data,meta,in_attributes):
    in_attributes["o"]=132
    in_data["meta"]=meta
    in_data["attributes"]=in_attributes
    actisens_dict["data"]=in_data
    #print(actisens_dict)
    actisens = json.dumps(actisens_dict) #actisens is json format
    #print(type(actisens))
    #  Take direct input json
#    with open(path1) as fp:
#        data=json.load(fp)
    in_json={"data":{"id":1,"type":"actitrak","meta":{"t":"\"2021-2-17T11:30:00Z\"","l":"178d0da4-a5b6-416d-8fdc-64d11304b24d","e":"actisen","ei":"b632d77e-9d4f-4396-852f-2fbe2e1a1190","ps":"activity"},"attributes":{"t":"\"2021-2-17T11:30:00Z\"","w":120,"a":0,"s":120,"m":0,"v":762,"r":192,"o":0,"d":0}},"meta":{"version":1,"statusCode":200}}

    #res_bytes = json.dumps(actisens_dict).encode('utf-8')
    print(type(in_json))
    array_json=[]
    array_json.append(in_json) # json appended to array

    x=json.dumps(array_json) #array to string
    return x

def time():
    dt=datetime.now()
    dt_string = dt.strftime("%d-%m-%YT%H:%M:%S")
    dt_string="/"+(dt_string)
    dt_string=dt_string+"Z/"
    return dt_string
    
def request(l3_uuid,request_url,x):
    gz = gzip.compress(x.encode('utf-8'))
    len=sys.getsizeof(gz)

    header = {
                'Content-Encoding':'gzip',
                'Api-Key':'f4e2edac4bc56f132f96acc9695e0645',
                'Content-Length':str(len),
                'User-Agent':'178d0da4-a5b6-416d-8fdc-64d11304b24d', #L3
                 'Content-Type': 'application/json'
                }
    trans_response = requests.request("POST", request_url, headers=header, data=gz)
    print(trans_response.text)
    if(trans_response.status_code== 200 ):
        print(" Transaction","successful")

def valid_asm(actisens_dict,in_data,in_meta,in_attributes,acti_meta):
    pass


def main_func():
    l3_uuid=str(uuid.uuid4())
    request_url='http://contrakv2data.smartmoo.com/eventscollector/events'
    #create dictionary for taking varied ASM input or o,d inputs
    actisens_dict={"data":"","meta":""}
    a={"version":"","statusCode":""}
    a["version"]=1
    a["statusCode"]=200
    actisens_dict["meta"]=a
    in_data={"id":"1","type":"","meta":"","attributes":""}
    in_data['type']="actitrack"
    meta={"t":"","l":"","e":"","ei":"","ps":""}
    in_attributes= {"t": "", "w": "","a": "","s": "","m": "","v": "","r": "","o": "","d": ""}
    t=time()
    meta['t']=t
    meta['l']=l3_uuid
    meta['e']="actisen"
    meta['ps']="activity"
    in_attributes['t']=t
    in_attributes['w']=in_attributes['s']=7200
    in_attributes['a']=in_attributes['m']=in_attributes['v']=in_attributes['r']=in_attributes['o']=in_attributes['d']=0 
    #print(actisens_dict)
    #input=print("Which packet you  want to create")
    x=orient(actisens_dict,in_data,meta,in_attributes)
    request(l3_uuid,request_url,x)
       
if __name__== '__main__':
    main_func()

    
