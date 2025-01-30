from google.cloud import dlp_v2
import json


def load_and_fill_template_config(file_path, replacements):
    with open(file_path, "r") as file:
        config = json.load(file)
    # Replace placeholders in the config
    config_str = json.dumps(config)
    for key, value in replacements.items():
        config_str = config_str.replace(f"{{{{{key}}}}}", value)

    print(f"DEBUG: After replacements, config string: {config_str}")
    return json.loads(config_str)


def create_dlp_job_template(project_id, template_id, inspect_template_config):
    dlp = dlp_v2.DlpServiceClient()

    # Define the parent project location
    parent = f"projects/{project_id}/locations/us-east1"

    # Convert min_likelihood from string to the DLP API enum value
    inspect_template_config["inspect_config"]["min_likelihood"] = dlp_v2.Likelihood[
        inspect_template_config["inspect_config"]["min_likelihood"]
    ]

    # Create the inspect job template
    response = dlp.create_inspect_template(
        parent=parent,
        inspect_template=inspect_template_config,
    )

    print(f"DLP Inspect Job Template created: {response.name}")
    return response.name


if __name__ == "__main__":
    CONFIG_FILE = "inspect_template_config.json"  # Path to your JSON configuration file
    PROJECT_ID = "upgradlabs-1735976404499"
    TEMPLATE_ID = "EMAIL_PHONE_INSPECT"

    # Prepare replacements for placeholders
    replacements = {
        "DISPLAY_NAME": TEMPLATE_ID,
        "DESCRIPTION": "Template for detecting EMAIL_ADDRESS, PHONE_NUMBER",
        "INFO_TYPES": json.dumps([{"name": "EMAIL_ADDRESS"}, {"name": "PHONE_NUMBER"}]),
        "MIN_LIKELIHOOD": "POSSIBLE",
        "INCLUDE_QUOTE": "true"
    }

    # Load and fill the configuration
    inspect_template_config = load_and_fill_template_config(CONFIG_FILE, replacements)

    # Create the DLP inspect job template
    template_name = create_dlp_job_template(PROJECT_ID, TEMPLATE_ID, inspect_template_config)
    print(f"Created DLP Job Template: {template_name}")
