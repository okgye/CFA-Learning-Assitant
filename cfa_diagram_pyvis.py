from pyvis.network import Network
import networkx as nx

# Create a graph
G = nx.Graph()

# Add the central node for the CFA Level I Exam
G.add_node("CFA Level I Exam", size=30, title="CFA Level I Exam", color="#ff6666")

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

# Add topic nodes and connect them to the central node
for topic, subtopics in topics.items():
    G.add_node(topic, size=20, title=topic, color="#66b3ff")
    G.add_edge("CFA Level I Exam", topic)
    # Add subtopics and connect them to their parent topic
    for subtopic in subtopics:
        G.add_node(subtopic, size=15, title=subtopic, color="#99ff99")
        G.add_edge(topic, subtopic)

# Add cross-topic edges to reflect close relationships
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

# Create the PyVis network; adjust height, width, background and font color as desired
net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white", notebook=True)
net.from_nx(G)

# (Optional) Show physics controls to adjust layout parameters interactively
net.show_buttons(filter_=['physics'])

# Generate and open the interactive visualization
net.show("cfa_core_concepts.html")
