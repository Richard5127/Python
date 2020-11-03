#!/usr/bin/env python
# coding: utf-8

var = 0
sum = 0
cnt = 1
string = ""
var = int(raw_input("請輸入一數字"))
while cnt <= var:
	string += str(cnt)
	if cnt != var:
		string += '+'
	sum += cnt
	cnt += 1
print (string + '=' + str(sum))
