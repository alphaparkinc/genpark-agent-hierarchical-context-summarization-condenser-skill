"""
Demonstration of genpark-agent-hierarchical-context-summarization-condenser-skill
"""

from client import HierarchicalContextCondenserClient

def main():
    condenser = HierarchicalContextCondenserClient(chunk_size_words=20)

    long_narrative = (
        "Agent received order 401 from customer Alice. Customer requested expedited shipping for heavy industrial machinery. "
        "Logistics verified inventory at Texas warehouse facility. Inventory is currently sufficient with 40 units ready. "
        "Carrier FedEx freight dispatched for pallet pickup. Expected delivery is scheduled for Thursday noon. "
        "Customer confirmation email dispatched and logged into audit ledger."
    )

    result = condenser.build_summary_tree(long_narrative)
    print("=== HIERARCHICAL CONTEXT TREE BUILT ===")
    print(f"Original Words: {result['original_word_count']} -> Summary Words: {result['summary_word_count']}")
    print(f"Compression Factor: {result['compression_ratio']}x")
    print("Root Condensation:", result["root_summary"])

if __name__ == "__main__":
    main()
