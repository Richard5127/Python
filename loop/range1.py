#!/usr/bin/env python
# coding: utf-8

sum = 0
d_var = int(input("請輸入一下限值"))
t_var =	int(input("請輸入一上限值"))
for i in range(d_var, t_var + 1):
	if i %3 == 0:
		sum += i
print ("總和=" + str(sum))
