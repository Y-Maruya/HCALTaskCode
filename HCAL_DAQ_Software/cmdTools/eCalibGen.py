#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 生成温度测试命令集
# 每执行一次，会获取一次EBU 16贴点的温度数据
from cmdGen import generator
from cmdGen import probeMod

gen = generator('./CMDLib/eCalib.dat')
gen.CommandSend(0x127f) # enable all chip, and make amplifier active. Accept external trigger

# 选择Probe寄存器
gen.CommandSend(0x0600)


probe = probeMod() # 控制Probe bit数据的生成
# 最外侧循环为通道选择
for chn in range(36):

    gen.CommandSend(0x0501) #将数据通道指向FPGA内部SC/Probe模块
    probe.setChn(chn)
    cfgByte = probe.formatOutput()
    gen.CommandSend(0x0300+cfgByte) #传输数据
    gen.CommandSend(0x0500) #关闭传输通道

    gen.CommandSend(0x0800) #开始向ASIC配置Probe

    #下面对DAC进行循环
    #发现不能直接生成命令，需要制定指出dac范围，此代码作废
    pass
