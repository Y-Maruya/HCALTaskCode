import CmdConsole2b
import sys
import time
from time import sleep,localtime

if __name__=="__main__":
    acqTime = 180
    currentTime = time.localtime()
    fdaqCmd = "fdaq -X -T -t " + str(acqTime) + " /mnt2/ScECAL_CR/data/DRCosmicRayTst/" + time.strftime("%Y%m%d_%H%M%S",time.localtime()) + "/tst"
   
    i = 1
    def acq():
        CmdConsole2b.enterACQ()
        CmdConsole2b.felixShellDo(fdaqCmd)
        CmdConsole2b.quitACQ()

    #while i < 5:
        #if currentTime.tm_hour == 16 & currentTime.tm_min == 42:
        #    print("--startAcq--\n")
        #    i = i + 1
    acq()
    
    print("--autoAcqStop--\n")
        
