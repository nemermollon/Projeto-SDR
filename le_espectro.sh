#!/bin/bash

gdh="$(date +'%Y%m%d-%H%M')"

# rtl_power -f 80M:100M:25k -g 50 -i 1 -e 10m "$gdh".csv && wait && ./heatmap2.py "$gdh".csv "$gdh".png
# -i 1 => reporta a cada 1 segundo (escreve no arquivo ou na tela)
# -e 10m => encerra após 10 minutos
rtl_power -f 80M:100M:25k -g 50 -i 1 -e 1m "$gdh".csv && wait && ./heatmap2.py "$gdh".csv "$gdh".png

