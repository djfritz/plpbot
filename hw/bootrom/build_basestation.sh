#!/bin/sh

tar -xf ../../sw/firmware/plpbot_basestation.plp plp.hex
python ../scripts/plpromgen.py plp.hex
cp inferred_rom.v ../verilog
