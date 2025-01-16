import os
import time

import jwt

private_key = os.environ.get('PRIVATE_KEY')
if private_key is None:
    print('pem is not set')
    exit(1)

client_id = os.environ.get('CLIENT_ID')
if client_id is None:
    print('client_id is not set')
    exit(1)

payload = {
    # Issued at time
    'iat': int(time.time()),
    # JWT expiration time (10 minutes maximum)
    'exp': int(time.time()) + 600,
    
    # GitHub App's client ID
    'iss': client_id
}

# Create JWT
encoded_jwt = jwt.encode(payload, private_key.encode(), algorithm='RS256')

print(f"JWT={encoded_jwt}")
