# -*- coding: UTF-8 -*-

'''
概念介绍

def是可执行的代码。Python的函数是由一个新的语句编写的，即def。不像C这样的编译语言，def是一个可执行的语句——函数并不存在，直到Python运行了def后才存在。
事实上，在if语句、while循环甚至是其他的def中嵌套是合法的（甚至在某些场合还很有效）。
在典型的操作中，def语句在模块文件中编写，并自然而然地在模块文件第一次被导入的时候生成定义的函数。


lambda创建一个对象但将其作为结果返回。也可以用lambda表达式创建函数，这一功能允许我们把函数定义内联到语法上一条def语句不能工作的地方
（这是一个更加高级的概念，我们推迟到第19章介绍）


return将一个结果对象发送给调用者。当函数被调用时，其调用者停止运行直到这个函数完成了它的工作，之后函数才将控制权返回调用者。
函数是通过return语句将计算得到的值传递给调用者的，返回值成为函数调用的结果。


yield向调用者发回一个结果对象，但是记住它离开的地方。像生成器这样的函数也可以通过yield语句来返回值，并挂起它们的状态以便稍后能够恢复状态。
这是本书稍后要介绍的另一个高级话题。


global声明了一个模块级的变量并被赋值。在默认情况下，所有在一个函数中被赋值的对象，是这个函数的本地变量，并且仅在这个函数运行的过程中存在。
为了分配一个可以在整个模块中都可以使用的变量名，函数需要在global语句中将它列举出来。通常情况下，变量名往往需要关注它的作用域（也就是说变量存储的地方），
并且是通过实赋值语句将变量名绑定至作用域的。


nonlocal声明了将要赋值的一个封闭的函数变量。类似的，Python 3.0中添加的nonlocal语句允许一个函数来赋值一条语法封闭的def语句的作用域中已有的名称。
这就允许封闭的函数作为保留状态的一个地方——当一个函数调用的时候，信息被记住了——而不必使用共享的全局名称。


习题
1.编写函数有什么意义？
---函数是Python避免程序代码冗余的最基本方式：把代码分解成函数，意味着未来只有一个运算的代码的拷贝需要更新。
函数是Python中代码重用的基本单位：在函数中包装代码，就使其成为可再利用的工具，可在许多程序中调用它。
最后，函数可让我们把复杂系统分割为可管理的部分，而每一部分都可独立进行开发。

2.什么时候Python将会创建函数？
---当Python运行到并执行def语句时，函数就会被创建。这个语句会创建函数对象，并将其赋值给函数名。
当函数所在模块文件被另一个模块导入时，通常就会发生这种事（回想一下，导入会从头到尾运行文件中的代码，包括任何的def），
但是，当def通过交互模式输入，或者嵌套在其他语句中时（例如，if），也会发生这件事。

3.当一个函数没有return语句时，它将返回什么？
---如果控制流程来到函数主体末尾并没有运行return语句，函数就会传回None对象。这类函数通常是通过表达式语句调用，并将其None结果赋值给变量通常是没有意义的。

4.在函数定义内部的语句什么时候运行？
---函数主体（嵌套在函数定义语句中的代码）在函数稍后通过一个调用表达式调用时就会执行。函数每次被调用，主体都会全新运行一次。

5.检查传入函数的对象类型有什么错误？
---检查传入函数的对象类型，实质上就是破坏函数的灵活性，把函数限制在特定的类型上。没有这类检查时，函数可能处理所有的对象类型：
任何支持函数所预期的接口的对象都能用（接口一词是指函数所执行的一组方法和表达式运算符）。

'''
if __name__ == '__main__':
    pass