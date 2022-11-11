from azure.storage.blob import BlobClient
import time

blob = BlobClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=urls;AccountKey=pQakwxv1mG9495upsjqgk+wRHWWp6u9+kO9Yw+wIEHxK10jRZvYX0ZXuSYZM+SEpDIE6rvcR1PVy+ASt+rfDCQ==;EndpointSuffix=core.windows.net", container_name="urls", blob_name="urls")

global counter
counter = 0
while(True):
    file1 = open("urls3.txt", "r")
    Lines = file1.read()
    blob.upload_blob(Lines, overwrite=True)
    counter += 1
    print("Uploaded: No. " + str(counter))
    time.sleep(10)




