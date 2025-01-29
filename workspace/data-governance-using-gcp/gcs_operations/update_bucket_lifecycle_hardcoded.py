from google.cloud.storage import Client


def update_bucket_policy(bucket_name, lifecycle_rules):
    gcs_client = Client()
    bucket = gcs_client.get_bucket(bucket_name)
    bucket.lifecycle_rules = lifecycle_rules
    bucket.patch()
    print(f"Lifecycle policy updated successfully for bucket: {bucket_name}")


bucket_name = "walmart_data_governance_1912985"

lifecycle_rules =  [
    {
      "action": {"type": "Delete"},
      "condition": {"age": 30}
    }
  ]

update_bucket_policy(bucket_name,lifecycle_rules)