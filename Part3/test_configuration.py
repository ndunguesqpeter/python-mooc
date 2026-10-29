config_data = {
    "R1": {
        "banner": "This Device is being monitored 24/7.",
        "mgmt_ip": "10.254.0.1",
        "interface_data": [
            {
                "if_name": "GigabitEthernet1",
                "state": "shutdown",
                "mode": "access",
                "config": "10",
            },
            {
                "if_name": "GigabitEthernet2",
                "state": "up",
                "mode": "routing",
                "config": "10.12.0.1",
            },
            {
                "if_name": "GigabitEthernet3",
                "state": "up",
                "mode": "routing",
                "config": "10.13.0.1",
            },
        ],
    }
}
print(config_data["R1"]["interface_data"][1]["mode"])