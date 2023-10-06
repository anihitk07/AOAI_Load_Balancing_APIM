import requests
import json
import logging
import sys
import os
from msal import ConfidentialClientApplication

def get_sp_access_token(client_id, client_credential, tenant_name, scopes):
    logging.info('Attempting to obtain an access token...')
    result = None
    print(tenant_name)
    app = ConfidentialClientApplication(
        client_id=client_id,
        client_credential=client_credential,
        authority=f"https://login.microsoftonline.com/{tenant_name}",
    )
    result = app.acquire_token_for_client(scopes=scopes)

    if "access_token" in result:
        logging.info('Access token successfully acquired')
        return result['access_token']
    else:
        logging.error('Unable to obtain access token')
        logging.error(f"Error was: {result['error']}")
        logging.error(f"Error description was: {result['error_description']}")
        logging.error(f"Error correlation_id was: {result['correlation_id']}")
        raise Exception('Failed to obtain access token')
    
def main():
    # Setup logging
    try:
        logging.basicConfig(
            level=logging.ERROR,
            format='%asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[logging.StreamHandler(sys.stdout)]
        )
    except:
        logging.error('Failed to setup logging: ', exc_info=True)

    try:
        # Obtain an access token
        token = get_sp_access_token(
            client_id = os.getenv('CLIENT_ID'),
            client_credential = os.getenv('CLIENT_SECRET'),
            tenant_name = os.getenv('TENANT_ID'),
            scopes = "https://cognitiveservices.azure.com/.default"
        )
    except:
        logging.error('Failed to obtain access token: ', exc_info=True)

    try:
        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}',
        'api-key': f'{os.getenv("APIM_API_KEY")}',
        }

        params = {
            'api-version': '2023-03-15-preview',
        }

        json_data = {
            'model': f'{os.getenv("DEPLOYMENT_NAME")}',
            'messages': [
                {
                    'role': 'user',
                    'content': 'Once upon a time',
                },
            ],
        }
        for x in range(10):
            response = requests.post(
                f'{os.getenv("OPENAI_API_COMPLETION")}',
                params=params,
                headers=headers,
                json=json_data,
            )
            res = json.loads(response.content)
            print(json.dumps(res, indent=4, sort_keys=True))

    except:
        logging.error('Failed to summarize file: ', exc_info=True)


if __name__ == "__main__":
    main()
