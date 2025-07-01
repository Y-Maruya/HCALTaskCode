#light calibration every group calib 20s

import CmdConsole2b
import sys
import time
from time import sleep,localtime

if __name__ == "__main__":
    infoSlince = 1
    t = 5
    groupNum = 0
    rgmin = 1600
    dac = rgmin
    #rgmid = 2800
    rgmax = 2000
    step = 20
    #dacRg = list(range(rgmin,rgmax,step))#+list(range(rgmid+200,rgmax,200))
    dacRg = [2600]

    trigDelayMin = 100
    trigDelayMax = 120
    delayStep = 2
    delayRg = list(range(trigDelayMin,trigDelayMax+delayStep,delayStep))

    fdaqCmd = "fdaq -X -T -t "+str(t)+" /mnt2/ScECAL_CR/data/"+time.strftime("%Y_%m%d",time.localtime())+"/lightCalib/"+time.strftime("%Y%m%d_%H%M%S",time.localtime())+"_Group0"+"_trigDelay"+str(trigDelayMin)+"_"+str(delayStep)+"_"+str(trigDelayMax)+"/"
    #CmdConsole2b.cfgECAL('HL',1)
    CmdConsole2b.realtimeEnable(32,0b100)
    CmdConsole2b.sclkFreqSel(32,0)
    CmdConsole2b.cfgECALHV()
    CmdConsole2b.tluEn(0)
    CmdConsole2b.internalSyncEnable(32)
    CmdConsole2b.gbtTrigEn(0)

    for groupNum in range(1):
        for dac in dacRg:
            for trigDelay in delayRg:
                CmdConsole2b.lightCalibSingleGroup(32,groupNum,dac,0)
                CmdConsole2b.cfgECALwithTrigDelay(1,trigDelay,'HL',1)
                sleep(0.1)
                CmdConsole2b.enterACQ()
                CmdConsole2b.felixShellDo(fdaqCmd+"group"+str(groupNum)+"_DAC"+str(dac)+"_TrigDelay" + str(trigDelay),infoSlince)            
                sleep(t+0.1)
                CmdConsole2b.quitACQ()
                sleep(0.1)
    CmdConsole2b.lightCalibSingleGroup(32,0,0,1)
    CmdConsole2b.sclkFreqSel(32,2)
    CmdConsole2b.hvSet(32,0,40)
