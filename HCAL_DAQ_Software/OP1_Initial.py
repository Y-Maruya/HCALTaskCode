

# 将GBT1,3的除了测试通道的Elink全部打开
# 8b/10b 和TH FH等要手动配置

import CmdConsole


if __name__ == "__main__":
    # 将GBT Link0 和GBT Link2 配置为时钟通道
    CmdConsole.FEC_clockInit([0,2])

    # 将GBT Link1 和GBT Link3 配置为数据通道
    CmdConsole.FEC_dataInit([1,3])

    # Encoding方式自动配置代码尚未开发，暂由GUI操作完成
