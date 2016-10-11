# *** MY CODE ***

import csv

with open("/etc/passwd", "r") as f, open("write_file.txt", "w") as w:
    reader = csv.reader(f, delimiter=":")
    writer = csv.writer(w, delimiter="\t")
    for row in reader:
            try:
                writer.writerow([row[0], row[2]])
            except IndexError:
                pass

# *** HIS CODE ***
#with open('/etc/passwd') as passwd, open('/tmp/output.csv', 'w') as output:
    #r = reader(passwd, delimiter=':')
    #w = writer(output, delimiter='\t')
    #for record in r:
        #if len(record) > 1:
            #w.writerow((record[0], record[2]))
