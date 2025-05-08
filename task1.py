import networkx as nx

# Побудова графа
G = nx.DiGraph()

# Додаткові вузли
G.add_node("Source")
G.add_node("Sink")

# Вузли
terminals = ["Термінал 1", "Термінал 2"]
warehouses = ["Склад 1", "Склад 2", "Склад 3", "Склад 4"]
stores = [f"Магазин {i}" for i in range(1, 15)]

# Джерело до терміналів
G.add_edge("Source", "Термінал 1", capacity=999)
G.add_edge("Source", "Термінал 2", capacity=999)

# Термінали до складів
G.add_edge("Термінал 1", "Склад 1", capacity=25)
G.add_edge("Термінал 1", "Склад 2", capacity=20)
G.add_edge("Термінал 1", "Склад 3", capacity=15)

G.add_edge("Термінал 2", "Склад 2", capacity=10)
G.add_edge("Термінал 2", "Склад 3", capacity=15)
G.add_edge("Термінал 2", "Склад 4", capacity=30)

# Склади до магазинів
G.add_edge("Склад 1", "Магазин 1", capacity=15)
G.add_edge("Склад 1", "Магазин 2", capacity=10)
G.add_edge("Склад 1", "Магазин 3", capacity=20)

G.add_edge("Склад 2", "Магазин 4", capacity=15)
G.add_edge("Склад 2", "Магазин 5", capacity=10)
G.add_edge("Склад 2", "Магазин 6", capacity=25)

G.add_edge("Склад 3", "Магазин 7", capacity=20)
G.add_edge("Склад 3", "Магазин 8", capacity=15)
G.add_edge("Склад 3", "Магазин 9", capacity=10)

G.add_edge("Склад 4", "Магазин 10", capacity=20)
G.add_edge("Склад 4", "Магазин 11", capacity=10)
G.add_edge("Склад 4", "Магазин 12", capacity=15)
G.add_edge("Склад 4", "Магазин 13", capacity=5)
G.add_edge("Склад 4", "Магазин 14", capacity=10)

# Магазини до стоку
for store in stores:
    G.add_edge(store, "Sink", capacity=999)

# Алгоритм максимального потоку
flow_value, flow_dict = nx.maximum_flow(G, "Source", "Sink", flow_func=nx.algorithms.flow.edmonds_karp)

print(f"\nМаксимальний потік: {flow_value}\n")
print("Термінал\tМагазин\t\tФактичний Потік")

# Вивід потоку: Термінал → Склад → Магазин
for terminal in terminals:
    for warehouse in flow_dict[terminal]:
        if flow_dict[terminal][warehouse] > 0:
            for store in flow_dict[warehouse]:
                if store.startswith("Магазин") and flow_dict[warehouse][store] > 0:
                    print(f"{terminal}\t\t{store}\t{flow_dict[warehouse][store]}")
