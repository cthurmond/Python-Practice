source_files = []

write_file = open("exercises.md", "w")
write_file.write("# Exercises")
for file in source_files:
    if file.endswith(".md"):
        write_file.write("##" + str(file).capitalize)
        open_file = open(file, "r")
        count = 1
        for line in open_file:
            if line.startswith("##"):
            	write_file.write("### " + str(count) + "Exercise " \
            		+ str(count)
            if not line.startswith("#"):
            	write_file.write(line)

        
