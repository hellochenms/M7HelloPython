import pdb 

需要断点的地方加入下句，常规运行脚本，到断点就会进入debug状态
pdb.set_trace()

debug状态下：
n: 执行下一句
s: 进入函数
c: 前进到下一个断点
p xxx: 打印变量xxx的值
q: 退出脚本
l: 打印附近代码
!xxx = sth: 给xxx变量赋值sth