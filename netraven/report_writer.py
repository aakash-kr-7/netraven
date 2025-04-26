import pandas as pd
import os

def write_report(ip_data):
    os.makedirs("netraven/output", exist_ok=True)
    report_path = "netraven/output/intrusion_report.csv"
    
    df = pd.DataFrame(ip_data)
    df.to_csv(report_path, index=False)
    print(f"[+] CSV report saved to {report_path}")

def generate_blocklist(ip_list):
    blocklist_path = "netraven/output/blocklist.sh"
    
    with open(blocklist_path, "w") as f:
        f.write("#!/bin/bash\n\n")
        for ip in ip_list:
            f.write(f"iptables -A INPUT -s {ip} -j DROP\n")
    
    print(f"[+] Blocklist script saved to {blocklist_path}")
