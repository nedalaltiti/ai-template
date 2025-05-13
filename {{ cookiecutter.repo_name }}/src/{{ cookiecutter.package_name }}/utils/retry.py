# retry.py
import time

def retry(func, retries=3, delay=1):
    for _ in range(retries):
        try:
            return func()
        except Exception:
            time.sleep(delay)
    raise Exception("Max retries exceeded")