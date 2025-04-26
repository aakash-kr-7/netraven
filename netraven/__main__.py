from .log_parser import parse_auth_log
from .geoip_lookup import get_geoip_data
from .cve_lookup import get_cve_data
from .report_writer import write_report, generate_blocklist
from .summary import print_summary
from .utils import color_print

from tqdm import tqdm
import time

def main():
    color_print("Starting NetRaven...", "cyan")
    time.sleep(0.5)

    color_print("Scanning logs for failed login attempts...", "yellow")
    attempts = parse_auth_log()
    time.sleep(0.5)

    if not attempts:
        color_print("No failed login attempts found.", "green")
        return

    color_print("Performing GeoIP and CVE lookups...", "yellow")

    enriched_data = []
    for ip, count in tqdm(attempts.items(), desc="Processing IPs", colour="cyan"):
        geo = get_geoip_data(ip)
        cve = get_cve_data(ip)
        enriched_data.append({
            "ip": ip,
            "attempts": count,
            "country": geo.get("country", "Unknown"),
            "region": geo.get("region", "Unknown"),
            "city": geo.get("city", "Unknown"),
            "cve": cve
        })
        time.sleep(0.1)  # optional: simulate work for smoother bar

    print_summary(enriched_data)
    
    color_print("Writing final report and blocklist...", "yellow")
    write_report(enriched_data)
    generate_blocklist([ip["ip"] for ip in enriched_data])
    time.sleep(0.5)

    color_print("Done. Stay safe out there, operator.", "green")
