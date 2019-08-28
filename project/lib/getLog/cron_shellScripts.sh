#/usr/bin/env bash
#
#date: 2019/08/28
#author: cgq
#usage: execute cron task


mkdir /tasks
echo '*/15 * * * *  /usr/bin/bash /tasks/shell_getMessage.sh &' >>/var/spool/cron/root
