import matplotlib.pyplot as plt
import networkx as nx
from adjustText import adjust_text

# Create the graph
G = nx.Graph()

# Add the central node for the CFA Level I Exam
G.add_node("CFA Level I Exam", size=2500, color="#ff6666")

# Define the major topics and their subtopics
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

# Add major topics and subtopics, and connect them to the central node
for topic, subtopics in topics.items():
    G.add_node(topic, size=1800, color="#66b3ff")
    G.add_edge("CFA Level I Exam", topic)
    for subtopic in subtopics:
        G.add_node(subtopic, size=1200, color="#99ff99")
        G.add_edge(topic, subtopic)

# Add cross-topic edges to reflect relationships
G.add_edge("Ethical & Professional Standards", "Corporate Issuers")
G.add_edge("Ethical & Professional Standards", "Financial Reporting & Analysis (FSR)")
G.add_edge("Quantitative Methods", "Economics")
G.add_edge("Quantitative Methods", "Portfolio Management")
G.add_edge("Financial Reporting & Analysis (FSR)", "Corporate Issuers")
G.add_edge("Financial Reporting & Analysis (FSR)", "Equity Investments")
G.add_edge("Equity Investments", "Fixed Income")
G.add_edge("Equity Investments", "Derivatives")
G.add_edge("Fixed Income", "Derivatives")
G.add_edge("Derivatives", "Alternative Investments")
G.add_edge("Portfolio Management", "Equity Investments")
G.add_edge("Portfolio Management", "Fixed Income")
G.add_edge("Portfolio Management", "Alternative Investments")

# Attempt to use Graphviz's hierarchical layout ("dot") if available; otherwise, use a spring layout
try:
    pos = nx.nx_agraph.graphviz_layout(G, prog='dot')
except Exception as e:
    print("Graphviz layout not available, falling back to spring layout.")
    pos = nx.spring_layout(G, k=1.5, seed=42)

# Prepare node attributes for drawing
node_sizes = [G.nodes[node].get('size', 1000) for node in G.nodes]
node_colors = [G.nodes[node].get('color', "#cccccc") for node in G.nodes]

# Create a high-resolution figure with A4 landscape dimensions (11.69" x 8.27")
plt.figure(figsize=(11.69, 8.27), dpi=300)
nx.draw_networkx_edges(G, pos, alpha=0.4, edge_color="gray")
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.9)

# Manually place labels and adjust to avoid overlapping
texts = []
for node, (x, y) in pos.items():
    txt = plt.text(x, y, node, fontsize=7, fontweight='bold',
                   horizontalalignment='center', verticalalignment='center',
                   bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=1))
    texts.append(txt)

# Adjust labels to minimize overlap
adjust_text(texts, arrowprops=dict(arrowstyle="-", color='black', lw=0.5))

plt.title("CFA Level I Exam – Core Concepts Hierarchy", fontsize=16, fontweight="bold")
plt.axis("off")

# Save the figure in landscape A4 size (both PDF and high-resolution PNG)
plt.savefig("cfa_core_concepts_landscape_A4.pdf", format="pdf", bbox_inches="tight")
plt.savefig("cfa_core_concepts_landscape_A4.png", format="png", bbox_inches="tight")

print("A4 landscape printable files 'cfa_core_concepts_landscape_A4.pdf' and 'cfa_core_concepts_landscape_A4.png' have been saved.")
