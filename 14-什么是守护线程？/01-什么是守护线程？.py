import threading
import time


# 守护线程（Daemon Thread） 是一种特殊的线程类型，他的主要作用是在程序的主执行流程结束时自动终止。
# 守护线程通常用于执行后台任务，这些任务不需要阻塞程序的退出。
# 当python程序的所有非守护线程都完成并结束时，守护线程会被强制终止，无论他们是否已经完成他们的任务。
# 守护线程常用于以下场景：
# 执行清理工，比如定期清理缓存或日志。
# 监听事件，例如网络连接或文件系统变化。
# 提供某种形式的服务，如心跳检测或状态监控。

# 当你创建一个新的线程时，你可以通过设置daemon属性来指定他是否应该作为守护线程运行。
# 默认情况下，所有threading.Thread 创建的线程都是非守护线程。
# 要创建一个守护线程，你可以在启动线程之前设置daemon=True


def background_task():
    while True:
        print('我是守护线程~')
        time.sleep(1)


# 创建线程
daemon_thred = threading.Thread(daemon=True, target=background_task)

# 启动线程
daemon_thred.start()

# 主线程运行结束
time.sleep(5)
print('主线程结束')

# 守护线程的即时终止意味着他们可能不会有机会执行清理操作，因此，在设计守护线程时，最好确保他们能够在任何时候被中断，不会导致程序状态的不一致或数据丢失。
