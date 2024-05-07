import hashlib
import hmac
import urllib.parse


def verify_shopify_hmac(query_string, client_secret):
    # Parse the query string into a dictionary
    query_params = urllib.parse.parse_qs(query_string)

    # Remove the HMAC parameter
    hmac_param = query_params.pop('hmac')[0]
    
    print(hmac_param)

    # Sort the remaining parameters alphabetically by parameter name
    sorted_params = "&".join([f"{k}={v[0]}" for k, v in sorted(query_params.items())])
    
    print(sorted_params)

    # Calculate the HMAC-SHA256 hash
    hash_digest = hmac.new(bytes(client_secret, 'utf-8'), msg=bytes(sorted_params, 'utf-8'), digestmod=hashlib.sha256).hexdigest()
    
    print(hash_digest)

    # Compare the calculated HMAC with the received HMAC
    return hmac.compare_digest(hash_digest, hmac_param)