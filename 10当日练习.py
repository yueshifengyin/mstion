# 3、读取一个文本，分别匹配文本中所有的
# *以大写字母开头的单词（包括特殊字符的不算）
# *数字 包括整数，小数，整数，负数，分数，百分数
import re

with open("./123.txt", 'r') as f:
    data = f.read()
regex1 = re.compile(r'[A-Z][a-z]+[a-z]|[A-Z][A-Z]+[a-z]|[A-Z][A-Z]+[A-Z]')
diyi = regex1.findall(data)
print(diyi)

regex2 = re.compile(r'-?\d+.?\d+%?|-?\d+\\?\d+')
dier = regex2.findall(data)
print(dier)