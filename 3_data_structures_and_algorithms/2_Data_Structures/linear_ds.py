class LinearDs:
    def __init__(self):
        """ initialize an empty python list"""
        self.items=[]
    def showItems(self):
        """ print the data structure contents """
        assert len(self.items)!=0 ,"data structure is empty"
        print(self.items)
        return
    def isEmpty(self):
        """ check if the data structure is empty or has elements"""
        return self.items==[]
    def size(self):
        """ return data structure size"""
        return len(self.items)
