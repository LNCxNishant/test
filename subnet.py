import ipaddress

def calculate_subnet_info(ip_address, subnet_prefix):
    # Parse the IP address and create an IPv4Network object
    ip = ipaddress.IPv4Network(f"{ip_address}/{subnet_prefix}", strict=False)
    
    # Get the subnet mask
    subnet_mask = ip.netmask
    
    # Get the first address in the subnet
    first_address = ip.network_address
    
    # Get the last address in the subnet
    last_address = ip.broadcast_address
    
    # Calculate the number of addresses in the subnet
    num_addresses = len(list(ip.hosts()))
    
    return subnet_mask, first_address, last_address, num_addresses

# Example usage
ip_address = "192.168.1.10"
subnet_prefix = 24  # This is equivalent to a subnet mask of 255.255.255.0

subnet_mask, first_address, last_address, num_addresses = calculate_subnet_info(ip_address, subnet_prefix)

print(f"IP Address: {ip_address}")
print(f"Subnet Mask: {subnet_mask}")
print(f"First Address: {first_address}")
print(f"Last Address: {last_address}")
print(f"Number of Addresses: {num_addresses}")
