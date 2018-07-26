#!/bin/bash
# vim: set expandtab tabstop=4 shiftwidth=4:

for file in *.dot
do
    echo $file
    basename=$(basename $file .dot)
    dot -Tpng -o $basename.png $file
done
