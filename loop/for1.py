#!/usr/bin/env python
# coding: utf-8

string = ""
var = raw_input("請輸入一字串")
for i in var[1:-2]:
	string += i
	string += '='
print (string + var[-2])
