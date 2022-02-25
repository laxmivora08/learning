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
import zlib
from datetime import datetime
def orient(actisens_dict,in_data,meta,in_attributes):
    in_attributes["o"]=132
    in_data["meta"]=meta
    in_data["attributes"]=in_attributes
    actisens_dict["data"]=in_data
    print(actisens_dict)
    actisens = json.dumps(actisens_dict) #actisens is json format
    print(type(actisens))
    #  Take direct input json
    in_json='{"data": {"id": "1", "type": "actitrack", "meta": {"t": "/10-02-2021T22:57:11Z/", "l":"178d0da4-a5b6-416d-8fdc-64d11304b24d", "e": "actisen", "ei":"076d5c90-669e-4e0f-885f-ca4f14895204", "ps": "activity"}, "attributes": {"t": "/10-02-2021T22:57:11Z/", "w": 7200, "a": 123, "s": 200, "m": 12, "v": 190, "r": 192, "o": 132, "d": 0}}, "meta": {"version": 1, "statusCode": 200}}'

    #res_bytes = json.dumps(actisens_dict).encode('utf-8')
    array_json=[]
    array_json.append(in_json) # json appended to array
    print(type(array_json))
    x=json.dumps(array_json) #array to string
    print("x",type(x))
    #arr = (bytes(x,'utf-8'))
    #print(type(arr))
    return x
def time():
    dt=datetime.now()
    dt_string = dt.strftime("%d-%m-%YT%H:%M:%S")
    dt_string="/"+(dt_string)
    dt_string=dt_string+"Z/"
    #print(dt_string)
    return dt_string
def request(l3_uuid,request_url,x):
#    with gzip.open("zen.gz", "wb") as f:
#        f.write(x)
    #gz=zlib.compress(x,'utf-8')
    y=x.encode("utf-8")
    gz=zlib.compress(y)
    print(type(gz))
    len=sys.getsizeof(gz)
    print(sys.getsizeof(gz))
    header = {
                'Content-Encoding':'gzip',
                'Api-Key':'f4e2edac4bc56f132f96acc9695e0645',
                'Content-Length':str(len),
                'User-Agent':'178d0da4-a5b6-416d-8fdc-64d11304b24d'
                }
    trans_response = requests.request("POST", request_url, headers=header, data=gz)
    print(trans_response)
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
    print(actisens_dict)
    #input=print("Which packet you  want to create")
    x=orient(actisens_dict,in_data,meta,in_attributes)
    request(l3_uuid,request_url,x)
if __name__== '__main__':
    main_func()

    
