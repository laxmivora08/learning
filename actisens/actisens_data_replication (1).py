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
import os

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
    #    cwd=os.getcwd()
#    path1=os.path.join(cwd+'/l1.json')
#    with open(path1) as fp:
#        data=json.load(fp) 
#    #res_bytes = json.dumps(actisens_dict).encode('utf-8')
#    print("data",type(data6))
#    in_json=json.dumps(data)
    
    in_json={"data":{"id":220,"type":"actitrak","meta":{"t":"\"2022-02-22T18:66:50Z\"","l":"6483c902-59da-4bff-bc3f-731e2cc66dcc","e":"actisen","ei":"0feb100d-bfdc-460c-96d5-664634bc7fef","ps":"activity"},"attributes":{"t":"\"2022-02-22T18:66:50Z\"","w":300,"a":2,"s":257,"m":1,"v":907,"r":192,"o":0,"d":0,"tr":17}},"meta":{"version":1,"statusCode":200}}
     
    #res_bytes = json.dumps(actisens_dict).encode('utf-8')

    print(type(in_json))
    array_json=[]
    array_json.append(in_json) # json appended to array

    x=json.dumps(array_json) #array to string
    return x
#def ams_zero():
#    for i in range(10):
#        
#def time():
#    dt=datetime.now()
#    dt_string = dt.strftime("%d-%m-%YT%H:%M:%S")
#    dt_string="/"+(dt_string)
#    dt_string=dt_string+"Z/"
#    return dt_string
def request(l3_uuid,request_url,x):
    gz = gzip.compress(x.encode('utf-8'))
    len=sys.getsizeof(gz)

    header = {
                'Content-Encoding':'gzip',
                'Api-Key':'f4e2edac4bc56f132f96acc9695e0645',
                'Content-Length':str(len),
                'User-Agent':'6483c902-59da-4bff-bc3f-731e2cc66dcc', #L3 uuid
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
#    t=time()
#    meta['t']=t
#    meta['l']=l3_uuid
#    meta['e']="actisen"
#    meta['ps']="activity"
#    in_attributes['t']=t
#    in_attributes['w']=in_attributes['s']=7200
#    in_attributes['a']=in_attributes['m']=in_attributes['v']=in_attributes['r']=in_attributes['o']=in_attributes['d']=0 
    #print(actisens_dict)
    #input=print("Which packet you  want to create")
    x=orient(actisens_dict,in_data,meta,in_attributes)
    request(l3_uuid,request_url,x)
       
if __name__== '__main__':
    main_func()

    
