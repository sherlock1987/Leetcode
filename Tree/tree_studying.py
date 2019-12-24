class Node(object):
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None#初始化程序，每次都会执行的。
#小的放在左边，大的放在右边
    def insert(self,newData):
        if self.data == newData:
            return False
        elif newData < self.data:
            if self.leftChild == None:#生成新的node
                self.leftChild = Node(newData) #重复创建的意思
            else:
                self.leftChild.insert(newData)
        elif newData > self.data:
            if self.rightChild == None:#生成新的node
                self.rightChild  = Node(newData)
            else:
                self.rightChild.insert(newData)

    def findValue(self,newData):
        if self.data == newData:
            return True
        elif newData < self.data:
            if self.leftChild == None:#没有找到
                return False
            else:
                return self.leftChild.findValue(newData)
        else:
            if self.rightChild == None:#没有找到
                return False
            else:
                return self.rightChild.findValue(newData) #从这个right开始找数字 不熟悉此类用法

if __name__ == '__main__': #运行这个文件的时候执行，运行其他文件的时候不执行
    node = Node(5)
    node.insert(100)
    node.insert(6)

    print (node.findValue(100))