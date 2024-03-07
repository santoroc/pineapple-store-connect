import jwt
from datetime import datetime


class Authenticator:

    def __init__(self, key_id, issuer_id, private_key):
        self.key_id = key_id
        self.issuer_id = issuer_id
        self.private_key = private_key


    def generate_token(self, endpoint: str, parameters: str) -> str:
        """
        Generate the JWT token for App Store Connect API authentication.
        args:
            endpoint (str): example: '/v1/salesReports'
            parameters (str): url parameters to be used with the request.
                                Must be the same parameters used on the request.
        return:
            JWT token (str)
        """


        ALGORITHM = 'ES256'

        issue_epoch = int(datetime.now().strftime('%s'))
        self._expiration_epoch = issue_epoch + 1200 # + 20 min

        payload = {
                'iss': self.issuer_id,
                'iat': issue_epoch,
                'exp': self._expiration_epoch,
                'aud': 'appstoreconnect-v1',
                'scope': [f'GET {endpoint}?{parameters}']
            }
        
        headers = {
                'alg': ALGORITHM,
                'kid': self.key_id,
                'typ': 'JWT'
            }

        token = jwt.encode(
                payload=payload,
                key=self.private_key,
                headers=headers,
                algorithm=ALGORITHM
            ).decode('utf-8')
        
        return token