import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph (though the hierarchy is somewhat conceptual rather than strictly directional)
G = nx.Graph()

# --------------------------
# 1. CENTRAL NODE
# --------------------------
G.add_node("CFA Level I Exam", size=2500, color="#ff6666")

# --------------------------
# 2. TOPIC NODES (10 Major)
# --------------------------
topics = {
    "Ethical & Professional Standards": ["Code of Ethics", "Professional Conduct", "GIPS Standards"],
    "Quantitative Methods": ["Time Value of Money", "Statistical Concepts", "Probability & Hypothesis Testing"],
    "Economics": ["Microeconomics", "Macroeconomics", "International Trade & Currency"],
    "Financial Reporting & Analysis (FSR)": ["Financial Statements", "Ratios & Analysis", "Accounting Standards"],
    "Corporate Issuers": ["Corporate Governance", "Capital Budgeting", "ESG & Stakeholder Management"],
    "Equity Investments": ["Equity Valuation", "Market Efficiency", "Industry & Company Analysis"],
    "Fixed Income": ["Bond Valuation", "Yield Measures", "Duration & Convexity"],
    "Derivatives": ["Forwards & Futures", "Options", "Swaps"],
    "Alternative Investments": ["Real Estate", "Private Equity", "Hedge Funds"],
    "Portfolio Management": ["Portfolio Theory", "Asset Allocation", "Risk & Return"]
}

# Add the major topic nodes
for topic in topics:
    G.add_node(topic, size=1800, color="#66b3ff")
    # Connect each major topic to the central node
    G.add_edge("CFA Level I Exam", topic)

# --------------------------
# 3. SUBTOPICS
# --------------------------
# Add subtopic nodes and connect them to their respective major topics
for topic, subtopic_list in topics.items():
    for subtopic in subtopic_list:
        G.add_node(subtopic, size=1200, color="#99ff99")
        G.add_edge(topic, subtopic)

# --------------------------
# 4. CROSS-EDGES FOR RELATED CONCEPTS
# (Brings related topics closer together)
# --------------------------

# Ethical & Professional Standards touches all areas conceptually,
# but we won't add too many edges to avoid clutter.
G.add_edge("Ethical & Professional Standards", "Corporate Issuers")
G.add_edge("Ethical & Professional Standards", "Financial Reporting & Analysis (FSR)")

# Quantitative Methods strongly related to Economics & Portfolio Management
G.add_edge("Quantitative Methods", "Economics")
G.add_edge("Quantitative Methods", "Portfolio Management")

# Financial Reporting & Analysis (FSR) is closely linked with Corporate Issuers and Equity Investments
G.add_edge("Financial Reporting & Analysis (FSR)", "Corporate Issuers")
G.add_edge("Financial Reporting & Analysis (FSR)", "Equity Investments")

# Equity Investments often ties to Fixed Income & Derivatives (capital markets)
G.add_edge("Equity Investments", "Fixed Income")
G.add_edge("Equity Investments", "Derivatives")

# Fixed Income & Derivatives are closely related
G.add_edge("Fixed Income", "Derivatives")

# Derivatives & Alternative Investments have conceptual overlap
G.add_edge("Derivatives", "Alternative Investments")

# Portfolio Management is a broad discipline that uses inputs from Equities, Fixed Income, Alternatives
G.add_edge("Portfolio Management", "Equity Investments")
G.add_edge("Portfolio Management", "Fixed Income")
G.add_edge("Portfolio Management", "Alternative Investments")

# --------------------------
# 5. DRAW THE GRAPH
# --------------------------
plt.figure(figsize=(14, 10))

# Spring layout with random seed for reproducibility
pos = nx.spring_layout(G, k=2.0, seed=42)

# Extract node attributes
node_sizes = [G.nodes[node].get('size', 1000) for node in G.nodes]
node_colors = [G.nodes[node].get('color', "#cccccc") for node in G.nodes]

# Draw nodes and edges
nx.draw_networkx_edges(G, pos, alpha=0.4, edge_color="gray")
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.9)
nx.draw_networkx_labels(G, pos, font_size=9, font_weight="bold")

plt.title("CFA Level I Exam – Core Concepts Hierarchy & Relationships", fontsize=14, fontweight="bold")
plt.axis("off")
plt.savefig("diagram.png")

