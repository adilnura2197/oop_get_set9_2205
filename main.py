class Kompyuter:
    def __init__(self, model, xotira):
        self.model = model
        self.__xotira = xotira

    def get_xotira(self):
        return self.__xotira

    def set_xotira(self, xotira):
        if xotira > 0:
            self.__xotira = xotira
            print("Xotira yangilandi")
        else:
            print("Noto'g'ri qiymat")


c1 = Kompyuter("HP", 8)
print(c1.get_xotira())
