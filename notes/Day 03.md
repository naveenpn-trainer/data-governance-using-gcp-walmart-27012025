# Data Lifecycle Management

> DLM is the process of managing data througout its lifecycle, from creation to deletion to ensure data is effectively and securely handled at every stage

## gcloud Command

**Describe Bucket**

```
gcloud storage buckets describe gs://walmart_data_governance_1912985

gcloud storage buckets describe gs://walmart_data_governance_1912985 --format="json(lifecycle_config)"
```

**Update bucket with lifecyle policy**

```
gcloud storage buckets update gs://walmart_data_governance_1912985 --lifecycle-file=life_cycle_rule_001.json
```

**Remove Lifecycle rules from a bucket**

```
gcloud storage buckets update gs://walmart_data_governance_1912985 --clear-lifecycle
```



# Data Encryption and Key Management

> Data Encryption is the process of converting data into coded form to prevent unauthorized access. 

GCP offers multiple layers of encryption

1. Google Managed Encryption Keys (GMEK) (Default for most services)
2. Customer Managed Encryption Keys (CMEK)
   - Using KMS (Key Managedment Service)
3. Customer Supplied Encryption Keys (CSEK)
   - Customer provide their own encryption keys

## gcloud Commands for CMEK

**Create CMEK Bucket**

```
gcloud storage buckets create gs://[BUCKET_NAME] --location=[LOCATION_NAME] --default-encryption-key=projects/[PROJECT_ID]/locations/[LOCATION]/keyRings/[KEYRING_NAME]/cryptoKeys/[KEY_NAME]
```



```
gcloud storage buckets create gs://cmek-bucket-19121985 --location=us-east1 --default-encryption-key=projects/upgradlabs-1735976404499/locations/us-east1/keyRings/my-custom-keyring/cryptoKeys/key01
```

**Upload files without encryption keys**

```
gcloud storage cp sample_dataset.dat gs://cmek-bucket-191285
```

**Upload files with encryption keys**

```
gcloud storage cp sample_dataset.dat gs://cmek-bucket-191285 --encryption-key=projects/upgradlabs-1735976404499/locations/us-east1/keyRings/my-custom-keyring/cryptoKeys/key01
```

**View the file**

```
gcloud storage cat gs://cmek-bucket-191285/sample_dataset.dat
```

**View the file after disabling the key**

```
ERROR: (gcloud.storage.cat) HTTPError 400: Cloud KMS key is disabled, destroyed, or scheduled to be destroyed.
- '@type': type.googleapis.com/google.rpc.PreconditionFailure
  violations:
  - description: ''
    subject: ''
    type: KEY_DISABLED
```



## gcloud Commands for CSEK

```
gcloud storage buckets create gs://csek-bucket-191285 --location=us-east1
```

**Generate Base64 encryption key**

```
openssl rand -base64 32
```

**Copy file using encryption key**

```
gcloud storage cp sample_dataset.dat gs://csek-bucket-191285 --encryption-key=/hUWY4HBGrki9z2l2ty4guLQQnDvGG2o3wR7Vm8kV9Y=
```

**View the file without encryption key**

```
gcloud storage cat gs://csek-bucket-191285/sample_dataset.dat

ERROR: (gcloud.storage.cat) Missing decryption key with SHA256 hash DC7E/LA+yR/boC/a2Ae470USRKB0PtdHgR87S/INoz4=. No decryption key matches object gs://csek-bucket-191285/sample_dataset.dat#1738174895418931.
```

**View the file with encryption key**

```
gcloud storage cat gs://csek-bucket-191285/sample_dataset.dat --encryption-key=/hUWY4HBGrki9z2l2ty4guLQQnDvGG2o3wR7Vm8kV9Y=
```



# Data Loss Prevention (DLP)

> Google Cloud's Data Loss Prevention is a fully managed service designed to help organization discover, classify and protect sensitive data.

* DLP can be applied GCS , Big Query

## Key Features of DLP API

1. Sensitive Data Discovery
   - Automatically scans for sensitive data such as PII, PCI, PHI
   - Supports scans in GCS, BigQuery and Datastore
2. Customizable Data Classification
   - We can define custom detectors using regex
   - Built-in detectors for over 180+ 
3. Data Masking and Transformation
   - De-identify sensitive data using 









