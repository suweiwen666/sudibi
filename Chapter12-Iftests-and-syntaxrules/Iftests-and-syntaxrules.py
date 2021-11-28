# -*- coding: UTF-8 -*-
'''
本章介绍语法规则

1.在Python中怎样编写多路分支？
---if语句加多个elif分句通常是编写多路分支的最直接的方式，不过也许并不是最简明的。
字典索引运算通常也能实现相同的结果，尤其是字典包含def语句或lambda表达式所写成的可调用函数。

2.在Python中怎样把if/else语句写成表达式？
---在Python 2.5中，表达式形式Y if X else Z在X为真时会返回Y，否则，返回Z。这相当于4行if语句。
and/or组合（（X and Y） or Z）也以相同方式工作，但更难懂，而且要求Y为真。

3.怎样使单个语句横跨多行？
---把语句包裹在语法括号当中（（）、[]、或{}），这样就可以按照需要横跨多行；当Python看见闭合括号时，语句就会结束，该语句之外的第2行可以以任意缩进层级开始。

4.True和False这两个字代表了什么意义？
---True和False只不过分别是整数1和0的特殊版本而已。它们代表的就是Python中的布尔真假值。它们可以用来进行真测试、变量初始化，以及在交互提示模式中打印表达式结果。

'''

if __name__ == '__main__':
    pass