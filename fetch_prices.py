import requests

r = requests.get("https://soodana.ir", timeout=30)
print(r.status_code)
print(r.text[:200])
