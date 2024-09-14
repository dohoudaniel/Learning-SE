#!/bin/bash
wget -P /tmp/ https://github.com/dohoudaniel/alx-low_level_programming/raw/master/0x18-dynamic_libraries/libwinning.so
export LD_PRELOAD=/tmp/libwinning.so
