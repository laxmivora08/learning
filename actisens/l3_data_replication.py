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

def payload_info():
    cwd=os.getcwd()
    path1=os.path.join(cwd+'/l3.json')
#    with open(path1) as fp:
#        data=json.load(fp) 
#    #res_bytes = json.dumps(actisens_dict).encode('utf-8')
#    print("data",type(data))
    #j_son=json.dumps(data)
    j_son={"data":{"type":"actitrak",
                   "meta":{"t":"2022-01-26T16:40:00Z","l":"0,1","e":"Gateway","ei":"6483c902-59da-4bff-bc3f-731e2cc66dcc","ps":"GwInfo"},
                    "attributes":{"sysInfo":{
                                    "fv":" 1.3",
                                    "ip":"fd00:8000::65b:1",
                                    "ut":"2021-10-26T02:05:10Z",
                                    "sp":"airtel",
                                    "sn":"89914509009594485958", 
                                    "ci":{
                                            "mcc":"404",
                                            "mnc":"45",
                                            "lac":"0470",
                                            "cid":"00E0F14"
                                            }
                                    }, "events": [{"t":"2022-01-26T03:38:19Z","sq":"24","bv":"1.10","cs":1},{"t":"2022-01-26T06:38:19Z","sq":"22","bv":"4.60","cs":1},{"t":"2022-01-26T08:38:19Z","sq":"21","bv":"4.10","cs":1},{"t":"2022-01-26T10:38:19Z","sq":"20","bv":"4.10","cs":1}],
                                    "devicesInfo":{
                                            "dc":3,
                                            "di": [{"uuid":"fc922720-3cdb-4a3f-8566-a05429639d8a" ,"ip":"fd00:8000::618:3"},
                                                   {"uuid":"0feb100d-bfdc-460c-96d5-664634bc7fef","ip":"fd00:8000::618:2"},
                                                   {"uuid":"076d5c90-669e-4e0f-885f-ca4f14895204","ip":"fd00:8000::618:1"}]}}},
            "meta": {
                    "version":"0.1",
                    "statusCode":200
                    }
            }
    #print("j_son",type(j_son))
    array_json=[]
    array_json.append(j_son)
    print(type(array_json))
    x=json.dumps(array_json)
    print(x)
#    print(type(x))
    return x

def time():
    dt=datetime.now()
    dt_string = dt.strftime("%d-%m-%YT%H:%M:%S")
    dt_string="/"+(dt_string)
    dt_string=dt_string+"Z/"
    #print(dt_string)
    return dt_string
def request(request_url,x):
    gz = gzip.compress(x.encode('utf-8'))
    print(gz)
    len=sys.getsizeof(gz)
    header = {
                'Content-Encoding':'gzip',
                'Api-Key':'f4e2edac4bc56f132f96acc9695e0645',
                'Content-Length':str(len),
                'User-Agent':'6483c902-59da-4bff-bc3f-731e2cc66dcc', #L3
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
    request_url='http://contrakv2data.smartmoo.com/eventscollector/events'
    #input=print("Which packet you  want to create")
    x=payload_info()
    request(request_url,x)
if __name__== '__main__':
    main_func()

    
