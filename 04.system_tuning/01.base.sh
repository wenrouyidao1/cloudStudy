#!/usr/bin/env bash

LIMIT="/etc/security/limits.conf"
SYSCTL="/etc/sysctl.conf"

cat <<-EOF >>${LIMIT}
* soft nproc 11000
* hard nproc 11000
* soft nofile 655350
* hard nofile 655350
EOF

cat <<-EOF >>${SYSCTL}
net.ipv4.ip_forward = 0
kernel.msgmnb = 65535
kernel.msgmax = 65535
net.ipv4.tcp_keepalive_time = 30
EOF

sysctl -p