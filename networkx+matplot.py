import networkx as nx
import matplotlib.pyplot as plt

# Erstellen des Kontrollfluss-Graphen
G = nx.DiGraph()

# Knoten hinzufügen
nodes = [
    "Start", "for filename in file_list", "file = find_file(filename)",
    "if (file == null)", "error_code = FILE_NOT_FOUND", "Break",
    "if (not open_file(file))", "error_code = ERROR_OPEN_FILE",
    "text_matches = search_file(file, text_to_censor)",
    "if (size(text_matches) == 0)", "error_code = ERROR_TEXT_NOT_FOUND",
    "else", "for position in text_matches", "replace_text(position, ' ')",
    "close_file(file)", "Next Iteration", "Return error_code"
]

for node in nodes:
    G.add_node(node)

# Kanten hinzufügen (Kontrollfluss)
edges = [
    ("Start", "for filename in file_list"),
    ("for filename in file_list", "file = find_file(filename)"),
    ("file = find_file(filename)", "if (file == null)"),
    ("if (file == null)", "error_code = FILE_NOT_FOUND"),
    ("error_code = FILE_NOT_FOUND", "Break"),
    ("if (file == null)", "if (not open_file(file))"),
    ("if (not open_file(file))", "error_code = ERROR_OPEN_FILE"),
    ("error_code = ERROR_OPEN_FILE", "Break"),
    ("if (not open_file(file))", "text_matches = search_file(file, text_to_censor)"),
    ("text_matches = search_file(file, text_to_censor)", "if (size(text_matches) == 0)"),
    ("if (size(text_matches) == 0)", "error_code = ERROR_TEXT_NOT_FOUND"),
    ("error_code = ERROR_TEXT_NOT_FOUND", "Break"),
    ("if (size(text_matches) == 0)", "else"),
    ("else", "for position in text_matches"),
    ("for position in text_matches", "replace_text(position, ' ')"),
    ("replace_text(position, ' ')", "close_file(file)"),
    ("close_file(file)", "Next Iteration"),
    ("Next Iteration", "for filename in file_list"),
    ("for filename in file_list", "Return error_code"),
    ("Break", "Return error_code")
]

for edge in edges:
    G.add_edge(*edge)

# Zeichnen des Graphen
plt.figure(figsize=(15, 10))
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color='red')
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')

plt.title("Programmstrukturgraph für die Funktion censor_files", fontsize=14)
plt.axis('off')
plt.show()
