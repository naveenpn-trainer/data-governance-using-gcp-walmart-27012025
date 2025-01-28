from google.cloud.storage import Client
bucket_name = "walmart_data_governance_002"
client = Client()
bucket = client.bucket(bucket_name=bucket_name)
bucket.delete()