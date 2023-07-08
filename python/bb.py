'''
Author: Kinvy-byte 761669072@qq.com
Date: 2023-07-07 16:00:39
LastEditors: Kinvy-byte 761669072@qq.com
LastEditTime: 2023-07-07 16:06:16
FilePath: /kinvy_demo/python/bb.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# coding=UTF-8

score = int(input("0-100"))

# if score >= 85:
#     print("A")
if score < 85 and score >= 60:
    print("B")
else:
    print("C")