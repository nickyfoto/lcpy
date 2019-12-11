class MetaCls(type):
    def __getitem__(cls, index):
        pass
       # print("Using meta __getitem__ on classes that have my type")

class List(metaclass=MetaCls):
    pass

