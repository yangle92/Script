#！/usr/bin/expect

set git /usr/bin/git 
set u "yangle92"
set p "**********"

cd /root/data/Script/


spawn git push -u origin master
expect {
"*Username*"
	{send "$u\r";exp_continue}
"*Password*"
	{send "$p\r"}

}
interact


git commit -m "msg"
git push
