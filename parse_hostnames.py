import re
import sys

def parse_hostname(line):
    """Parses the hostname, strips out IP addresses
    """
    regex = re.compile('^(?P<host>.*|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s(?P<key_type>ssh-.*)\s(?P<fingerprint>.*)$')
    r = regex.search(line).groupdict()['host']
    li = [ elem for elem in r.split(',') if not valid_ipv4(r) ]
    if li:
        return li[0]

def valid_ipv4(ip):
    """Validates IPv4 Addresses
    """
    # Shamelessly stolen from stack overflow 
    # http://stackoverflow.com/questions/319279/how-to-validate-ip-address-in-python
    pattern = re.compile(r"""
        ^
        (?:
          (?:
            [3-9]\d?|2(?:5[0-5]|[0-4]?\d)?|1\d{0,2}
          |
            0x0*[0-9a-f]{1,2}
          |
            0+[1-3]?[0-7]{0,2}
          )
          (?:
            \.
            (?:
              [3-9]\d?|2(?:5[0-5]|[0-4]?\d)?|1\d{0,2}
            |
              0x0*[0-9a-f]{1,2}
            |
              0+[1-3]?[0-7]{0,2}
            )
          ){0,3}
        |
          0x0*[0-9a-f]{1,8} 
        |
          0+[0-3]?[0-7]{0,10}
        |
          429496729[0-5]|42949672[0-8]\d|4294967[01]\d\d|429496[0-6]\d{3}|
          42949[0-5]\d{4}|4294[0-8]\d{5}|429[0-3]\d{6}|42[0-8]\d{7}|
          4[01]\d{8}|[1-3]\d{0,9}|[4-9]\d{0,8}
        )
        $
    """, re.VERBOSE | re.IGNORECASE)
    return pattern.match(ip) is not None

def main(root, known_hosts_file):  
    hostnames = []                    
    tmp = ""
    f = open(known_hosts_file, 'r')
    for line in f:
        hostnames.append(parse_hostname(line))
        hostnames = [ f for f in sorted(set(hostnames)) if f != None ]
    for host in hostnames:
        tmp = tmp + " " + root + "@" + host
    print tmp  

if __name__ == "__main__":
    main(root=sys.argv[1], known_hosts_file=sys.argv[2])    

    

