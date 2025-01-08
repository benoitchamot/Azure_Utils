import pandas as pd
from azure.storage.blob import BlobServiceClient

def storage_list_blobs(storage_account, storage_container, storage_key):
    # Construct account URL
    account_url = f"https://{storage_account}.blob.core.windows.net/"

    # Create a BlobServiceClient
    blob_service_client = BlobServiceClient(account_url=account_url, credential=storage_key)

    # Get a ContainerClient
    container_client = blob_service_client.get_container_client(storage_container)

    blobs = []

    for blob in container_client.list_blobs():
        blobs.append({
            'name': blob.name,
            'size': int(round(blob.size/1024, 0)) # size in kB
        })

    return pd.DataFrame(blobs)