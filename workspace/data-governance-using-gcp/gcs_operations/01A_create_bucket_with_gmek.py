from google.cloud.storage import Client
bucket_name = "walmart_data_governance_002"
client = Client()
bucket = client.bucket(bucket_name=bucket_name)
new_bucket = client.create_bucket(bucket)
print(f"Bucket {bucket_name} created successsfully")