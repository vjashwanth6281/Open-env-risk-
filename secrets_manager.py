import os

def get_secret(secret_name):
    try:
        from huggingface_hub import get_space_secret
        secret = get_space_secret(secret_name)
        if secret: return secret
    except ImportError:
        pass
    return os.environ.get(secret_name)
