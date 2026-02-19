lst1 = ['rudra', 100, 200, 'sampreet', 100.50, 'super', 3.14];
# [start<opt> : end<opt> : step<opt>] 
print(lst1[1:6]); # prints elements from index 1 to 5
print(lst1[::2]); # prints non-adjacent elements

# insert(index, element);
lst1.insert(1, "loves");
# creates a nested list
lst1.append(['but', 'sampreet', 'dosnt', 'love', 'rudra']); 
print(lst1);

lst2 = [1, 2, 3, 4, 5, 6, 7];
# add the elements in list 
lst2.extend([8, 9]);
print(lst2);

print(sum(lst2));
lst2.pop();
print(lst2);

# add another 1 to lst2
lst2.append(1);
print(lst2.count(1));

# list.index(elmnt*, start<opt>, end<opt>)
print(lst2.index(1, 1));
# positional Args
print("minimum element in the list 2 is : {} and maximum is : {}".format(min(lst2), max(lst2))); 
# keyword Args
print("minimum element in the list 2 is : {mini} and maximum is : {maxi}".format(mini=min(lst2), maxi=max(lst2))); 

lst2*=5 # whole list will get append 5 times!
print(lst2);

# Set
st = set()
print(type(st))

st = {"rudra", "aditi", "sampreet", "adithi", "rudra"};
print(st)
st.add("sampreet")

# another way to implement set
dic1 = {1, 2, 3, 4, 5};
print(type(dic1))
print(dic1)

# Dictionary
dic2 = {"car1" : "BMW", "car2" : "Audi", "car3" : "Benz"};
print(type(dic2))
for x in dic2.items():
  print(x)
  
# Nested Dictionary
car1_model_type = {"manual":2000}
car2_model_type = {"automatic":2000}
car3_model_type = {"hybrid":2000}
car_mods = {"Audi":car2_model_type, "Benz":car3_model_type, "BMW":car1_model_type};

print("audi automatic model year is: {}".format(car_mods["Audi"]["automatic"]));

# tuples  
# - immutable unlike list they cannot be modified only can be replaced with anther tuple
# - memory efficient as the size is fixed!
tup = tuple();
tup = ("akshay", "kareena", "both", "would", "look", "great", "in", "a", "movie");
print(tup)



















