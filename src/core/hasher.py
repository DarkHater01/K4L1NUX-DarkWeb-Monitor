import hashlib
import os


def hash_value(value: str, salt: str | None = None) -> str:
    """Devuelve un fingerprint SHA-256. Nunca guardamos el valor en claro."""
    salt = salt if salt is not None else os.environ.get("K4L1NUX_SALT", "")
    return hashlib.sha256((salt + value).encode("utf-8")).hexdigest()
