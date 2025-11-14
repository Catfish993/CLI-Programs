#!/bin/bash

# This CLI tool allows you to convert currency and return the gold amount with appropriate weight
#1 platinum piece (pp)= 5 gold pieces (gp)
#
#1 gold piece (gp)= 10 silver pieces (sp)
#
#1 electrum piece (ep)= 5 silver pieces (sp)
#
#1 silver piece (sp)= 10 copper pieces (cp)

amount=$1  
currencyType=$2  

if [[ $currencyType == "gp" ]]; then
    total=$amount
elif [[ $currencyType == "sp" ]]; then
    total=$(echo "$amount * 0.1" | bc) 
elif [[ $currencyType == "ep" ]]; then
    total=$(echo "$amount * 0.2" | bc) 
elif [[ $currencyType == "pp" ]]; then
    total=$(echo "$amount * 5" | bc)   
elif [[ $currencyType == "cp" ]]; then
    total=$(echo "$amount * 0.01" | bc)
else
    echo "Invalid currency type. Please use gp, sp, ep, pp, or cp."
    exit 1
fi

# Output the conversion result
echo "$amount $currencyType = $total GP"
