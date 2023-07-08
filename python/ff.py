'''
Author: Kinvy-byte 761669072@qq.com
Date: 2023-07-08 13:40:46
LastEditors: Kinvy-byte 761669072@qq.com
LastEditTime: 2023-07-08 13:44:40
FilePath: /kinvy_demo/python/ff.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE =
'''
##

d = {101:'zhangsan', 102:'lisi', 103:'wangwu'}
# i = 0
for i in d.keys():
    print("i = " + str(i))

for i in d.values():
    print("i = " + str(i))

for i, j in d.items():
    print("i = " + str(i) + ",j = " + str(j))