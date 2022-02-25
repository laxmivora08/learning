#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 07:14:36 2021

@author: stellapps
"""
import xlrd
import json
import sys
import gzip
import requests
file="/home/stellapps/my_workspace/actisens/L1_input.xls"
wb=xlrd.open_workbook(file)
sheet=wb.sheet_by_index(0)

rows=sheet.nrows

actisens_dict={"data":{
                       "id":"",
                       "type":"actitrak",
                       "meta":{"t":"","l":"","e":"","ei":"","ps":""},
                       "attributes":{"t":"","w":"","a":"","s":"","m":"","v":"","r":"","o":"","d":""}},
                "meta":{"version":1,"statusCode":200}}
actisens_dict["data"]["meta"]["e"]="actisen"
actisens_dict["data"]["meta"]["ps"]="activity"
j=0
for i in range(rows):
    if(i==0):
        pass
    else:
        actisens_dict["data"]["id"]=int(sheet.cell_value(i,j))
        actisens_dict["data"]["meta"]["t"]=sheet.cell_value(i,j+1)
        actisens_dict["data"]["meta"]["l"]=sheet.cell_value(i,j+2)
        actisens_dict["data"]["meta"]["ei"]=sheet.cell_value(i,j+3)
        actisens_dict["data"]["attributes"]["t"]=sheet.cell_value(i,j+1)
        actisens_dict["data"]["attributes"]["w"]=int(sheet.cell_value(i,j+4))
        actisens_dict["data"]["attributes"]["a"]=int(sheet.cell_value(i,j+5))
        actisens_dict["data"]["attributes"]["s"]=int(sheet.cell_value(i,j+6))
        actisens_dict["data"]["attributes"]["m"]=int(sheet.cell_value(i,j+7))
        actisens_dict["data"]["attributes"]["v"]=int(sheet.cell_value(i,j+8))
        actisens_dict["data"]["attributes"]["r"]=int(sheet.cell_value(i,j+9))
        actisens_dict["data"]["attributes"]["o"]=int(sheet.cell_value(i,j+10))
        actisens_dict["data"]["attributes"]["d"]=int(sheet.cell_value(i,j+11))
    json_object = json.dumps(actisens_dict)  
    in_json={"data":{"id":12,"type":"actitrak","meta":{"t":"\"2021-06-09T18:40:00Z\"","l":"6483c902-59da-4bff-bc3f-731e2cc66dcc","e":"actisen","ei":"37f2b714-b9dc-49b9-987d-3e540912033e","ps":"activity"},"attributes":{"t":"\"2021-06-09T18:40:00Z\"","w":320,"a":150,"s":800,"m":460,"v":810,"r":192,"o":0,"d":0}},"meta":{"version":1,"statusCode":200}}
#    print("json",in_json)
#    print("dict",json_object)
    arr=[]
    array_json=[]
    request_url="http://contrakv2data.smartmoo.com/eventscollector/events"
    array_json.append(json_object)
    arr.append(in_json)
    # json appended to array
    x=json.dumps(array_json)
    print(x)
    gz = gzip.compress(x.encode("utf-8"))
    len=sys.getsizeof(gz)
    
    
    x1=json.dumps(arr)
    print(x1)
    gz1 = gzip.compress(x1.encode("utf-8"))
    len=sys.getsizeof(gz1)
    
    
    header = {
                "Content-Encoding":"gzip",
                "Api-Key":"f4e2edac4bc56f132f96acc9695e0645",
                "Content-Length":str(len),
                "User-Agent":"6483c902-59da-4bff-bc3f-731e2cc66dcc", #L3 uuid
                 "Content-Type": "application/json"
                }
    trans_response = requests.request("POST", request_url, headers=header, data=gz)
    trans_response = requests.request("POST", request_url, headers=header, data=gz1)
    print(trans_response.text)
    if(trans_response.status_code== 200 ):
        print(" Transaction","successful")

