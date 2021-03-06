# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000
Проверить работу скрипта на разных комбинациях сеть/маска.


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
net = input('введите сеть в формате ххх.ххх.ххх.ххх/уу:')
x=net.split('/')
ip=x[0]
mask=x[1]

oct1, oct2, oct3, oct4 = ip.split('.')
z='1'*int(mask)+'0'*(32-int(mask))

print (f'''
Network:
{oct1:<8} {oct2:<8} {oct3:<8} {oct4:<8}
{int(oct1):08b} {int(oct2):08b} {int(oct3):08b} {int(oct4):08b}
Mask:
/{mask}
{int(z[0:8], 2):<8} {int(z[8:16], 2):<8} {int(z[16:24], 2):<8} {int(z[24:32], 2):<8}
{z[0:8]:<8} {z[8:16]:<8} {z[16:24]:<8} {z[24:32]:<8}
''')