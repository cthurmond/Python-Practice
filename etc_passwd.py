password_file = open("/etc/passwd", "r")

password_dict = {}

for line in password_file:
    if line[0] != "#":
        current_line = line.split(":")
        password_dict[current_line[0]] = current_line[2]

for key in sorted(password_dict.keys()):
    print key + " " + password_dict[key]

password_file.close()

