import threading

# 创建共享变量
counter = 0
# 增加计数器的值
def increment_counter(n):
    global counter
    for _ in range(n):
        counter+=1
# 创建线程
num_threads = 10
num_increments =100000
threads = []
# 启动线程
for i in range(num_threads):
    t = threading.Thread(target=increment_counter,args=(num_increments,))
    threads.append(t)
    t.start()
#等待所有线程完成
for t in threads:
    t.join()
print(f"Final counter value:{counter}")

# 没有使用锁，因此当多个线程尝试同时修改counter时可能会发生竞态条件。







