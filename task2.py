import csv
from BTrees.OOBTree import OOBTree
import timeit

# --- Структури даних ---
tree = OOBTree()
dictionary = {}

# --- Додавання товарів ---
def add_item_to_tree(tree, item):
    tree[item["ID"]] = item

def add_item_to_dict(dictionary, item):
    dictionary[item["ID"]] = item

# --- Діапазонні запити ---
def range_query_tree(tree, min_price, max_price):
    return [item for _, item in tree.items() if min_price <= item["Price"] <= max_price]

def range_query_dict(dictionary, min_price, max_price):
    return [item for item in dictionary.values() if min_price <= item["Price"] <= max_price]

# --- Завантаження CSV ---
def load_data(path):
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        items = []
        for row in reader:
            item = {
                "ID": int(row["ID"]),
                "Name": row["Name"],
                "Category": row["Category"],
                "Price": float(row["Price"])
            }
            items.append(item)
        return items

# --- Запуск ---
data = load_data("generated_items_data.csv")

# Додавання в обидві структури
for item in data:
    add_item_to_tree(tree, item)
    add_item_to_dict(dictionary, item)

# --- Вимірювання часу ---
def benchmark(func, *args):
    return timeit.timeit(lambda: func(*args), number=100)

# Випадковий діапазон для тесту
min_price = 100
max_price = 300

tree_time = benchmark(range_query_tree, tree, min_price, max_price)
dict_time = benchmark(range_query_dict, dictionary, min_price, max_price)

print(f"Total range_query time for OOBTree: {tree_time:.6f} seconds")
print(f"Total range_query time for Dict:    {dict_time:.6f} seconds")
