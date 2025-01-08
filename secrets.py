from dotenv import load_dotenv
import os

from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

def initialise_client():
    # Load the variables from the .env file
    load_dotenv()

    # Set key vault name from .env
    vault = os.getenv('VAULT_NAME')

    # Initialise client
    uri = f"https://{vault}.vault.azure.net"

    return SecretClient(vault_url=uri, credential=DefaultAzureCredential())

def secrets_get(secretName):
    client = initialise_client()
    return client.get_secret(secretName).value