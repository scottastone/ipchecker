# Copyright Scott Stone (c) 2022
import ipinfo
import sys
import pprint

class IPProcessor():
    def __init__(self, ip, token_file_name: str='access_token'):
        self.token_file_name = token_file_name
        self._load_access_token()
        self.handler = ipinfo.getHandler(access_token=self.access_token)
        self.ip = ip
        self.pprinter = pprint.PrettyPrinter()

        self._check_and_strip_ip()
    
    def _load_access_token(self):
        try:
            with open(self.token_file_name, 'r') as f:
                self.access_token = f.read()
        except FileNotFoundError:
            print('File not found: access_token')
            sys.exit(1)

    def _check_and_strip_ip(self):
        self.ip = [ip.split(':')[0] for ip in self.ip]
        for ip in self.ip:
            if ip.count('.') != 3:
                print(f'Invalid IP address: {self.ip}')
                sys.exit(1)

            for num in ip.split('.'):
                if int(num) > 255:
                    print(f'Invalid IP address: {self.ip}')
                    sys.exit(1)
        
    def get_details(self):
        if len(self.ip) > 1:
            ip_data = self.handler.getBatchDetails(self.ip)
        elif len(self.ip) == 1: 
            ip_data = self.handler.getDetails(self.ip[0]).all
        
        self.pprinter.pprint(ip_data)
        return ip_data