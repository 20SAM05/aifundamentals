import csv

# with open("students.csv", "w" , newline="") as f :
#   writer = csv.writer(f)
#   writer.writerow(["Name","Age","Grade"])
#   writer.writerow(["Alice",14,"8th"])
#   writer.writerow(["Bob",15,"9th"])
#   writer.writerow(["Charlie",13,"7th"])
  

with open("students.csv","r") as f :
  reader = csv.reader(f)
  for row in reader :
    print(row)
