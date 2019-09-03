#!/usr/bin/env bash
#
# date: 2019/09/02
# usage: transfer public key


if [ ! -f /usr/bin/expect ];then
  yum -y install expect
fi

# ssh-keygen: create public key
if [ ! -f ${HOME}/.ssh/id_rsa ];then
  ssh-keygen -t rsa -f ${HOME}/.ssh/id_rsa -q -N ""
fi

# ssh-copy-id: transfer id_rsa.pub to remote webserver
user="root"
password="1"
for ipaddress in $(cat ips.txt);do
  {
  /usr/bin/expect <<-EOF
  spawn ssh-copy-id ${user}@${ipaddress}
  expect "*yes/no*" { send "yes\r" }
  expect "*password*" { send "${password}\r" }
  expect eof
EOF
  }&
done
wait

echo "OK"
