import ipaddress

# Lista de ips que não pode ser usado
def block_ip(ip):

    prohibited_ranges = [
        "200.219.0.0/23",
        "177.221.56.0/24",
        "177.221.57.128/25",
        "177.221.58.0/24",
        "177.221.59.0/24",
        "168.205.124.128/25",
        "168.205.125.128/25",
        "168.205.126.128/25",
        "168.205.127.0/24",
        "187.63.236.0/24",
        "187.63.237.0/24",
        "187.63.238.0/24",
        "187.63.239.0/25",
        "179.63.156.0/24",
        "179.63.157.0/24",
        "179.63.158.0/24",
        "179.63.159.0/24",
        "45.179.86.128/25",
    ]

    ip_range = ipaddress.IPv4Address(ip)
    for prohibited_range in prohibited_ranges:
        if ip_range in ipaddress.IPv4Network(prohibited_range):
            return True
    return False


# return se o ip podee sere usando
def const_prefix(ip):
    prefixo = ipaddress.IPv4Network(ip, strict=False)
    ips = []
    for ipv4 in prefixo:
        ips.append(str(ipv4))

    return ips
