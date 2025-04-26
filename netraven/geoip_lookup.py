import requests

def get_geoip_data(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        return {
            "country": data.get("country", "Unknown"),
            "region": data.get("regionName", "Unknown"),
            "city": data.get("city", "Unknown")
        }
    except Exception as e:
        return {
            "country": "Error",
            "region": "Error",
            "city": "Error"
        }
