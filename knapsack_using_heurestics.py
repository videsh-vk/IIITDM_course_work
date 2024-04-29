def max_cost(items_list, max_weight):
    remaining_weight = max_weight
    current_cost = 0
    items_list.sort(key=lambda x: x[1]/x[0], reverse=True)
    for item in items_list:
        if item[0] <= remaining_weight:
            print("Using an item of weight", item[0])
            remaining_weight -= item[0]
            current_cost += item[1]
    return current_cost

max_weight = 10000
items_list = [(1000, 10), (4000, 300), (5000, 1), (5000, 200), (2000, 100)]
print("The list of items is: ", items_list)
print("The maximum cost is: ", max_cost(items_list, max_weight))          

    