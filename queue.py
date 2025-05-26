class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, plate_num):
        self.q.append(plate_num)

    def dequeue(self):
        return self.q.pop(0)

    def get_cars_inqueue(self):
        return len(self.q)

    def has_car_onqueue(self):
        return False if not self.q else True  # No cars