#!/bin/sh

#generates the plpbot hardware from the reference PLP source and the plpbot patch
#requires mercurial and the xilinx webpack with the xilinx settings sourced

hg clone https://progressive-learning-platform.googlecode.com/hg plpbot_hw
cd plpbot_hw
patch -p1 ../plpbot.patch

cd reference/plp-2.2/hw
sh scripts/build_1200k_linux.sh


