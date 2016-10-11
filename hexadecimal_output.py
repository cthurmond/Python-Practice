while True:
    user_input = raw_input("Enter a hexadecimal number to convert,\
or 'q' to quit: ")
    if user_input.lower() == "q":
        break
    else:
        user_input = "0x" + user_input
        print int(user_input, 16)


