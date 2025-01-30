import time

from google.cloud import dlp_v2
import json

def load_and_fill_config(config_file, replacements):
    with open(config_file, "r") as file:
        config = json.load(file)

    # Replace placeholders in the config
    config_str = json.dumps(config)  
    for key, value in replacements.items():
        config_str = config_str.replace(f"{{{{{key}}}}}", value)  
    
    # Convert back to a dictionary
    return json.loads(config_str)  


def create_dlp_inspect_job_with_template(project_id, inspect_job_config):
    # Initialize the DLP client
    dlp = dlp_v2.DlpServiceClient()

    # Define the parent project location
    parent = f"projects/{project_id}/locations/global"

    # Create the DLP job
    response = dlp.create_dlp_job(parent=parent, inspect_job=inspect_job_config)

    print(f"DLP Inspect Job created successfully: {response.name}")
    return response.name

def poll_for_job_completion(job_name):
    dlp = dlp_v2.DlpServiceClient()

    # Poll for the job status
    print("Polling for job status...")
    job_status = None
    while job_status != "DONE":
        try:
            time.sleep(10)  # Wait 10 seconds before checking status
            job = dlp.get_dlp_job(name=job_name)
            job_status = job.state.name
            if job_status == "RUNNING":
                print("Job is still running...")
            elif job_status == "FAILED":
                print("Job has failed.")
                print(f"Error Details: {job.details}")
                break
        except Exception as e:
            print(f"Error while checking job status: {e}")
            break

    if job_status == "DONE":
        print(f"Job {job_name} completed successfully with status: {job_status}")
    elif job_status != "DONE":
        print(f"Job {job_name} did not complete successfully.")

# Usage: Load inspect job configuration, fill placeholders, and create the inspect job
if __name__ == "__main__":
    CONFIG_FILE = "inspect_job_config.json"  # Path to the JSON file
    PROJECT_ID = "upgradlabs-1736758861064"
    GCS_INPUT_URI = "gs://data_data_governance_001/sample_dataset.dat"
    RESULTS_DATASET_ID = "dlp_results"
    RESULTS_TABLE_ID = "testtable"
    TEMPLATE_ID = "3763771487318451314"
    TEMPLATE_NAME = f"projects/{PROJECT_ID}/locations/global/inspectTemplates/{TEMPLATE_ID}"

    # Prepare replacements for placeholders
    replacements = {
        "GCS_INPUT_URI": GCS_INPUT_URI,
        "TEMPLATE_NAME": TEMPLATE_NAME,
        "PROJECT_ID": PROJECT_ID,
        "RESULTS_DATASET_ID": RESULTS_DATASET_ID,
        "RESULTS_TABLE_ID": RESULTS_TABLE_ID,
    }

    # Load the configuration and replace placeholders
    inspect_job_config = load_and_fill_config(CONFIG_FILE, replacements)

    # Create the DLP inspect job
    job_name = create_dlp_inspect_job_with_template(PROJECT_ID, inspect_job_config)
    print(f"Created DLP Inspect Job: {job_name}")

    #poll_for_job_completion(job_name)
