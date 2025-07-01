#!/usr/bin/python

# 生成Config命令
from cmdGen import generator

fileName = './CMDLib/ValidTH_250THR_Vopcomp_28'
cfgFileHandle = open(fileName+'.txt')
cfgDat = cfgFileHandle.read()
cfgByte = filter(None,cfgDat.split(' '))
gen = generator(fileName+'.dat')
gen.CommandSend(0x0601);
gen.CommandSend(0x0501);

for byte in cfgByte:
    gen.CommandSend(0x0300+int(byte,16))

gen.CommandSend(0x0500)
gen.CommandSend(0x0800)

gen.fClose()
