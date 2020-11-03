#!/usr/bin/env python
# coding: utf-8

var = raw_input("請輸入一數字")
num = int(var)
if num < 1000:
	if num > 500:
		print (var + " > 500")
	elif num < 500:
		print (var + " < 500")
	else:
		print (var + " = 500")
else:
	print (var + " >= 1000")
