from azure.storage.blob import BlobClient
import time

blob = BlobClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=urls;AccountKey=pQakwxv1mG9495upsjqgk+wRHWWp6u9+kO9Yw+wIEHxK10jRZvYX0ZXuSYZM+SEpDIE6rvcR1PVy+ASt+rfDCQ==;EndpointSuffix=core.windows.net", container_name="urls", blob_name="urls")

""" f = open("url-generator/urls3.txt", "rb").read()
count = 0
print("Using readlines()")
Lines = f
print(Lines)
for line in Lines:
    count += 1
    blob.upload_blob(line)
    print("Line{}: {}".format(count, line.strip())) """

global counter
counter = 0
while(True):
    file1 = open("urls3.txt", "r")
    Lines = file1.read()
    blob.upload_blob(Lines, overwrite=True)
    counter += 1
    print("Uploaded: No. " + str(counter))
    time.sleep(10)




