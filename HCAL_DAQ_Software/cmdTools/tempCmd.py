#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 生成温度测试命令集
# 每执行一次，会获取一次EBU 16贴点的温度数据
from cmdGen import generator

gen = generator('./CMDLib/tempAcq.dat')
gen.CommandSend(0x1804) # Point at High byte reg in FPGA
gen.CommandSend(0x180e) # write
gen.CommandSend(0x1805) # Point at Low byte reg in FPGA
gen.CommandSend(0x1820) # write
gen.CommandSend(0x1806) # Point at PCA register in FPGA
gen.CommandSend(0x18ff) # Select all channel
gen.CommandSend(0x1803) # Point at Op Register in FPGA
gen.CommandSend(0x1802) # Set Op as write PCA reg
gen.CommandSend(0x1700) # Execute
gen.delay(10)                

gen.CommandSend(0x1801) # Point at TMP reg reg in FPGA
gen.CommandSend(0x1801) # Select configure reg in TMP
gen.CommandSend(0x1803) # Point at Op Reg in FPGA
gen.CommandSend(0x1801) # Write TMP Register

gen.CommandSend(0x1802) # Point at TMP addr reg in FPGA
gen.CommandSend(0x1800) # Select TMP whose addr is 0
gen.CommandSend(0x1700) # Execute
gen.delay(10)

gen.CommandSend(0x1802)
gen.CommandSend(0x1801) # Select TMP whose addr is 1
gen.CommandSend(0x1700) # Let TMP get temp. value
gen.delay(10)
gen.CommandSend(0x1801)
gen.CommandSend(0x1800)
gen.CommandSend(0x1803)
gen.CommandSend(0x1803)
gen.CommandSend(0x1700)
gen.delay(10)


gen.CommandSend(0x1802)
gen.CommandSend(0x1800)
gen.CommandSend(0x1700)
for I2CSwitch_chn in range(8):
    # Connect PCA chn
    gen.CommandSend(0x1806)
    gen.CommandSend(0x1800 + (1 << I2CSwitch_chn))
    gen.CommandSend(0x1803)
    gen.CommandSend(0x1802)
    gen.CommandSend(0x1700)
    gen.delay(10)
    # Prepare to temp. read
    gen.CommandSend(0x1803)
    gen.CommandSend(0x1800)

    for Tmp117Addr in range(2):
        gen.CommandSend(0x1802)
        gen.CommandSend(0x1800 + Tmp117Addr)
        gen.CommandSend(0x1700)
        gen.delay(10)

gen.fClose()
