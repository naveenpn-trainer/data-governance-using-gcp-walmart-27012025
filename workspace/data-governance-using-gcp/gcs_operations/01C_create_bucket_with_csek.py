from google.cloud.storage import Client
import os
def generate_encryption_keys():
    return os.urandom(32)

def upload_object_with_csek(bucket_name, encryption_key, file_path, blob_name):
    client = Client()
    bucket = client.bucket(bucket_name)
    blob =bucket.blob(blob_name=blob_name, encryption_key=encryption_key)
    blob.upload_from_filename(file_path)
    print("Successfully uploaded")
    
    
bucket_name = "walmart_datagovernance_cmek_1912985"
encryption_keys = generate_encryption_keys()
upload_object_with_csek(bucket_name=bucket_name,encryption_key=encryption_keys,file_path="sample_dataset.dat", blob_name="sample.dat")

