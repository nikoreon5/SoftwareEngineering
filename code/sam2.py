def show_costs(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        costs = f.readlines()
        if costs:
            print("Книга расходов:")
            for cost in costs:
                print(cost.strip())
        else:
            print("На данный момент расходов нет.")
def add_cost(filename):
    with open(filename, 'a', encoding='utf-8') as f:
        cost = input("Введите расход и сумму: ")
        f.write(cost + "\n")
add_cost("code/costs.txt")
add_cost("code/costs.txt")
add_cost("code/costs.txt")
show_costs("code/costs.txt")