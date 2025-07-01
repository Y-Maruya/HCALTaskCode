#light calibration every group calib 20s

import CmdConsole2b
import sys
import time
from time import sleep,localtime

if __name__ == "__main__":
    infoSlince = 1
    t = 3
    groupNum = 0
    rgmin = 2
    dac = rgmin
    rgmax = 13
    step = 1
    timeRg = list(range(rgmin,rgmax,step))

    fdaqCmd = "fdaq -X -T -t "+str(t)+" /mnt2/ScECAL_CR/data/"+time.strftime("%Y_%m%d",time.localtime())+"/tdcCalib/"+time.strftime("%Y%m%d_%H%M%S",time.localtime())+"delay"+str(rgmin)+"_"+str(step)+"_"+str(rgmax)+"/"
    #CmdConsole2b.cfgECAL('HT',1)
    CmdConsole2b.realtimeEnable(32,0b100)
    CmdConsole2b.sclkFreqSel(32,2)
    CmdConsole2b.tluEn(0)
    #CmdConsole2b.internalSyncEnable(32)
    CmdConsole2b.gbtTrigEn(1)
    CmdConsole2b.unlockVldMod()
    CmdConsole2b.trigGenDelay(1)
    CmdConsole2b.trigSwitch2external(0)

    for delayValue in timeRg:
        CmdConsole2b.trigGenDelay(delayValue)
        sleep(0.1)
        CmdConsole2b.enterACQ()
        CmdConsole2b.felixShellDo(fdaqCmd+"_timeDelay"+str(delayValue),infoSlince)            
        sleep(t+0.1)
        CmdConsole2b.quitACQ()
        sleep(0.1)
    CmdConsole2b.lockVldMod()
    CmdConsole2b.trigSwitch2external(1)
