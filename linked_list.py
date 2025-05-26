import string
import random


class ParkingSlot:
    def __init__(self, label, plate_num):
        self.label = label
        self.plate_num = plate_num


class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node


class Header:
    def __init__(self):
        self.head = None
        self._initialize_slots()

    def _initialize_slots(self):
        # Create ONLY 20 labeled slots
        rows = ["A", "B", "C", "D"]
        cols = range(1, 6)
        previous_node = None
        for row in reversed(rows):
            for col in reversed(cols):
                label = f"{row}{col}"
                node = Node(ParkingSlot(label, "None"), previous_node)
                previous_node = node
        self.head = previous_node

    # FOR TESTING PURPOSES ????????????????????????????????????????????????????????????
    def _init_full_slots(self):
        current_node = self.head
        while current_node is not None:
            if current_node.value.plate_num == "None":  # Find the first available slot (naka-order from A1 to D5)
                rand_id = self.id_generator()
                current_node.value.plate_num = rand_id
            current_node = current_node.next_node

    def id_generator(self, size=3, chars=string.ascii_uppercase, nums=string.digits):
        rand_str = "".join(random.choice(chars) for _ in range(size))
        rand_int = "".join(random.choice(nums) for _ in range(size))
        return ' '.join((rand_str, rand_int))

    # FOR TESTING PURPOSES ????????????????????????????????????????????????????????????

    def insert(self, plate_num):
        # if self.check_plate_num(plate_num): FOR CHECKING (SHOULD BE ON UI)
        #     print("gumagana ^_^")
        #     return

        current_node = self.head
        while current_node is not None:
            if current_node.value.plate_num == "None":  # Find the first available slot (naka-order from A1 to D5)
                current_node.value.plate_num = plate_num
                return current_node.value.label  # return label to be printed out sa ui
            current_node = current_node.next_node
        # print("All slots are full. Cannot add more plate numbers.")     # If mas malaki sa 20

    def delete_plate_num(self, slot_code):
        current_node = self.head
        while current_node is not None:
            if current_node.value.label == slot_code:
                if current_node.value.plate_num == "None":
                    return False  # means slot code have no car
                else:
                    current_node.value.plate_num = "None"
                    # print(f"Plate number {plate_num} has been removed.")    # Prints after deleting.
                    return True  # means successfully removed
            current_node = current_node.next_node

    def is_full(self):
        current_node = self.head
        while current_node is not None:
            if current_node.value.plate_num == "None":
                return False  # meaning may bakante pa
            current_node = current_node.next_node

        return True  # if while loop ends nang wala bakante, means puno na

    # this is for the visual
    def get_parking_slot_state(self) -> list:
        current_node = self.head

        raw_list = []
        while current_node is not None:
            if current_node.value.plate_num == "None":
                raw_list.append("E")
            else:
                raw_list.append("O")

            current_node = current_node.next_node

        row1 = raw_list[:5]
        row2 = raw_list[5:10]
        row3 = raw_list[10:15]
        row4 = raw_list[15:]
        parking_slot_state = [row1, row2, row3, row4]

        return parking_slot_state

    def print_linked_list(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            print(f"{current_node.value.label}({current_node.value.plate_num})", end=" -> ")
            current_node = current_node.next_node
            count += 1
            if count % 5 == 0:
                print()

    def check_plate_num(self, plate_num):  # if True -> naulit, else return (nothing happens)
        current_node = self.head
        while current_node is not None:
            if current_node.value.plate_num == plate_num:
                return True
            current_node = current_node.next_node
        return False


'''functions: print_linked_list -> prints the list|| insert -> inserts plate number|| delete_plate_num -> deletes existing plate number'''