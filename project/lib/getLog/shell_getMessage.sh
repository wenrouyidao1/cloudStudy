#/usr/bin/env bash
#
#date: 2019/08/28
#author: cgq
#usage: get system information


Date=$(date +%Y%m%d%H%M%S)
Hostname=$(hostname)

if [ ! which vmstat &>/dev/null ]; then
        yum -y install procps-ng &>/dev/null
        if [ $? -eq 0 ];then
                echo "vmstat already installed"
        fi
fi
if [ ! which bc &>/dev/null ]; then
        yum -y install bc &>/dev/null
        if [ $? -eq 0 ];then
                echo "bc already installed"
        fi
fi

US=$(vmstat | awk 'NR==3{ print $13 }')
SY=$(vmstat | awk 'NR==3{ print $14 }')
IDLE=$(vmstat | awk 'NR==3{ print $15 }')

TOTAL=$(free -mw | awk 'NR==2{ print $2 }')
USE=$(free -mw | awk 'NR==2{ print $3 }')
FREE=$(free -mw | awk 'NR==2{ print $4 }')
CACHE=$(free -mw | awk 'NR==2{ print $7 }')
memoryRate=$(echo "((${USE}+${CACHE})/${TOTAL})*100" | bc -ql)

disk_useRate=$(df -Th | awk 'NR==2{ print $6 }')
diskRate=${disk_useRate:0:2}

if [ ! -e /var/log/monitor/monitor.log ];then
    mkdir /var/log/monitor
    touch /var/log/monitor/monitor.log
fi
fileSize=$(du -sh /var/log/monitor/monitor.log | awk '{ print $1 }')
if [ "${fileSize}" == "2.1M" ];then
    mv /var/log/monitor/monitor.{log,log.bak-${Date}}
else
    echo "\"${Date}\" - \"${Hostname}\" - {\"cpu\": {\"user\": ${US}, \"system\": ${SY}, \"idle\": ${IDLE}}, \"memory\": {\"total\": ${TOTAL}, \"free\": ${FREE}, \"useRate\": ${memoryRate}}, \"disk\": {\"useRate\": ${diskRate}}}" >>/var/log/monitor/monitor.log
fi
