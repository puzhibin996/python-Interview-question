# python中常见的数据结构有：
# 1. ————————————————————————————————链表————————————————————————————————

# python中实现链表
# 单链表-节点类
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# 但链表-链表类
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self,key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        prev_node = None
        while cur_node and cur_node.data != key:
            prev_node = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return
        prev_node.next = cur_node.next
        cur_node = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def insert_after_node(self,prev_node_data,data):
        if not self.head:
            raise ValueError(" The list has no elements")
        prev_node = self.head
        while prev_node and prev_node.data != prev_node_data:
            prev_node = prev_node.next
        if not prev_node:
            raise ValueError("")
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

# 使用链表
# 创建一个链表实例
llist = LinkedList()
# 在链表尾部添加元素
llist.append('a')
llist.append('b')
llist.append('c')
print("链表元素：",llist.print_list())

# 在链表头部添加元素
llist.prepend('D')
print("链表元素：",llist.print_list())


# 在指定节点之后插入元素
llist.insert_after_node('b','E')
print("链表元素：",llist.print_list())


# 删除链表中的元素
llist.delete_node('a')
print("链表元素：",llist.print_list())



# 总结
# 链表是一种常见的数据结构，它有节点组成，每个节点包含数据和指向下一个节点的引用。与数组相比，连败哦在内存中不一定连续存储，
# 而是通过节点之间的链接来组织数据。链表在python中并不直接内置，但可以通过定义节点类和链表类来实现。
# 链表的类型：
#           单链表：每个节点质保函一个指向下个节点的引用
#           双链表：每个节点包含指向前一个节点和后一个节点的引用
#           循环链表：最后一个节点的引用指向第一个节点，形成闭环










