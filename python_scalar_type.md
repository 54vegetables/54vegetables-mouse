### 2.3.2标量类型
基础的Python数字类型就是int和float。int可以存储任意大小数字：
```
inval = 17239871
inval ** 6
```
*输出结果：26254519291092456596965462913230729701102721*

浮点数在Python中用float表示，每一个浮点数都是双精度64位数值。它们可以用科学计数法表示：<br>
```
fval = 7.243
fval2 = 6.78e-5
```

整数除法会把结果自动转型为浮点数
```
3 / 2
```
*输出结果：1.5*

如果需要C风格的整数除法（去除了非整数结果的小数部分），可以使用整数除法操作符
```
3 // 2
```
*输出结果：1*
***
#### 2.3.2.2字符串
用单引号'或双引号"写一个字符串字面值
```
a = 'one way of writing a string'
b = "another way"
```
含有换行的多行字符串，你可以使用三个单引号'''或三个双引号"""
```
c = """
This is a longer string that
spans multiple lines
"""
```
可以使用count方法来计算c的回车符：
```
c.count('\n')
```
*输出结果：3*<br>
***
**Python的字符串是不可变的，你无法修改一个字符串**
```
a = 'this is a string'
a[10] = 'f'
```
*结果会出现TypeError异常*
```
b = a.replace('string', 'longer string')
b
```
*输出结果：'this is a longer string'*

操作后，变量a就是不可修改的：
```
a
```
*输出结果：'this is a string'*
***
Python对象可以通过str函数转换成字符串：
```
a = 5.6
s = str(a)<br>
s
```
*输出结果：'5.6'*
***
字符串是Unicode字符的序列，因此可以被看作是除了列表和元素的另一种序列：
```
s = 'python'
list(s)
```
*输出结果：['p', 'y', 't', 'h', 'o', 'n']*
**[:3]这种语法被称为切片**，在多种Python序列中都有实现<br>
```
s[:3]
```
*输出结果：'pyt'*
***
反斜杠符号\是一种转义符号，它用来指明特殊符号，比如换行符号\n或Unicode字符。如果要在字符串中写反斜杠则需要将其转义。
```s = '12\\34'
print(s)
```
*输出结果：12\34*
<br>
可以在字符串前面加一个前缀符号r，表明这些字符是原生字符
```
# nbsp;r是raw的缩写，表示原生的
s = r'this \has \no \special \characters'
s
```
*输出结果：'this \\\has \\\no \\\special \\\characters'*
***
将两个字符串结合到一起产生一个新字符串
```
a = 'this is the first half '
b = 'and tjis is the second half'
a + b
```
*输出结果：'this is the first half and tjis is the second half'*
***
字符串对象拥有一个format方法，可以用来代替字符串中的格式化参数，并产生一个新的字符串
```
template = '{0:.2f} {1:s} are worth US${2:d}'
template.format(4.5560, 'Argentine Pesos', 1)
```
*输出结果：'4.56 Argentine Pesos are worth US$1'*
<br>
#### 2.3.2.3字节与Unicode
```
val = "espaol"
type(val)
```
*输出结果：str*
```
val
```
*输出结果：'espa\ue7c8ol'*
<br>
使用encode方法将这个Unicode字符串转换为UTF-8字节：
```
val_utf8 = val.encode('utf-8')
type(val_utf8)
```
*输出结果：bytes*
```
val_utf8
```
*输出结果：b'espa\xee\x9f\x88ol'*
<br>
使用decode方法进行解码
```
print(val_utf8.decode('utf-8'))
```
*输出结果：espaol*
<br>
在字节对象中我们并不想让所有的数据都隐式地解码为Unicode字符串,可以在字符串前加前缀b来定义字符文本，尽管可能很少这么做：
```
bytes_val = b'this is bytes'
bytes_val
```
*输出结果：b'this is bytes'*
```
decoded = bytes_val.decode('utf-8')
decoded
```
*输出结果：'this is bytes'*
<br>
#### 2.3.2.4  布尔值
Python中的布尔值写作True或False。比较运算符和其他条件表达式的结果为True或False。布尔值可以与and和or关键字合用。<br>
True and True<br>
输出结果：True<br>
False or True<br>
输出结果：True<br>
<br>
#### 2.3.2.5类型转换
str、bool、int和float既是数据类型，同时也是可以将其他数据转换为这些类型的函数：<br>
s = '3.14159'<br>
fval = float(s)<br>
type(fval)<br>
输出结果：float<br>
int(fval)<br>
输出结果：3<br>
bool(fval)<br>
输出结果：True<br>
bool(0)<br>
输出结果：False<br>
<br>
#### 2.3.2.6  None
None是Python的null值类型。如果一个函数没有显示地返回值，则它会隐式地返回None:<br>
a = None<br>
a is None<br>
输出结果：True<br>
b = 5<br>
b is not None<br>
输出结果：True<br>
None还可以作为一个常用的函数参加默认值：<br>
def add_and_maybe_multiply(a, b, c=None):<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result = a + b<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if c is not None:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result = result * c<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return result<br>
result = add_and_maybe_multiply(1, 2)<br>
result<br>
输出结果：3<br>
result = add_and_maybe_multiply(1, 2, 3)<br>
result<br>
输出结果：9<br>
从技术角度来说，None不仅是一个关键字，它还是NoneType类型的唯一实例：<br>
type(None)<br>
输出结果：NoneType<br>
#### 2.3.2.7  日期和时间
Python中内建的datetime模块，提供了datetime、data和time类型。<br>
from datetime import datetime, date, time<br>
<br>
dt = datetime(2011, 10, 29, 20, 30, 21)<br>
dt.year<br>
输出结果：2011<br>
dt.month<br>
输出结果：10<br>
dt.day<br>
输出结果：29<br>
dt.hour<br>
输出结果：20<br>
dt.minute<br>
输出结果：30<br>
dt.second<br>
输出结果：21<br>
<br>
对于datetime实例，可以分别使用date和time方法获取它的date和time对象<br>
dt.date()<br>
输出结果：datetime.date(2011, 10, 29)<br>
dt.time()<br>
输出结果：datetime.time(20, 30, 21)<br>
<br>
strftime将对象转换为字符串<br>
dt.strftime('%m/%d/%Y %H:%M')<br>
输出结果：'10/29/2011 20:30'<br>
strptime将字符串转换为对象<br>
dt.strptime('20091031', '%Y%m%d')<br>
输出结果：datetime.datetime(2009, 10, 31, 0, 0)<br>
