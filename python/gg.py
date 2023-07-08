'''
Author: Kinvy-byte 761669072@qq.com
Date: 2023-07-08 14:29:06
LastEditors: Kinvy-byte 761669072@qq.com
LastEditTime: 2023-07-08 14:39:21
FilePath: /kinvy_demo/python/gg.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AElim
'''

line = """
this is LastEditTime LastEditTime LastEditTime LastEditTime LastEditTime,
LastEditTime LastEditTime LastEditTime LastEditTime LastEditTime.
"""

line=line.replace(',','')
line=line.replace('.','')

word = line.split()

freq = []
for i in word:
    freq.append(word.count(i))
    # print(word.count(i))

print(word) 
print(freq)
d=dict(zip(word, freq))

print(d)