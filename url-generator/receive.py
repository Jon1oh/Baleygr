from azure.storage.blob import BlobClient
import csv

blob = BlobClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=urls;AccountKey=pQakwxv1mG9495upsjqgk+wRHWWp6u9+kO9Yw+wIEHxK10jRZvYX0ZXuSYZM+SEpDIE6rvcR1PVy+ASt+rfDCQ==;EndpointSuffix=core.windows.net", container_name="urls", blob_name="urls")


data = blob.download_blob()

dataread = data.readall().decode()

finale = dataread.split("\n")

with open("urldownload.csv",  "w") as csv_file:
    wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    for word in finale:
        wr.writerow([word])
    





 
