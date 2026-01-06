import hashlib


def hash_feature(text: str, buckets: int = 10) -> int:
    """
    Convert a text feature into a fixed bucket index using hashing.
    """
    hashed_value = hashlib.md5(text.encode()).hexdigest()
    return int(hashed_value, 16) % bucket

