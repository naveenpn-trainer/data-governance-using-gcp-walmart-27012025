from google.cloud.storage import Client
client = Client()

bucket_name = "walmart_datagovernance_cmek_85"
bucket = client.bucket(bucket_name)
kms_key_name = "projects/upgradlabs-1735976404499/locations/us-east1/keyRings/my-custom-keyring/cryptoKeys/key01"
bucket.default_kms_key_name = kms_key_name


bucket.create(location="us-east1")
print(f"Bucket {bucket_name} created successfully")
