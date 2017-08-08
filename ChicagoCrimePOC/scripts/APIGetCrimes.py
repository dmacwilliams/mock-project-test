import os
import os.path
import sys
import requests
import datetime
import json
import csv
import datetime
import time
import os



#parameterized start date
current_date=datetime.datetime.now()
current_date_iso=datetime.datetime.now().isoformat()
#for testing only
#current_date=current_date.replace(month=3)

print ("Current date = %s" % current_date )

if current_date.month==1:
    start_date=str(current_date.year-1)+'-'+'12'+'-'+'01T00:00:00.000'
    #output_dict = [x for x in input_dict if datetime.datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f') > datetime.datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S.%f')]
else:
    start_date=str(current_date.year)+'-'+str(current_date.month-1).zfill(2)+'-'+'01T00:00:00.000'
    #output_dict = [x for x in input_dict if datetime.datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f') > datetime.datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S.%f')]

print ("Start date = %s" % start_date )


api_scope='https://data.cityofchicago.org/resource/6zsd-86xi.json'
app_token='7bmu6mXNvdH6Em4OqX2SAfvBX'
#correct, below
url=api_scope+"?"+'$$app_token='+app_token+"&"+'$limit=100000'+"&$"+"where=date%20between%20%27"+str(start_date)+"%27%20and%20%27"+str(current_date_iso)+'%27'
#testing only
#url='https://data.cityofchicago.org/resource/6zsd-86xi.json?$$app_token=7bmu6mXNvdH6Em4OqX2SAfvBX&$limit=50000&$where=date%20between%20%272015-12-01T00:00:00.000%27%20and%20%272016-01-19T13:44:45.400000%27'


s=requests.Session()
r=s.get(url, stream=True, verify=False)

# Convert request response string into json
j_str = json.dumps(r.json())
# Transform json input to python objects
input_dict = json.loads(j_str)
# Filter python objects with list comprehensions
#output_dict = [x for x in input_dict if datetime.datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f') > datetime.datetime.strptime('2016-05-01T00:00:00.000', '%Y-%m-%dT%H:%M:%S.%f')]


output_dict=input_dict

output=output_dict
#keys = output[0].keys()
keys = ['y_coordinate','year','domestic','case_number','id','description','district','arrest','community_area','latitude','primary_type',
'beat','date','ward','iucr','longitude','location_description','x_coordinate','updated_on','fbi_code','block']

with open('C:\ChicagoCrimeETL\inbound\crimes.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys,extrasaction='ignore',lineterminator = '\n')
    dict_writer.writeheader()
    dict_writer.writerows(output)
    
