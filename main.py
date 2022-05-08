# Copyright Scott Stone (c) 2022
import sys
from ipprocessor import IPProcessor

def main():
    try:
        inputs = sys.argv[1]
    except IndexError:
        print('Usage: main.py <ip_address>')
        sys.exit(1)    

    ip_address = get_ips(inputs)
    
    info = IPProcessor(token_file_name='access_token', ip=ip_address)
    info.get_details()

def get_ips(inputs) -> list[str]:
    if inputs.endswith(".txt"):
        with open(inputs, 'r') as f:
            ip_address = f.readlines()
            print(f"Found {len(ip_address)} IP addresses")
    else:
        ip_address = [inputs]
    ip_address = [ip.strip() for ip in ip_address]
    return ip_address

if __name__ == '__main__':
    main()