"""Constants for aioshelly."""
import asyncio

import aiohttp

from .exceptions import DeviceConnectionError

CONNECT_ERRORS = (
    aiohttp.ClientError,
    asyncio.TimeoutError,
    DeviceConnectionError,
    OSError,
)

MODEL_NAMES = {
    # Gen1 CoAP based models
    "SH2LED-1": "Shelly 2LED",
    "SHAIR-1": "Shelly Air",
    "SHBDUO-1": "Shelly DUO",
    "SHBLB-1": "Shelly Bulb",
    "SHBTN-1": "Shelly Button1",
    "SHBTN-2": "Shelly Button1",  # hw v2
    "SHBVIN-1": "Shelly Vintage",
    "SHCB-1": "Shelly Bulb RGBW",
    "SHCL-255": "Shelly Color",
    "SHDIMW-1": "Shelly Dimmer W1",
    "SHDM-1": "Shelly Dimmer",
    "SHDM-2": "Shelly Dimmer 2",
    "SHDW-1": "Shelly Door/Window",
    "SHDW-2": "Shelly Door/Window 2",
    "SHEM": "Shelly EM",
    "SHEM-3": "Shelly 3EM",
    "SHGS-1": "Shelly Gas",
    "SHHT-1": "Shelly H&T",
    "SHIX3-1": "Shelly i3",
    "SHMOS-01": "Shelly Motion",
    "SHMOS-02": "Shelly Motion 2",
    "SHPLG-1": "Shelly Plug",
    "SHPLG-S": "Shelly Plug S",
    "SHPLG-U1": "Shelly Plug US",
    "SHPLG2-1": "Shelly Plug E",
    "SHRGBW2": "Shelly RGBW2",
    "SHRGBWW-01": "Shelly RGBW",
    "SHSEN-1": "Shelly Sense",  # CoAP v1, unsupported
    "SHSM-01": "Shelly Smoke",
    "SHSM-02": "Shelly Smoke 2",
    "SHSPOT-1": "Shelly Spot",
    "SHSPOT-2": "Shelly Spot 2",
    "SHSW-1": "Shelly 1",
    "SHSW-21": "Shelly 2",
    "SHSW-25": "Shelly 2.5",
    "SHSW-44": "Shelly 4Pro",  # CoAP v1, unsupported
    "SHSW-L": "Shelly 1L",
    "SHSW-PM": "Shelly 1PM",
    "SHTRV-01": "Shelly Valve",
    "SHUNI-1": "Shelly UNI",
    "SHVIN-1": "Shelly Vintage",
    "SHWT-1": "Shelly Flood",
    # Gen2 RPC based models
    "SAWD-0A1XX10EU1": "Shelly Wall Display",
    "SNGW-0A11WW010": "Shelly Plus 10V",
    "SNPL-00110IT": "Shelly Plus Plug IT",
    "SNPL-00112EU": "Shelly Plus Plug S",
    "SNPL-00112UK": "Shelly Plus Plug UK",
    "SNPL-00116US": "Shelly Plus Plug US",
    "SNPM-001PCEU16": "Shelly Plus PM Mini",
    "SNSN-0013A": "Shelly Plus H&T",
    "SNSN-0031Z": "Shelly Plus Smoke",
    "SNSN-0043X": "Shelly Plus Uni",
    "SNSN-0D24X": "Shelly Plus I4DC",
    "SNSW-001P15UL": "Shelly Plus 1PM UL",
    "SNSW-001P16EU": "Shelly Plus 1PM",
    "SNSW-001P8EU": "Shelly Plus 1PM Mini",
    "SNSW-001X15UL": "Shelly Plus 1 UL",
    "SNSW-001X16EU": "Shelly Plus 1",
    "SNSW-001X8EU": "Shelly Plus 1 Mini",
    "SNSW-0024X": "Shelly Plus I4",
    "SNSW-002P16EU": "Shelly Plus 2PM",
    "SNSW-102P16EU": "Shelly Plus 2PM",
    "SPEM-002CEBEU50": "Shelly Pro EM",
    "SPEM-003CEBEU": "Shelly Pro 3EM",
    "SPSH-002PE16EU": "Shelly Pro Dual Cover PM",
    "SPSW-001PE16EU": "Shelly Pro 1PM",
    "SPSW-001XE16EU": "Shelly Pro 1",
    "SPSW-002PE16EU": "Shelly Pro 2PM",
    "SPSW-002XE16EU": "Shelly Pro 2",
    "SPSW-003XE16EU": "Shelly Pro 3",
    "SPSW-004PE16EU": "Shelly Pro 4PM",
    "SPSW-101PE16EU": "Shelly Pro 1PM",
    "SPSW-101XE16EU": "Shelly Pro 1",
    "SPSW-102PE16EU": "Shelly Pro 2PM",
    "SPSW-102XE16EU": "Shelly Pro 2",
    "SPSW-104PE16EU": "Shelly Pro 4PM",
    "SPSW-201PE16EU": "Shelly Pro 1PM",
    "SPSW-201XE16EU": "Shelly Pro 1",
    "SPSW-202PE16EU": "Shelly Pro 2PM",
    "SPSW-202XE16EU": "Shelly Pro 2",
}

# Timeout used for Device IO
DEVICE_IO_TIMEOUT = 10

# Timeout used for HTTP calls
HTTP_CALL_TIMEOUT = 10

# Firmware 1.8.0 release date (CoAP v2)
GEN1_MIN_FIRMWARE_DATE = 20200812

# Firmware 0.8.1 release date
GEN2_MIN_FIRMWARE_DATE = 20210921

WS_HEARTBEAT = 55

# Default Gen2 outbound websocket API URL
WS_API_URL = "/api/shelly/ws"

# Notification sent by RPC device in case of WebSocket close
NOTIFY_WS_CLOSED = "NotifyWebSocketClosed"
