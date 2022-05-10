import csv 
with open('navegacion (4).csv', 'r') as f:
    reader = csv.reader(f)
    with open("output.csv", "w") as result: 
            writer = csv.writer(result)
            for r in reader:
                writer.writerow()