import json
import pickle

# 序列化（serialization）是将对象的状态信息转换为可以存储或传输的形式过程。
# 在python中，序列化通常意味着将对象转换为字节流，JSON字符串或者其它可以持久化存储或通过网络传输的格式。
# 反序列化（Deserialization）则是相反的过程，即将序列化的数据还原成对象。
# 序列化主要目的是：
# 1.持久化：将对象的状态保存到磁盘上，以便以后可以恢复。
# 2.数据交换：将对象的状态转换为可传输的格式，以便通过网络发送给其它系统或服务。
# 3.简化数据处理：将复杂的数据结构转换为简单的文本格式，便于处理或与其它系统交互。

# python中的序列化方法
# JSON序列化
# JSON（JavaScript Object Notaion）是一种轻量级数据交换格式，易于人阅读和编写，同时也易于机器解析和生成。Python内置了JSON模块来处理JSON数据。

### 实例
# 定义一个简单的字典
data={
    "name":"puzhibin",
    "age":19,
    "xingbie":False

}
# 将字典序列化为JSON字符串
json_str = json.dumps(data)
print(json_str)

# 反序列化JSON字符串为字典
data_back = json.loads(json_str)
print(data_back)

### Pickle 序列化
# Pickle是python的一个内置模块，用于序列化和反序列化python对象结构。pickle可以序列化大多数python对象，包括负载的数据结构。
### 示例
# 定义一个简单字典
data1 = {
    "name":"puzhibin",
    "age":19,
    "xingbie":False,

}
# 将对象序列化为字节流
with open('data1.pickle','wb') as f:
    pickle.dump(data1,f)
# 从字节流中反序列化对象
with open('data1.pickle','rb') as f:
    data_back1 = pickle.load(f)
print(data_back1)

# 选择合适的序列化方法，
# 选择序列化方法时，需要考虑几个因素。
# 1.兼容性：如果你需要与非python系统交互，JSON通常是更好的选择，因为他是一种广泛支持的标准格式。
# 2.安全性：Pickle序列化可能导致安全问题，因为她可以执行任意python代码。因此在处理不受信任的数据源时，应谨慎使用pickle。
# 3.性能：Pickle通常比JSON更快，尤其是在处理复杂对象时。但是json更易于人阅读和调式。
