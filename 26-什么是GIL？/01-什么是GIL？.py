



# 关于全局解释器锁（Global interpreter Lock 简称GIL）的问题非常常见。
# GIL是CPython（Python的官方实现）中的一个同步机制，他确保在同一时刻只有一个线程能够在Python字节码上执行。
# GIL的主要作用：
# 1.简化内存管理： 由于CPython的内存管理不是线程安全的，GIL避免了多个线程同时访问Python对象而导致的数据竞争问题。