from collections import Counter
from colorama import Fore

def print_summary(ip_data):
    countries = [ip["country"] for ip in ip_data]
    ip_list = [ip["ip"] for ip in ip_data]
    attempts = [ip["attempts"] for ip in ip_data]

    print(f"{Fore.CYAN}=== Summary Statistics ===")
    print(f"{Fore.GREEN}Total Unique Attackers: {len(ip_list)}")
    print(f"Total Failed Attempts: {sum(attempts)}")
    
    top_countries = Counter(countries).most_common(3)
    print(f"{Fore.YELLOW}Top Attack Origins:")
    for country, count in top_countries:
        print(f"{country}: {count} IPs")
