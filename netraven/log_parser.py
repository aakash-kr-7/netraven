import re
from collections import defaultdict

def parse_auth_log(log_path="/var/log/auth.log"):
    ip_attempts = defaultdict(int)
    ip_pattern = re.compile(r"Failed password.*from (\d+\.\d+\.\d+\.\d+)")
    
    try:
        with open(log_path, "r") as f:
            for line in f:
                match = ip_pattern.search(line)
                if match:
                    ip = match.group(1)
                    ip_attempts[ip] += 1
    except FileNotFoundError:
        print(f"[!] Log file not found: {log_path}")
    
    return dict(ip_attempts)
