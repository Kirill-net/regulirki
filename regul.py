import csv
from pprint import pprint
from correct import Correct


with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

new = Correct(contacts_list)
new.correct_name()
new.correct_phone()
new.united()

with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list)











