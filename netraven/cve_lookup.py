import requests

def get_cve_data(ip):
    # Simulate tool signature. In real world, you'd detect the tool from logs.
    # Here, we use 'sshd' to represent potential SSH vulnerabilities.
    keyword = "sshd"
    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={keyword}&resultsPerPage=1"
    
    headers = {
        "User-Agent": "NetRavenCLI"
    }
    
    try:
        r = requests.get(url, headers=headers, timeout=5)
        if r.status_code == 200:
            data = r.json()
            cves = data.get("vulnerabilities", [])
            if cves:
                return cves[0]["cve"]["id"]
        return "None"
    except Exception as e:
        return "Error"
