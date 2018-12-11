print(1+3+4+3)
print('3s')
print("3s")
print('ss','s')
print('ss'+'s')
print("'3'")
print('"3"')
print(3)
print(3,'ss')
print(3+'ss')


'''
Output：
11
3s
3s
ss s
sss
'3'
"3"
3
3 ss
Traceback (most recent call last):
  File "print.py", line 10, in <module>
    print(3+'ss')
TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''
