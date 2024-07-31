import threading

# 关于全局解释器锁（Global interpreter Lock 简称GIL）的问题非常常见。
# GIL是CPython（Python的官方实现）中的一个同步机制，他确保在同一时刻只有一个线程能够在Python字节码上执行。
# GIL的主要作用：
# 1.简化内存管理： 由于CPython的内存管理不是线程安全的，GIL避免了多个线程同时访问Python对象而导致的数据竞争问题。
# 2.保证线程安全： 确保不会有两个线程同事执行python字节码，从而避免了数据竞争不一致的问题.
# GIL的限制：
# 1.多核性能受限： 在多核处理器上，即时有多个核心可用，由于GIL的存在，python的多线程程序也只能在一个核心上运行
# 2.I/O密集型任务影响较小： 对于I/O密集型任务（如网络请求、文件读写等），GIL的影响相对较小，因为当线程阻塞等待I/O时，GIL会被释放，其它线程可以运行。


# 代码举例：


# 创建共享变量
counter = 0
def increment_counter(n):
    global counter
    for _ in range(n):
        counter +=1
def thread_task(n):
    print(f"Thread {threading.current_thread().name} starts")
    increment_counter(n)
    print(f"Thread {threading.current_thread().name} finishes")

# 创建两个线程
t1 = threading.Thread(target=thread_task,args=(10000,))
t2 = threading.Thread(target=thread_task,args=(10000,))
# 启动线程
t1.start()
t2.start()

# 等待线程完成
t1.join()
t2.join()
print(f"Final counter value:{counter}")



