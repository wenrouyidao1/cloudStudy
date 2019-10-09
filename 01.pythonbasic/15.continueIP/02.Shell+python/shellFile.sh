#/usr/bin/env bash

netip="10.36.145"
for hostip in $(seq 2 254); do
{
        ping -c1 -s0.5 ${netip}.${hostip} &>/dev/null
        if [ $? -eq 0 ];then
                echo ${netip}.${hostip} >>onlineComputer.txt
        fi
}&
done
wait
echo "complete"