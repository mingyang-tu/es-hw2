# Embedded System HW-2 CubeIDE

> download [STM32CubeL4](https://github.com/STMicroelectronics/STM32CubeL4)

> modified from sample code for wifi client/server

> replace main.cpp in directory in STM32CubeL4-master/Projects/B-L475E-IOT01A/Applications/WiFi/WiFi_Client_Server/Src/main.c

> replace .project and .cproject in STM32CubeL4-master/Projects/B-L475E-IOT01A/Applications/WiFi/WiFi_Client_Server/SW4STM32/B-L475E-IOT01/
### Adjustment
Modify main.h (WiFi_Client_Server/Inc/main.h)
```javascript
#include "wifi.h"
#include "stm32l475e_iot01.h"
#include "stm32l4xx_hal.h"               <--add
#include "stm32l475e_iot01_accelero.h"   <--add
#include "stm32l475e_iot01_magneto.h"    <--add
#include "stm32l475e_iot01_gyro.h"       <--add
#include "stm32l475e_iot01_tsensor.h"    <--add
#include "stm32l475e_iot01_psensor.h"    <--add
#include "stm32l475e_iot01_hsensor.h"    <--add
#include "stm32l475e_iot01_qspi.h"       <--add
#include "stdio.h"
```
Enable HAL_QSPI_MODULE in stm32l4xx_hal_conf.h
![image](https://user-images.githubusercontent.com/59012686/229274080-fef65dff-dac1-47f7-8e55-1a5027128f24.png)
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
