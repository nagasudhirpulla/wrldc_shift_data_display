from dataclasses import dataclass, field
from src.config.appConfig import getAppConfig
from src.services.scadaFetcher import fetchScadaPntHistData
import datetime as dt
import numpy as np


@dataclass
class ShiftData:
    maxFreq: float
    maxFreqTime: dt.datetime
    minFreq: float
    minFreqTime: dt.datetime
    avgFreq: float
    maxDem: float
    maxDemTime: dt.datetime
    minDem: float
    minDemTime: dt.datetime

    wrErExportMin: float
    wrErExportMax: float
    wrSrExportMin: float
    wrSrExportMax: float
    wrNrExportMin: float
    wrNrExportMax: float
    wrIrExportMin: float
    wrIrExportMax: float

    wrErImportMin: float
    wrErImportMax: float
    wrSrImportMin: float
    wrSrImportMax: float
    wrNrImportMin: float
    wrNrImportMax: float
    wrIrImportMin: float
    wrIrImportMax: float


def checkNan(x):
    if np.isnan(x):
        return ""
    else:
        return x


def getShiftData(startDt: dt.datetime, endDt: dt.datetime) -> ShiftData:
    appConf = getAppConfig()

    # get demand stats
    demPnt = appConf.demPnt
    demData = fetchScadaPntHistData(demPnt, startDt, endDt, secs=1).astype(int)
    maxDem = demData.max()
    minDem = demData.min()
    maxDemTime = demData.idxmax().strftime("%H:%M")
    minDemTime = demData.idxmin().strftime("%H:%M")

    # get freq stats
    freqPnt = appConf.freqPnt
    freqData = fetchScadaPntHistData(freqPnt, startDt, endDt, secs=1)
    maxFreq = freqData.max().round(3)
    minFreq = freqData.min().round(2)
    maxFreqTime = freqData.idxmax().strftime("%H:%M")
    minFreqTime = freqData.idxmin().strftime("%H:%M")
    avgFreq = freqData.mean().round(2)

    # WR-SR stats
    wrSrPnt = appConf.wrSrPnt
    wrSrData = fetchScadaPntHistData(
        wrSrPnt, startDt, endDt, secs=1).astype(int)
    wrSrExportData = wrSrData[wrSrData < 0]
    wrSrImportData = wrSrData[wrSrData > 0]
    wrSrExportMin = wrSrExportData.max()
    wrSrExportMax = wrSrExportData.min()
    wrSrImportMin = wrSrImportData.min()
    wrSrImportMax = wrSrImportData.max()

    # WR-NR stats
    wrNrPnt = appConf.wrNrPnt
    wrNrData = fetchScadaPntHistData(
        wrNrPnt, startDt, endDt, secs=1).astype(int)
    wrNrExportData = wrNrData[wrNrData < 0]
    wrNrImportData = wrNrData[wrNrData > 0]
    wrNrExportMin = wrNrExportData.max()
    wrNrExportMax = wrNrExportData.min()
    wrNrImportMin = wrNrImportData.min()
    wrNrImportMax = wrNrImportData.max()

    # WR-ER stats
    wrErPnt = appConf.wrErPnt
    wrErData = fetchScadaPntHistData(
        wrErPnt, startDt, endDt, secs=1).astype(int)
    wrErExportData = wrErData[wrErData < 0]
    wrErImportData = wrErData[wrErData > 0]
    wrErExportMin = wrErExportData.max()
    wrErExportMax = wrErExportData.min()
    wrErImportMin = wrErImportData.min()
    wrErImportMax = wrErImportData.max()

    # WR-IR stats
    wrIrPnt = appConf.wrIrPnt
    wrIrData = fetchScadaPntHistData(
        wrIrPnt, startDt, endDt, secs=1).astype(int)
    wrIrExportData = wrIrData[wrIrData < 0]
    wrIrImportData = wrIrData[wrIrData > 0]
    wrIrExportMin = wrIrExportData.max()
    wrIrExportMax = wrIrExportData.min()
    wrIrImportMin = wrIrImportData.min()
    wrIrImportMax = wrIrImportData.max()

    shiftData: ShiftData = ShiftData(
        maxFreq=maxFreq,
        maxFreqTime=maxFreqTime,
        minFreq=minFreq,
        minFreqTime=minFreqTime,
        avgFreq=avgFreq,
        maxDem=maxDem,
        maxDemTime=maxDemTime,
        minDem=minDem,
        minDemTime=minDemTime,
        wrErExportMin=checkNan(wrErExportMin),
        wrErExportMax=checkNan(wrErExportMax),
        wrSrExportMin=checkNan(wrSrExportMin),
        wrSrExportMax=checkNan(wrSrExportMax),
        wrNrExportMin=checkNan(wrNrExportMin),
        wrNrExportMax=checkNan(wrNrExportMax),
        wrIrExportMin=checkNan(wrIrExportMin),
        wrIrExportMax=checkNan(wrIrExportMax),
        wrErImportMin=checkNan(wrErImportMin),
        wrErImportMax=checkNan(wrErImportMax),
        wrSrImportMin=checkNan(wrSrImportMin),
        wrSrImportMax=checkNan(wrSrImportMax),
        wrNrImportMin=checkNan(wrNrImportMin),
        wrNrImportMax=checkNan(wrNrImportMax),
        wrIrImportMin=checkNan(wrIrImportMin),
        wrIrImportMax=checkNan(wrIrImportMax)
    )
    return shiftData
