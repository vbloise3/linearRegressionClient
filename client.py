import os
import io
import boto3
import json
import csv

ENDPOINT_NAME = 'bikeshare-sagemaker-regression-v1'
runtime= boto3.client('runtime.sagemaker')

# Convert categorical date field
observation = "3,2011-01-03,1,0,1,0,1,1,1,0.196364,0.189405,0.437273,0.248309,120,1229"
observation = observation.replace("-","")

data = {"data":observation}
actual = {"data":"1349"}
payload = data['data']
# print(payload)

response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                    ContentType='text/csv',
                                    Body=payload)
# print(response)

result = json.loads(response['Body'].read().decode())
print('prediction: ', result['predictions'][0]['score'], '\t\tactual: ', str(actual['data']))
