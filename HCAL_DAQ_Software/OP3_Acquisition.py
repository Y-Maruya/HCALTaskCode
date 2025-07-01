# 1. 采集基线3秒
# 2. 电刻度
# need to be init before elecCalib

import CmdConsole2b

rgmin = 50
step1 = 50
rgmid = 400
step2 = 400
rgmax = 1200
dac = rgmin
rg = list(range(rgmin,rgmid,step1))+list(range(rgmid+step2,rgmax,step2))
for chn in range(36):
    #for delayValue in delayRg:
        for dac in rg:
            print("--cfg dac--\n")
            CmdConsole2b.elecSingleChnCfgGen(0,chn,dac,rgmin)
            # sleep(0.5)
            # CmdConsole2b.enterACQ()
            # print("--enter acq--\n")
            # CmdConsole2b.felixShellDo(fdaqCmd+"chn"+str(chn)+"_DAC"+str(dac),infoSlince)
            # CmdConsole2b.quitACQ()
print("--dac buffer shut down--\n")
            
