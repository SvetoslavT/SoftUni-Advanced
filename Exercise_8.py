# Fast Food
import collections


quantity_of_food = int(input())
int_orders = list(map(int, input().split(" ")))
largest_order = 0


while quantity_of_food > 0 or len(int_orders) > 0:
    if len(int_orders) == 0:
        break
    order = int_orders[0]
    if quantity_of_food - order < 0:
        break
    if order > largest_order:
        largest_order = order

    quantity_of_food -= order
    int_orders.pop(int_orders.index(order))


if int_orders:
    print((max(int_orders)))
    print(f"Orders left: {' '.join(str(n) for n in int_orders)}")
else:
    print(largest_order)
    print("Orders complete")


