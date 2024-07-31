

# 总结：
# GIL： 在多线程python程序中，即使没有使用锁，GIL也会阻止多个线程同时执行python字节码。
#       这意味着尽管线程可以切换执行，但他们不能真正并行运行。
# Lock： 当多个线程需要访问共享资源时，使用锁可以确保每次只能有一个线程可以访问该资源。
#       这可以防止竞态条件和其它同步问题。
