#!/usr/bin/python
# coding: utf-8

list1 = [ 925, 833, 530, 863, 467, 340, 786, 715, 202, 884, 148, 326, 10, 992, 567, 527, 839, 482, 863, 911, 40, 699, 428, 544, 904, 250, 167, 109, 25, 991, 150, 203, 219, 487, 656, 79, 632, 592, 937, 832, 916, 677, 225, 895, 939, 706, 892, 833, 975 ]
nu = int(input("請輸入一數字"))
print (str(min(list1)) + ',' + str(max(list1)) + ',' + str(sum(list1)) + ',' + str(sum(list1) % nu) + ',' + str(len(list1) * nu))
