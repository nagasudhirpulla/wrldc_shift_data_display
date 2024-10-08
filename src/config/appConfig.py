from dataclasses import dataclass, field
import json


@dataclass
class AppConfig:
    host: str = field(default="localhost")
    port: int = field(default=8080)
    histDataUrlBase: str = field(default="")
    isRandom: bool = field(default=False)
    freqPnt: str = field(default="")
    demPnt: str = field(default="")
    wrErPnt: str = field(default="")
    wrSrPnt: str = field(default="")
    wrNrPnt: str = field(default="")
    wrIrPnt: str = field(default="")


def loadAppConfig(fName="config/config.json") -> AppConfig:
    global jsonConfig
    with open(fName) as f:
        data = json.load(f)
        jsonConfig = AppConfig(**data)
        return jsonConfig


def getAppConfig() -> AppConfig:
    global jsonConfig
    return jsonConfig
