some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

for item in some_list:
  counter_of_dublicates = 0
  for is_dublicate in some_list:
    if (item == is_dublicate):
      counter_of_dublicates +=1
      if counter_of_dublicates > 1:
        print("items", is_dublicate) 

my_dubl_list = []
for values in some_list:
  if some_list.count(values) > 1:
    if values not in my_dubl_list:
      my_dubl_list.append(values)

print(my_dubl_list)