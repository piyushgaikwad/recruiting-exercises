# inp = {"apple": 15, "banana": 10}
# warehouse = [{"name": "owd", "inventory": {"apple": 11, "banana": 3}},
#              {"name": "fine", "inventory": {"apple": 5, "banana": 3}}]

ans = []  # This list to store final shipping result
n = int(input("Enter a order Number:"))  # number of Orders
inp = {}
# input for order_____________________
for i in range(n):
    keys = input()  # here i have taken keys as strings
    values = int(input())  # here i have taken values as integers
    inp[keys] = values
#print(inp)

# input of warehouse data__________________
inventory1 = {}
warehouse = []
comp = int(input("Enter Warehouse number:"))
for i in range(comp):
    c = input('Enter Warehouse name:')
    # see_inventory = {'name': c, 'inventory': inventory1}
    tmp_items = {}
    for j in range(n):
        keys = input()  # here i have taken keys as strings
        values = int(input())  # here i have taken values as integers
        # inventory1[keys] = values
        tmp_items[keys] = values
    warehouse.append({'name': c, 'inventory': tmp_items})


# print(warehouse)

# function to find cheapest shipping among all warehouses_____________
def solve(inp, warehouse, ans):
    for i in inp.keys():
        curr_item = i  # example apple,banana from order dictionary inp
        total = inp[i]  # values in dictionary
        tmpans = []
        for i in warehouse:
            if total > 0:
                if curr_item in i["inventory"].keys() and i["inventory"][curr_item] != 0:

                    if i["inventory"][curr_item] >= total:
                        tmpans.append({i["name"]: {curr_item: total}})
                        total = 0
                        i["inventory"][curr_item] -= total
                    else:
                        tmpans.append({i["name"]: {curr_item: i["inventory"][curr_item]}})
                        total -= i["inventory"][curr_item]
                        i["inventory"][curr_item] = 0
                else:
                    break

        if total == 0:
            # ans.append()
            ans.append(tmpans)
        else:
            ans.clear()
            ans.append([])
    print(ans)


solve(inp, warehouse, ans)
