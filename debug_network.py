import requests

url = "https://reqres.in/api/users?page=2"

print("--- NETWORK DEBUGGER ---")

# Test 1: Raw Request (No Headers)
print("\n1. Testing Raw Request (No Headers)...")
try:
    r = requests.get(url, timeout=10)
    print(f"   Status: {r.status_code}")
    if r.status_code == 403:
        print(f"   Block Reason: {r.text[:300]}") # Prints the error message from server
except Exception as e:
    print(f"   Failed: {e}")

# Test 2: Browser Mimic (With Headers)
print("\n2. Testing Browser Headers...")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.9"
}
try:
    r = requests.get(url, headers=headers, timeout=10)
    print(f"   Status: {r.status_code}")
    if r.status_code == 200:
        print("   ✅ SUCCESS! The headers are working.")
    elif r.status_code == 403:
        print(f"   ❌ STILL BLOCKED. Server says: {r.text[:300]}")
except Exception as e:
    print(f"   Failed: {e}")