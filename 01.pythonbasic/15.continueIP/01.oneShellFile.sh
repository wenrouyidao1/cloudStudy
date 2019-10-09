#!/usr/bin/env bash
# 缺点：一个一个ping主机，不能放在后台，慢

#循环ping主机，ping通则写入online文件，ping失败则跳出循环，进入下一次循环
netip="10.36.145"
n=2
while ((${n}<255)); do
  for hostip in $(seq ${n} 254); do
    ping -c1 -s0.5 ${netip}.${hostip} &>/dev/null
    if [ $? -eq 0 ]; then
      echo "${netip}.${hostip}" >>online${n}.txt
    else
      n=${hostip}
      break
    fi
  done
  let n++
done

#过滤只有一个ip地址的文件
for file in $(ls online*); do
{
  num=$(cat ${file} | wc -l)
  if [ ${num} -eq 1 ]; then
    rm -rf ${file}
  fi
}&
done
wait
echo "complete"