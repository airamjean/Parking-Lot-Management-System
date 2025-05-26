class Array():
    def __init__(self):
        self.carlist = []
        self._initialize()

    def _initialize(self):
        letters = ["A", "B", "C", "D"]
        nums = ["1", "2", "3", "4", "5"]

        for letter in letters:
            for num in nums:
                temp_list = [letter + num, ""]
                self.carlist.append(temp_list)

    def linearsearch_car(self, plate_num):
        """
        Input: carlist, target plate number
        Output: Parking Spot Code or None
        """
        length = len(self.carlist)
        for i in range(0, length):
            if self.carlist[i][1] == plate_num:
                return self.carlist[i][0]
            else:
                return None

    def add_to_list(self, slot_code, plate_num):
        length = len(self.carlist)
        for i in range(0, length):
            if self.carlist[i][0] == slot_code:
                self.carlist[i][1] = plate_num
                return

    def remove_from_list(self, slot_code):
        length = len(self.carlist)
        for i in range(0, length):
            if self.carlist[i][0] == slot_code:
                self.carlist[i][1] = ""
                return