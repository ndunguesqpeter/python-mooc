import json
cisco_lifecycle_data = {
    "cisco_ios":{
        "latest_release": "15.8(3)M",
        "list_of_supported_devices": ["Catalyst 2960", "Catalyst 4500"],
        "list_of_eol_devices": [
            {"model": "Catalyst 2940", "eol_date": "11/6/2016"},
            {"model": "Catalyst 3560", "eol_date": "11/14/2013"}
        ],
    },
    "cisco_nxos": {
        "latest_release": "7.0(3)I7(6)",
                "list_of_supported_devices": ["Nexus 9508", "nexus 7000"],
                "list_of_eol_devices": [
                    {"model": "Nexus 5000", "eol_date": "05/5/2018"},
                    {"model": "Nexus 3500", "eol_date": "12/21/2018"}
                ],
    }     
}

for os, data in cisco_lifecycle_data.items():
    print(f"Latest release for {os} is {data["latest_release"]}.")
    print("")
    print(f"Latest release for {os} is {data["list_of_eol_devices"][1]["eol_date"]}.")
print("")
print(json.dumps(cisco_lifecycle_data["cisco_ios"]["list_of_eol_devices"][0]["model"], indent=2))
print("")
new = json.dumps(cisco_lifecycle_data, indent=2)
