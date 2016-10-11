sum = 0
count = 0

while True:

    user_time = raw_input("Enter 10 km run time: ")
    if not user_time:
        if count == 0:
            print "Average time: 0"
        else:
            print "Average time: " + str(sum/count)
        break
    else:
        sum += float(user_time)
        count += 1


