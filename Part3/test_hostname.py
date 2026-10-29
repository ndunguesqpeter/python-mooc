device_facts = {"vendor": "cisco",
                "os_version": 16.8,
                "platform": "cisco catalyst",
                "os_type": "ios",
                "hostname": "R1"
}

for key, data in device_facts.items():
    # Replace underscore with a hyphen if you want exactly 'os-version' instead of 'os_version'
    formatted_key = key.replace("_", "-")
    print(f"{formatted_key}: {data}")