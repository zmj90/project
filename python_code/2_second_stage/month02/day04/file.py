"""
os模块处理文件
"""

import  os

print(os.path.getsize('my.log')) # 获取文件大小

print(os.listdir('.'))  # 查看一个目录中有什么文件

print(os.path.exists('abc'))  # 查看一个文件是否存在

print(os.path.isfile('my.log'))  # 查看文件是否为普通文件

os.remove('my.log') # 删除一个文件
