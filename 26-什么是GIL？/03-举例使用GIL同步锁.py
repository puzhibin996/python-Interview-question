import threading

# 共享变量
counter = 0
counter_lock = threading.Lock()

# 增加计数器的值
def increment_counter(n):
    global counter
    for _ in range(n):
        with counter_lock:
            counter+=1
# 创建线程
num_threads = 10
num_increments = 100000
threads = []
# 启动线程
for i in range(num_threads):
    t = threading.Thread(target=increment_counter,args=(num_increments,))
    threads.append(t)
    t.start()
# 等待所有线程完成
for t in threads:
    t.join()
print(f"Final counter value:{counter}")


