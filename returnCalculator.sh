#!/bin/bash

# inputs a price point and returns 5,10,20 % returns as well as -7% stop loss

investment=$1   # The initial investment amount

# Calculate gains
return1=$(echo "$investment * 0.05 + $investment" | bc)
echo "5% gain is: $return1"

return2=$(echo "$investment * 0.10 + $investment" | bc)
echo "10% gain is: $return2"

return3=$(echo "$investment * 0.20 + $investment" | bc)
echo "20% gain is: $return3"

stopLoss=$(echo "$investment * 0.93" | bc)
echo "Set Stop Loss to: $stopLoss"
