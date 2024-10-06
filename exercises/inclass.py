my_numbers: list[str] = ["bananas", "eggs"]
my_numbers.append("bananas")
print(my_numbers)
print(len(my_numbers))

my_name: str = "Izzi"
my_name_as_list: list[str] = list(my_name)
print(my_name_as_list)
my_name_as_list[3] = "y"
print(my_name_as_list)
my_name_as_list.insert(4, "i")

x: list[float] = [1.0, 2.0]
y: list[float] = [3.0, 4.0]
y = x
x[0] = 3.0
print(x)
print(y)
