from dotenv import load_dotenv
import os

from .az_secrets import secrets_get

LANG_SERVICE = 'language'

def get_credentials(services: list):

    # Create an empty dictionary to store the credentials
    creds = {}

    # Load the variables from the .env file
    load_dotenv()

    for service in services:

        endpoint = None
        key = None

        if service == LANG_SERVICE:
            print(f'Retrieve endpoint and key for {service}.')
            endpoint = os.getenv("LANG_ENDPOINT")
            key = secrets_get(os.getenv("LANG_SECRET"))
        else:
            print(f"Service '{service}' not supported.")

        # Add credential dictionary to the list
        creds[service] = {
            'endpoint': endpoint,
            'key': key
        }

    return creds
            

