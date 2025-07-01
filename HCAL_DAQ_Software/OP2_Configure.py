# 1. 将所有芯片配置为外触发模式
# 2. 将FPGA自动触发和外触发通道打开

import CmdConsole
import sys
from time import sleep		

if __name__ == "__main__":
    argvNum = len(sys.argv)
    if(argvNum == 2):
        #配置指定数量芯片
        CmdConsole.sp2eConfig(int(sys.argv[1]),0)
        #等待时间
        sleep(1)
        #打开外触发通道
        CmdConsole.realtimeEnable(int(sys.argv[1]),0b100)
        #产生内部定时触发给到外触发接口
        CmdConsole.internalSyncEnable(int(sys.argv[1]),1,100)
    elif(argvNum == 1):
        #默认32块前端板,同上
        CmdConsole.sp2eConfig(35)
        sleep(1)
        CmdConsole.realtimeEnable(35)
        CmdConsole.internalSyncEnable(35)



