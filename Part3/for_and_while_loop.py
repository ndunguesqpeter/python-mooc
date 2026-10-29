device_ips = [
              ["10.254.0.1", "not connected"],
              ["10.254.0.2", "not connected"],
              ["10.254.0.3", "not connected"]
              ]

for ip in device_ips:
    print(f"\nAttempting to establish a connection {ip[0]}")
    attempt = 0
    
    while attempt < 5:
        print("Establishing a connection...")
        attempt += 1
    print("Connection Established!")
    #ip[1] = "connected" modifies the original sub-list 
    # by replacing "not connected" with "connected
    ip[1] = "connected"
print(device_ips)