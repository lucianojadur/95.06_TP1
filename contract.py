class Contract():

    def __init__(self, name, start, end):
        self.__name = name
        self.__start = int(start)
        self.__end = int(end)
        self.__length = (end - start)%167
        self.__status = False

    def name(self):
        return self.__name

    def start(self):
        return self.__start

    def end(self):
        return self.__end

    def length(self):
        return self.__length

    def info(self):
        return self.__name, self.__start, self.__end

    def is_incompatible_with(self, another_contract):

        if self.start() == another_contract.start() and self.end() == another_contract.end():
            return True
        #print(another_contract.name())
        #print(self.name())
        if self.is_cyclic():
            is_incompatible = (self.end() < another_contract.start() and self.start() < another_contract.start()) or (
                        self.end() > another_contract.end() and self.start() > another_contract.end())
            if is_incompatible == True:
                print("incompatible")
                return True

        is_incompatible = (self.start() > another_contract.start() and self.start() < another_contract.end()) or (
                    self.end() > another_contract.start() and self.end() < another_contract.end())
        if is_incompatible == True:
            #print("incompatible")
            return True

        return False

    def is_cyclic(self):
        return self.end() < self.start()