Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> str1='suraj'
>>> str2='chauhan'
>>> print(str1+str2)
surajchauhan
>>> len(str1)
5
>>> len(str2)
7
>>> ch=str([1])
>>> str1='suraj'
>>> ch=str([3])
>>> print(ch)
[3]
>>> str1='suraj'
>>> ch=str[3]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    ch=str[3]
TypeError: 'type' object is not subscriptable
>>> ch=str1[3]
>>> str='suraj'
>>> ch=str[3]
>>> print(ch)
a
>>> print(str[4])
j
>>> print(str[1:4])
ura
>>> print(str[:5])
suraj
