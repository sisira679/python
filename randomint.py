import random
print("create a list of random integers:")
population=range(0,100)
num_list=random.sample(population,10)
print(num_list)
no_elements=4
print("\n Randomly select",no_elements,"multiple items from the said list:")
result_elements=random.sample(num_list,no_elements)
print(result_elements)
no_elements=8
print("\n randomly select",no_elements,"multiple items from the said list:")
result_elements=random.sample(num_list,no_elements)
print(result_elements)