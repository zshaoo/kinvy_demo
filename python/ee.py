'''
Author: Kinvy-byte 761669072@qq.com
Date: 2023-07-07 16:45:12
LastEditors: Kinvy-byte 761669072@qq.com
LastEditTime: 2023-07-07 16:57:36
FilePath: /kinvy_demo/python/ee.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
##

i = 100
x = 0
y = 0
z = 0

# 345
while i < 1000:
    x=i//100 
    y=(i%100)//10
    z=(i%100)%10

    if (i == y**3 + x**3 + z**3):
        print(i)

    i+=1