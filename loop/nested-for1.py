#!/usr/bin/env python
# coding: utf-8

var = int(input("請輸入一數字"))
print ("10827056\t謝昱陞")
cnt = var * 2 - 1
for i in range(1, var + 1):
	string = ""
	string += '-' * (var - i)
	string += str(i) * (i * 2 - 1)
	string += '-' * (var - i)
	print (string)
