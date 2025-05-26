import time, re

from linked_list import Header
from queue import Queue
from search_algorithm import Array
from visual import parklot_visual


def initialize():
    linked_list = Header()
    queue = Queue()
    array = Array()
    start_program(linked_list, queue, array)


# opening screen
def start_program(linked_list, queue, array):
    time.sleep(1.5)

    print("\n\n\n")
    print("PARKING LOT MANAGEMENT SYSTEM".center(40))

    # method that generates the parking lot visual
    park_slot_state = linked_list.get_parking_slot_state()  # method from linked list class
    parklot_visual(park_slot_state)

    print(f"Cars on queue: {queue.get_cars_inqueue()}")

    print("\n[1] Car pulls in\n[2] Car pulls out\n[3] Search for the Car\n[4] Exit")
    selected = input("Select an option: ").strip()

    match selected:
        case "1":
            plate_num = input("Input car's plate number: ")
            if not is_valid(plate_num):
                print("Invalid plate number format.")
                start_program(linked_list, queue, array)

            # method that takes the plate_num then store it to linked list and array
            slot_code = car_pull_in_process(plate_num, linked_list, queue, array)
            array.add_to_list(slot_code, plate_num)

            if slot_code is None:
                print("Car is put on queue.")
            else:
                print(f"Car parked at slot {slot_code}.")

            start_program(linked_list, queue, array)

        case "2":
            slot_code = input("Input slot code: ")
            # method that takes the plate_num then deletes it to linked list and array
            if linked_list.delete_plate_num(slot_code):
                array.remove_from_list(slot_code)
                print(f"Car on slot {slot_code} successfully pulled out.")

                # Check queue, dequeue, and insert process
                if queue.has_car_onqueue():
                    slot_code, plate_num = dequeue_and_insert(linked_list, queue, array)
                    array.add_to_list(slot_code, plate_num)
                    print(f"Next on queue is now parked at slot {slot_code}.")

            else:
                print(f"There is no occupying car on slot {slot_code}.")

            start_program(linked_list, queue, array)

        case "3":
            plate_num = input("Input car's plate number: ")

            car_slot = array.linearsearch_car(plate_num)
            if car_slot is None:
                print(f"Car with plate number {plate_num} not found.")
            else:
                print(f"Car with plate number {plate_num} is at slot {car_slot}.")

            start_program(linked_list, queue, array)

        case "4":
            print("Thank you for using this program.")
            time.sleep(1.5)

            quit()

        # hidden cases
        case "5":
            linked_list.print_linked_list()
            start_program(linked_list, queue, array)
        case "6":
            linked_list._init_full_slots()
            print("Filling all slots...")
            start_program(linked_list, queue, array)

        case _:
            print("Invalid input. Try again")
            start_program(linked_list, queue, array)


def dequeue_and_insert(linked_list, queue, array):
    plate_num = queue.dequeue()
    slot_code = car_pull_in_process(plate_num, linked_list, queue, array)
    return slot_code, plate_num


def car_pull_in_process(plate_num, linked_list, queue, array):
    # check if naulit plate num
    if linked_list.check_plate_num(plate_num):
        print("Plate number already exist in the lot.")
        start_program(linked_list, queue, array)
    else:
        # check if puno na yung linked list
        if linked_list.is_full():
            queue.enqueue(plate_num)  # add car to queue
            return None
        else:
            return linked_list.insert(plate_num)  # this method returns label/ slot code


def is_valid(plate_num):
    regex = r"[A-Z]{3} \d{3}"

    return True if re.fullmatch(regex, plate_num) else False


if __name__ == "__main__":
    initialize()