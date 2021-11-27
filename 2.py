import boto3
import requests
import pandas
 
#Getting data from the URL
get_data = requests.get('http://web.cs.wpi.edu/~cs1004/a16/Resources/SacramentoRealEstateTransactions.csv')
data = get_data.content
with open('/home/ec2-user/sqft_data.csv','wb') as input_file:
    input_file.write(data_content)

#Perform same operation using pandas 
 

#Writing conetnt of the file to S3 bucket - (use s3_client.upload_file, also send sns notification)
s3 = boto3.resource('s3')
bucketname = 'sqft-data-bucket'

filetoupload = '/home/ec2-user/sqft_data.csv'
s3_filename = 'prod/data/sqft_data.csv'

s3.meta.client.upload_file(filetoupload,bucketname,s3_filename)