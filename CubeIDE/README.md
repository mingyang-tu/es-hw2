# Embedded System HW-2 CubeIDE

> download [STM32CubeL4](https://github.com/STMicroelectronics/STM32CubeL4)

### Configuring
Open `main.cpp`, set hostname, SSID and password.

```javascript
#include "main.h"

/* Private defines -----------------------------------------------------------*/

#define TERMINAL_USE

/* Update SSID and PASSWORD with own Access point settings */
#define SSID     "esys305"        <--your wifi ssid
#define PASSWORD "305305abcd"     <--your wifi password

uint8_t RemoteIP[] = {192,168,50,153};  <--your ip address
#define RemotePORT	6538            <--your port number

#define WIFI_WRITE_TIMEOUT 10000
#define WIFI_READ_TIMEOUT  10000

#define CONNECTION_TRIAL_MAX          10
```
Open `server.py`, set hostname.

```
HOST = "HOSTNAME"  # IP address
PORT = port  # Port to listen on (use ports > 1023)
```

### Run `server.py`
Have to install pip3
```
python server.py
```

### Build and run `main.cpp`

## How to Run Code
1. `pip3 install {需要的模組}`
2. 運行`GUI-hw2.py`
