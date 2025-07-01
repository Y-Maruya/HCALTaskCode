#!/usr/bin/python

# 生成递增数据，检验FELIX下行数据是否稳定
from cmdGen import generator


gen = generator('./CMDLib/testData.txt')

for i in range(100):
    for num in range(0x100):
        gen.CommandSend(0x0300+(num+1)%0x100)

gen.fClose()
