### 2.3.3控制流
#### 2.3.3.1 if、elif和else
一个if语句可以接多个elif代码块和一个else代码块，如果所有的elif条件均为False,则执行else代码块：<br>
x = input("PLease enter a number: ")<br>
x = int(x)<br>
if x < 0:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print("It's negative")<br>
elif x == 0:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print('Equal to zero')<br>
elif 0 < x < 5:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print('Positive but smaller than 5')<br>
else:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print('Positive and larger than or equal to 5')<br>
输出结果：<br>
PLease enter a number: 3<br>
Positive but smaller than 5<br>
<br>
条件判断是从左到右的并且在and或or两侧的条件会有“短期”现象：<br>
a = 5; b = 7<br>
c = 8; d = 4<br>
#&nbsp;c>d是不会去判断的，因为第一个比较判断的值为True<br>
if a < b or c > d:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print('Made it')<br>
输出结果：Made it<br>
链式比较也是可以的:
4 > 3 > 2 > 1<br>
输出结果：True<br>
#### 2.3.3.2 for循环
for循环用于遍历一个集合（例如列表或元组）或一个迭代器。标准的for循环语法如下：<br>
for value in collection:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#&nbsp;用值做什么<br>
使用continue关键字可以跳过continue后面的代码进入下一次循环<br>
考虑以下代码，对列表中的非None值进行累加<br>
sequence = [1, 2, None, 4, 5]<br>
total = 0<br>
for value in sequence:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if value == None:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;continue<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;total += value<br>
total<br>
<br>
输出结果：12<br>
使用break关键字可以结束一个for循环<br>
以下代码会对列表元素累加，直到5出现:<br>
sequence = [1, 2, 0, 4, 6, 5, 2, 1]<br>
total_until_5 = 0<br><br>
for value in sequence:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if value == 5:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;break<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;total_until_5 += value<br>
total_until_5<br>
输出结果：13<br>
<br>
break关键字只结束最内层的for循环；最外层的for循环会继续运行:<br>
for i in range(4):<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for j in range(4):<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if j > i:<br>
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;break<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print((i, j))<br>
输出结果：<br>
(0, 0)<br>
(1, 0)<br>
(1, 1)<br>
(2, 0)<br>
(2, 1)<br>
(2, 2)<br>
(3, 0)<br>
(3, 1)<br>
(3, 2)<br>
(3, 3)<br>
如果集合或迭代器中的元素是一个列表（比如元组或列表），它们可以在for循环语句中很方便地通过拆包变为变量：<br>
for a, b, c in iterator:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# &nbsp;做些什么<br>
#### 2.3.3.3  while循环
while循环会在条件符合时一直执行代码块，直到条件判断为False或显示地以break结尾才结束：<br>
x = 256<br>
total = 0<br>
while x > 0:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if total > 500:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;break<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;total += x<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x = x // 2<br>
total<br>
输出结果：504<br>
#### 2.3.3.4 pass
pass就是Python中的“什么都不做”的语句。它用于在代码段中表示不执行任何操作（或者是作为还没有实现的代码占位符）。<br>
x = input('please enter a number: ')<br>
x = eval(x)<br>
if x < 0:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print('negative!')<br>
elif x == 0:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pass<br>
else:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print('positive!')<br>
输出结果：<br>
please enter a number: 999.56<br>
positive!<br>
#### 2.3.2.5 range
range函数返回一个迭代器，该迭代器生成一个等差整数序列：<br>
range(10)<br>
输出结果：range(0, 10)<br>
#nbsp;数字列表<br>
list(range(10))<br>
输出结果：[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]<br>
<br>
起始、结尾、步进（可以是负的）可以传参给range函数<br>
list(range(0, 20, 2))<br>
输出结果：[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]<br>
list(range(5, 0, -1))<br>
输出结果：[5, 4, 3, 2, 1]<br>
<br>
range常用于根据序列的索引遍历序列：<br>
seq = [1, 2, 3, 4]<br>
sum = 0<br>
for i in range(len(seq)):<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;val = seq[i]<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sum += val<br>
sum<br>
输出结果：10<br>
<br>
计算0到99,999中可以被3或5整除的整数相加：<br>
sum = 0<br>
for i in range(100000):<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if i % 3 == 0 or i % 5 == 0:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sum +=i <br>
sum<br>
输出结果：2333316668
#### 2.3.3.6 三元表达式
Python中的三元表达式允许你将一个if-else代码块联合起来，在一行代码或一个语句中生成数据。语法如下：<br>
value = true-expr if condition else false-expr<br>
此处的true-expr和false-expr可以是任意Python表达式，它与以下更详细的代码效果一致：<br>
if condition:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value = true-expr<br>
else:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value = false-expr<br>
以下是具体的示例：<br>
x = 5<br>
'None-negative' if x >= 0 else 'Negative'<br>
输出结果：'None-negative'<br>
