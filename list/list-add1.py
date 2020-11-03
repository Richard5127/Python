#!/usr/bin/python
# coding: utf-8

list7 = [ '1', '9', 'N', 'h', 'e' ]
list8 = [ '5', 'V', 'l', '2', 'N', 'I', 'i', 'E' ]
list9 = [ 'b', 'd', 'u', '3' ]
nu = int(input("請輸入一數字"))
if nu > 3:
	list7 += list8
	print (list7)
else:
	print (list9 * nu)
