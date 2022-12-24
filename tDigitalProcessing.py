# coding: UTF-8


class DigitalProcessing:
    @staticmethod
    def addUpEachItem(list_auei: list, flag: int = 0):
        """
        Add up each number in the list to get the value
        """
        flag = flag
        for i in list_auei:
            flag += i
        return flag

    @staticmethod
    def aneil(list_: list, flag: int = 1):
        """
        Add a number to each item in the list
        """
        return list(map(lambda x: x + flag, list_))

    def fcnaesn(self, numbers: list, lastValues: int):
        """
        Find a continuous number that adds equal to the specified number
        """
        while True:
            number_auei = self.addUpEachItem(numbers)
            if number_auei == lastValues:
                return numbers
            else:
                numbers = list(map(lambda x: x + 1, numbers))
                continue

    @staticmethod
    def ctl(snfl: str):
        """
        Cycle through the list
        The string that needs to be filled in the list
        :return:
        """
        for i in range(len(snfl)):
            rlist = [i]
        for j in snfl:
            rlist = [i] = j
        return rlist
