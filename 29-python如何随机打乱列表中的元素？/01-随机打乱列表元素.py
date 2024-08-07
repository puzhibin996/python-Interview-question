import random


def shuffle_list(arr):
    n = len(arr)
    for i in range(n -1, 0, -1):
        j = random.randint(0, i)
        arr[i],arr[j] = arr[j],arr[i],
    return arr

my_list = [1,2,3,4,5,6,7,8,9,10]
print(shuffle_list(my_list))


# 随机打乱列表中的元素，并且不能使用额外的内存空间，可以利用Fisher-Yates洗牌算法。
# 这个算法通过交换元素的位置来实现随机打乱，且不需要额外的内存空间。

