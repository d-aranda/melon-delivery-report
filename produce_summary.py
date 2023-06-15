def melon_delivery_report(filename, day):
    """Prints delivery report for inputted file and day"""
    
    with open(filename) as file:
        print(f"Day {day}")
        for line in file:
            melon, count, amount = line.rstrip().split("|")
        

        print(f"Delivered {count} {melon}s for total of ${amount}")

melon_delivery_report("um-deliveries-day-1.txt", 1)


# print("Day 1")
# the_file = open("um-deliveries-day-1.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-day-2.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-day-3.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()
