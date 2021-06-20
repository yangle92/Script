#!/bin/bash

Njob=15    #任务总数
for ((i=0; i<$Njob; i++)); do
{
          echo  "progress $i is sleeping for 3 seconds zzz…"
          sleep  3
} &
done
wait
echo -e "time-consuming: $SECONDS    seconds"    #显示脚本执行耗时
