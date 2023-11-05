import ipaddress

def calculate_subnet_info(ip_address, subnet_prefix):
    ip = ipaddress.IPv4Network(f"{ip_address}/{subnet_prefix}", strict=False)
    subnet_mask = ip.netmask
    first_address = ip.network_address
    last_address = ip.broadcast_address
    num_addresses = len(list(ip.hosts()))
    
    return subnet_mask, first_address, last_address, num_addresses
ip_address = input("Enter the IP address: ")
subnet_prefix = int(input("Enter the subnet prefix (e.g., 24 for /24): "))

subnet_mask, first_address, last_address, num_addresses = calculate_subnet_info(ip_address, subnet_prefix)
print(f"IP Address: {ip_address}")
print(f"Subnet Mask: {subnet_mask}")
print(f"First Address: {first_address}")
print(f"Last Address: {last_address}")
print(f"Number of Addresses: {num_addresses}")
