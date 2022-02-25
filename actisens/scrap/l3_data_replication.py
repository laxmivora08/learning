#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 13:27:58 2021

@author: laxmi vora
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:18:04 2021

@author: laxmi vora
"""
import requests

import pandas as pd
import uuid
import json
import gzip
import sys
import os
from datetime import datetime
#def not_live_l1():

def orient(actisens_dict,in_data,meta,in_attributes):
    in_attributes["o"]=132
    in_data["meta"]=meta
    in_data["attributes"]=in_attributes
    actisens_dict["data"]=in_data
    #print(actisens_dict)
    actisens = json.dumps(actisens_dict) #actisens is json format
    #print(type(actisens))
    cwd=os.getcwd()
    path1=os.path.join(cwd+'/l3.json')
#    with open(path1) as fp:
#        data=json.load(fp) 
#    #res_bytes = json.dumps(actisens_dict).encode('utf-8')
#    print("data",type(data))
    #j_son=json.dumps(data)
    j_son={"data":{"type":"actitrak",
                   "meta":{"t":"2021-02-17T14:40:19Z","l":"0,1","e":"Gateway","ei":"178d0da4-a5b6-416d-8fdc-64d11304b24d","ps":"GwInfo"},
                    "attributes":{"sysInfo":{
                                    "fv":" 3.2",
                                    "ip":"fd00:8000::628:1",
                                    "ut":"10:40",
                                    "sp":"airtel",
                                    "sn":"89914509009594485958",
                                    "ci":{
                                            "mcc":"404",
                                            "mnc":"45",
                                            "lac":"0470",
                                            "cid":"00E0F14"
                                            }
                                    }, "events": [{"t":"22021-02-17T04:38:19Z","sq":"23","bv":"3.10"},{"t":"2021-02-17T06:38:19Z","sq":"22","bv":"4.10"},      {"t":"2021-02-17T08:38:19Z","sq":"21","bv":"4.10"},{"t":"2021-02-17T10:38:19Z","sq":"20","bv":"4.10"}],
                                    "devicesInfo":{
                                            "dc":3,
                                            "di": [{"uuid":"18309e6e-cad4-46f1-b68e-553d75f105ff" ,"ip":"fd00:8000::123:3"},
                                                   {"uuid":"b632d77e-9d4f-4396-852f-2fbe2e1a1190","ip":"fd00:8000::123:2"},
                                                   {"uuid":"076d5c90-669e-4e0f-885f-ca4f14895204","ip":"fd00:8000::123:1"}]}}},
            "meta": {
                    "version":"0.1",
                    "statusCode":200
                    }
            }
    print("j_son",type(j_son))
    array_json=[]
    array_json.append(j_son)
    print(type(array_json))
    x=json.dumps(array_json)
#    print(type(x))
    return x

def time():
    dt=datetime.now()
    dt_string = dt.strftime("%d-%m-%YT%H:%M:%S")
    dt_string="/"+(dt_string)
    dt_string=dt_string+"Z/"
    #print(dt_string)
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
    print(trans_response)
    print(trans_response.text)
    if(trans_response.status_code== 200 ):
        print(" Transaction","successful")
def valid_asm(actisens_dict,in_data,in_meta,in_attributes,acti_meta):
    pass
def main_func():
    l3_uuid=str(uuid.uuid4())
    request_url='http://contrakv2data.smartmoo.com/eventscollector/events'
    actisens_dict={"data":"","meta":""}
    a={"version":"","statusCode":""}
    a["version"]=1
    a["statusCode"]=200
    actisens_dict["meta"]=a
    in_data={"type":"","meta":"","attributes":""}
    in_data['type']="actitrack"
    in_meta={"t":"",'l':"","e":"","ei":"","ps":""}
    sysInfo={"fv":" ","ip":"","ut":"","sp":"","sn":"","ci":""}
    ci:{
           "mcc":"",
           "mnc":"",
           "lac":"",
           "cid":""
         }
    events: []
    event_data={"t":"2021-02-03T14:00:00Z","sq":"23","bv":"4.10"}
    device_info={"dc":"","di":""}
    di=[]
    di_data={"uuid":"","ip":""}
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
    #input=print("Which packet you  want to create")
    x=orient(actisens_dict,in_data,meta,in_attributes)
    request(l3_uuid,request_url,x)
if __name__== '__main__':
    main_func()

    
