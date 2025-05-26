def parklot_visual(park_slot_state):
    print("*" * 40)

    rows = ["A", "B", "C", "D"]
    columns = ["1", "2", "3", "4", "5"]
    header = "   " + "     ".join(columns)
    print(header.center(40))

    for row in rows:
        row_num = rows.index(row)
        row_state = []
        for i in park_slot_state[row_num]:
            if i == "O":
                row_state.append("[**]")
            else:
                row_state.append("[  ]")

        row_display = f"{row}  " + "  ".join(row_state)

        print(row_display.center(40))

    print("*" * 40)