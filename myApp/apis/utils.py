import os
import firebase_admin
from firebase_admin import credentials, messaging


def notify(data):
    try:
        cred = credentials.Certificate(
            {
            "type": os.getenv('TYPE'),
            "project_id": os.getenv('PROJECT_ID'),
            "private_key_id": os.getenv('PRIVATE_API_KEY_ID'),
            "private_key": os.getenv('PRIVATE_KEY'),
            "client_email": os.getenv('CLIENT_EMAIL'),
            "client_id": os.getenv('CLIENT_ID'),
            "auth_uri": os.getenv('AUTH_URI'),
            "token_uri": os.getenv('TOKEN_URI'),
            "auth_provider_x509_cert_url": os.getenv('AUTH_PROVIDER'),
            "client_x509_cert_url": os.getenv('CLIENT_CETR_URI')
        }
        )
        try:
            firebase_admin.get_app()
        except ValueError:
            firebase_admin.initialize_app(cred)

        fcm_token = data["fcm_token"]
        del data['fcm_token']
        message = messaging.Message(
            data,
            token=fcm_token
        )
        messaging.send(message)
        return True
    except Exception as e:
        return f"{e}"