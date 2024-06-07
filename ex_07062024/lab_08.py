# list-add shopping card
# milk,bread,butter
# 1.add list
# 2.Remove list
# 3.Update list
# 4.view item
# 5.Exit

shopping_list = ["milk", "bread", "butter"]
print(shopping_list)
print(len(shopping_list))
print(shopping_list[0])
print(shopping_list[-1])

my_list = [1, 2, 3, "rut"]
print(type(my_list))
my_list.append("solanki")  # add item in the end of list
my_list.insert(1, "rutvi")

print(my_list)
my_list.remove(2)
print(my_list)
print(my_list.pop())
print(my_list.index(1))
"""
o/p
['milk', 'bread', 'butter']
3
milk
butter
<class 'list'>
"""
