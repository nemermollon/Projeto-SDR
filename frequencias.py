#!/bin/python3

# Verificar depois o uso do exec
#exec("rtl_power 80M:100M:50k")

# Formato de saída do CSV
# date, time, Hz low, Hz high, Hz step, samples, dbm, dbm, ...

import subprocess

#test = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE)
#output = test.communicate()[0]

# Uso
# rtl_power -f 80M:100M:25k -g 50 -i 10 -e 10m 1.csv && wait && ./heatmap2.py 1.csv 1.png

# gdh=$(date +"%Y%m%d-%H%M")
# rtl_power -f 80M:100M:25k -g 50 -i 1 -e 10m "$gdh".csv && wait && ./heatmap2.py "$gdh".csv "$gdh".png
# -i 1 => reporta a cada 1 segundo (escreve no arquivo ou na tela)
# -e 10m => encerra após 10 minutos

test = subprocess.Popen(["rtl_power", "-f", "80M:100M:50k", "-1", "saida.csv"], stdout=subprocess.PIPE)
output = test.communicate()[0]

res = output.split(b'\n')
for i in res:
	print(i)
