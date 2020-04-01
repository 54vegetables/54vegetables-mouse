## 2.3  Python语言基础
<b>使用IPython或Jupyter notebook运行。</b>
### 2.3.1  语言语义
Python语言的设计非常独特，它侧重于可读性、易用性及清晰性。

#### 2.3.1.1  缩进，而不是大括号
Python使用缩进（tab或者空格）来组织代码，而不是像其他语言比如R、C++、Java和Perl那样用大括号。
排序算法：<br>
 for x in array:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if x < pivot:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;less.append(x)<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;else:<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;greater.append(x)<br>
一个冒号代表一个缩进代码块的开始，单个代码块中所有的代码必须保持相同的缩进，直到代码块结束。

#### 2.3.1.2  一切皆为对象
Python语言的一个重要特征就是对象模型的一致性。每一个数值、字符串、数据结构、函数、类、模块以及所有存在于Python解释器中的事物，都是Python对象。每个对象都会关联到一种类型（例如字符串、函数）和内部数据。在实践中，一切皆为对象使得语言非常灵活，甚至函数也可以被当作对象来操作。

#### 2.3.1.3  注释
所有写在#号之后的文本会自动被Python解释器忽略。<br>
results = []<br>
for line in file_handel:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#&nbsp;当前保持行为空<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#&nbsp;if len(line)  ==  0:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#&nbsp;则继续<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;results.append(line.replace('foo', 'bar'))<br>
注释也可以写在一行被执行代码的后面。<br>
 print("Reached this line")    #&nbsp;简单的状态报告

#### 2.3.1.4  函数和对象方法的调用
调用函数时，向函数括号里传递0或多个参数，通常会把返回值赋值给一个变量：<br>
result = f(x, y, z)<br>
g()<br>
几乎所有的Python对象都有内部函数，称为方法，可以访问到对象内部的内容。你可以通过以下语法调用它们：<br>
obj.some_method(x, y, z)<br>
函数传参既可以是位置参数也可以是关键字参数：<br>
result = f(a, b, c, d=5, e='foo')

#### 2.3.1.5  变量和参数传递
在Python中对一个变量（或者变量名）赋值时，你就创建了一个指向等号右边对象的引用。<br>
a = [1, 2, 3]<br>
#&nbsp;将a赋值给一个新的变量b<br>
b = a<br>
a.append(4)<br>
b<br>
输出结果：[1, 2, 3, 4]<br>
<b>注意：赋值也被称为绑定。这是因为我们将一个变量名绑定到了一个对象上。已被赋值的变量名有时也会被称为被绑定变量。</b><br>
def append_element(some_list, element):<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;some_list.append(element)<br>

data = [1, 2, 3]<br>
append_element(data, 4)<br>
data<br>
输出结果：[1, 2, 3, 4]

#### 2.3.1.6  动态引用、强类型
Python中的对象引用并不涉及类型。以下操作是没有问题的：<br>
a = 5<br>
type(a)<br>
输出结果：int<br>
a = 'foo'<br>
type(a)<br>
输出结果：str<br>
<br>
<b>Python被认为是强类型语言，这意味着所有的对象都拥有一个指定的类型（或类）。</b>
隐式的转换只在某些特定、明显的情况下发生：<br>
a = 4.5<br>
b = 2<br>
#&nbsp;字符串格式化，用于后面访问<br>
print('a is {0}, b is {1}'.format(type(a), type(b)))<br>
输出结果：a is <class 'float'>, b is <class 'int'>
<br>
a / b<br>
输出结果：2.25<br>

使用isinstance函数来检查一个对象是否是特定类型的实例<br>
a = 5<br>
isinstance(a, int)<br>
输出结果：True<br>

isinstance接受一个包含类型的元组，检查对象的类型是否在元组中的类型中<br>
a = 5; b = 4.5<br>
isinstance(a, (int, float))<br>
输出结果：True<br>

isinstance(b, (int, float))<br>
输出结果：True

#### 2.3.1.7属性和方法
Python中的对象通常都会有属性和方法。属性和方法都可以通过形如obj.attribute_name的语法进行调用<br>
a = 'foo'<br>
a.<Tab><br>
属性和方法也可以通过getattr函数获得<br>
getattr(a, 'split')<br>
输出结果：<function str.split(sep=None, maxsplit=-1)<br>

#### 2.3.1.8鸭子类型
def isiterable(obj):<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;try:&nbsp;&nbsp;#&nbsp;可遍历<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;iter(obj)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return True<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;except TypeError:  # 不可遍历<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return False<br>

isiterable('a string')<br>
输出结果：True<br>
isiterable([1, 2, 3])<br>
输出结果：True<br>
isiterable(5)<br>
输出结果：False<br>

检查对象是否是一个列表（或者一个Numpy数组），如果不是就把它转换为列表：<br>
def isiterable(obj):<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;try:&nbsp;&nbsp;#&nbsp;可遍历<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;iter(obj)<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return True<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;except TypeError:  #&nbsp;不可遍历<br>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; False<br>
x = 'a string'<br>
#&nbsp;如果x不是列表类型，并且x可遍历，就将x转换为列表<br>
if not isinstance(x, list) and isiterable(x):<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;try:&nbsp;&nbsp;x = list(x)<br>
x<br>
输出结果：['a', ' ', 's', 't', 'r', 'i', 'n', 'g']

#### 2.3.1.9导入
在Python中，模块就是以.py为后缀名并包含Python代码的文件。假设有以下模块：<br>
PI = 3.14159<br>
def f(x):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return x + 2<br>
def g(a, b):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return a + b<br>
假设向从另一个相同路径下的文件连接到some_module.py中定义的变量和函数，有以下三种方法：<br>
method1：直接导入模块<br>
import some_module<br>
result = some_module.f(5)<br>
result<br>
输出结果：7<br>
pi = some_module.PI<br>
pi<br>
输出结果：3.14159<br>
<br>
method2:导入模块中的函数和变量<br>
from some_module import f, g, PI<br>

result = g(5, PI)<br>
result<br>
输出结果：8.14159<br>
<br>
method3:通过使用as关键字，可以对导入内容给予不同的变量名：<br>
import some_module as sm<br>
from some_module import g as gf, PI as pi<br>
<br>
r1 = sm.f(pi)<br>
r1<br>
输出结果：5.14159<br>
<br>
r2 = gf(6, pi)<br>
r2<br>
输出结果：9.14159<br>
#### 2.3.1.10二元运算符和比较运算符
检查两个引用是否指向同一个对象，可以使用is关键字。is not 在检查两个对象不是相同对象时也是有效的。<br>
a = [1, 2, 3]<br>
b = a<br>
c = list(a)<br>
a is b<br>
输出结果：True<br>
<br>
list函数总是创建一个新的Python列表（即一份拷贝），我们可以确定c与a是不同的。<br>
a is not c<br>
输出结果：True<br>
<br>
is和==是不同的，它比较的是里面的值<br>
a == c<br>
输出结果：True<br>
<br>
is和is not的常用之处是检查一个变量是否为None，因为None只有一个实例：<br>
a = None<br>
a is None<br>
输出结果：True<br>

#### 2.3.1.11  可变对象和不可变对象
列表、字典、NumPy数组都是可变对象，大多数用户定义的类型（类）也是可变的。可变对象中包含的对象和值是可以被修改的：<br>
a_list = ['foo', 2, [4, 5]]<br>
a_list[2] = (3, 4)<br>
a_list<br>
输出结果：['foo', 2, (3, 4)]<br>
<b>还有其他一些对象是不可变的，比如字符串、元组</b>

