#!/bin/python3

# Verificar depois o uso do exec
#exec("rtl_power 80M:100M:50k")

# Formato de saída do CSV
# date, time, Hz low, Hz high, Hz step, samples, dbm, dbm, ...

import subprocess

#test = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE)
#output = test.communicate()[0]

test = subprocess.Popen(["rtl_power", "-f", "80M:100M:50k", "-1", "saida.csv"], stdout=subprocess.PIPE)
output = test.communicate()[0]

res = output.split(b'\n')
for i in res:
	print(i)
