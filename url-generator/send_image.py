from azure.storage.blob import BlobClient
import time

blob = BlobClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=urls;AccountKey=pQakwxv1mG9495upsjqgk+wRHWWp6u9+kO9Yw+wIEHxK10jRZvYX0ZXuSYZM+SEpDIE6rvcR1PVy+ASt+rfDCQ==;EndpointSuffix=core.windows.net", container_name="images", blob_name="images")
folder = './greylist_screenshots'
blob.upload_blob(folder, overwrite=True)



