# Embedded System HW-2 MbedOS

> Modified from [mbed-os-example-sockets](https://github.com/ARMmbed/mbed-os-example-sockets)

## Members

- 毛楷維 b07901134
- 古振宏 b08901103
- 涂銘洋 b07202031

## Getting Started

### Libraries

- [BSP_B-L475E-IOT01](https://os.mbed.com/teams/ST/code/BSP_B-L475E-IOT01/)
- [COMPONENT_ism43362](https://github.com/ARMmbed/wifi-ism43362/)
- mbed-os (6.13.0)

### Configuring

Open `mbed_app.json`, set hostname, SSID and password.

```
{
    "config": {
        "hostname": {
            "help": "The demo will try to connect to this web address on port 80 (or port 443 when using tls).",
            "value": "\"HOSTNAME\""     <--
        },
        "use-tls-socket": {
            "value": false
        }
    },
    "target_overrides": {
        "*": {
            "nsapi.default-wifi-security": "WPA_WPA2",
            "nsapi.default-wifi-ssid": "\"SSID\"",              <--
            "nsapi.default-wifi-password": "\"PASSWORD\"",      <--
```

Open `server.py`, set hostname.

```
HOST = "HOSTNAME"  # IP address
```

### Run `server.py`

```
install pip3
python server.py
```

### Build and run `main.cpp`

### demo photo

