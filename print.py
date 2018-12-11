# 这是一个注释

# 用print()在括号中加上字符串
# You can use single quotes or double quotes, but they need to be used together.
print('3s')
print("3s")
'''
Output:
3s
3s
'''
# print()也可以打印整数，或者计算结果
print(3)
print(1+3+4+3)
'''
Output:
3
11
'''

# 输出引号：
# You can either put double quotes inside single quotes,
# singles inside doubles,
# or use the "\" backslash.
print("'3'")
print('"3"')
print('you\'ll have success here')
print("you'll have success here too")

'''
Output:
'3'
"3"
you'll have success here
you'll have success here too
'''

# print()函数也可以接受多个字符串
# 用逗号“,”隔开，就可以连成一串输出；遇到逗号“,”会输出一个空格
# 或者使用"+", 没空格. You will need to add one if you wanted.
print('ss','s')
print('ss'+'s')
'''
Output:
ss s
sss
'''

# If you use the "+" to join integers and floats together, then you will perform an arithmetic operation. If you use the ",", then it will print them out separately, with a space.
# ”+“连接整数和小数，输出计算结果
# “，”连接他们，分别输出，不计算
print(3+0.5)
print(3,0.5)
'''
Output:
3.5
3 0.5
'''

# You cannot use the "+" to join strings with ints or floats, you must use the ",".
# 只能用“，”连接数字和string，有空格
# 用“+”报错
print(3,'ss')
print(3+'ss')
'''
Output:
3 ss
Traceback (most recent call last):
  File "print.py", line 10, in <module>
    print(3+'ss')
TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''
