# Copyright Scott Stone (c) 2022
import sys
from ipprocessor import IPProcessor

def main():
    try:
        nargs = len(sys.argv)
        if nargs == 2:
            inputs = sys.argv[1]
        if nargs == 1:
            print("No input file specified. Doing a default lookup on 8.8.8.8")
            inputs = "8.8.8.8"

    except IndexError:
        print('Usage: main.py <ip_address>')
        sys.exit(1)    

    ip_address = get_ips(inputs)
    info = IPProcessor(token_file_name='access_token', ip=ip_address)
    ip_data = info.get_details()

def get_ips(inputs) -> list[str]:
    if inputs.endswith(".txt"):
        with open(inputs, 'r') as f:
            ip_address = f.readlines()
    else:
        ip_address = [inputs]

    ip_address = [ip.strip() for ip in ip_address]
    return ip_address

if __name__ == '__main__':
    main()