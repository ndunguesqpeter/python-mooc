import os
import sys
from datetime import datetime
from pathlib import Path
from netmiko import ConnectHandler

DEVICES = {
    "S1": "192.168.50.82",
    "S2": "192.168.50.83",
}

user = os.environ["LAB_USER"]
password = os.environ["LAB_PASS"]

out_dir = Path("backups")
out_dir.mkdir(exist_ok=True)
stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
failed = []

for name, ip in DEVICES.items():
    try:
        with ConnectHandler(device_type="cisco_ios", host=ip,
                            username=user, password=password, timeout=20) as conn:
            config = conn.send_command("show running-config")
        (out_dir / f"{name}_{stamp}.cfg").write_text(config)
        print(f"[OK]   {name} ({ip}) saved")
    except Exception as e:
        print(f"[FAIL] {name} ({ip}): {e}")
        failed.append(name)

sys.exit(1 if failed else 0)