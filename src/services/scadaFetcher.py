import json
import random
import pandas as pd
import requests
from src.config.appConfig import getAppConfig
import datetime as dt


def fetchScadaPntHistData(pntId: str, startTime: dt.datetime, endTime: dt.datetime, type="snap", secs=60) -> pd.Series:
    appConf = getAppConfig()
    if appConf.isRandom == True:
        return fetchScadaPntRandHistData(pntId, startTime, endTime)
    pntId = pntId.strip()
    if pntId == "":
        return pd.Series()
    urlStr = appConf.histDataUrlBase
    paramsObj = {'pnt': pntId,
                 'strtime': startTime.strftime("%d/%m/%Y/%H:%M:%S"),
                 "endtime": endTime.strftime("%d/%m/%Y/%H:%M:%S"),
                 "secs": secs,
                 "type": type}
    try:
        r = requests.get(url=urlStr, params=paramsObj)
        data = json.loads(r.text)
        r.close()
    except:
        # print("Error loading data from scada api")
        data = []
    dataRes = pd.Series([x["dval"] for x in data],
                        index=[dt.datetime.strptime(x["timestamp"], "%Y-%m-%dT%H:%M:%S") for x in data])
    return dataRes

def fetchScadaPntRandHistData(pntId, startTime: dt.datetime, endTime: dt.datetime) -> pd.Series:
    pntId = pntId.strip()
    if pntId == "":
        return pd.Series()
    if startTime > endTime:
        return pd.Series()
    timestamps = pd.date_range(
        startTime, endTime, freq=dt.timedelta(minutes=1)).tolist()
    dataSeries = pd.Series([random.randint(-1000, 1000)
                           for x in timestamps], index=timestamps)
    return dataSeries