1、将目标python文件（本例中hello.py）所在目录（本例中/Users/xxxxxx/m2pythonbin）加入环境变量PATH中：
在用户目录下(cd ~)，打开或新建.profile文件，<br/>
加入一行export PATH=$PATH:/Users/xxxxxx/m2pythonbin

2、给想执行的python文件增加执行权限<br/>
例：chmod u+x hello.py (u:文件所有者，+:增加，x:执行权限；a+x则对所有用户增加执行权限)

3、直接在terminal终端中，如下述方式执行<br/>
例：hello.py

4、注意：直接执行的python文件，需要指定执行程序，<br/>
比如在第一行为#!/usr/bin/python