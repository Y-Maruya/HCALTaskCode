#light calibration every group calib 20s

import CmdConsole2b
import sys
import time
from time import sleep,localtime

if __name__ == "__main__":
    infoSlince = 1
    t = 25
    groupNum = 0
    rgmin = 2000
    dac = rgmin
    #rgmid = 2800
    rgmax = 3500
    step = 100
    rg = list(range(rgmin,rgmax+step,step))#+list(range(rgmid+200,rgmax,200))
    for groupNum in range(6):
        for dac in rg:
            CmdConsole2b.lightCalibSingleGroupCfgGen(groupNum=groupNum,dac=dac,rgmin=rgmin)
