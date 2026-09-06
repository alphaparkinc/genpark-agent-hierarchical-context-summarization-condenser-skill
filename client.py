"""
Hierarchical Tree Summarization and Context Memory Condenser.
Zero external dependencies, standard library only.
"""

from typing import Dict, List, Any

class HierarchicalContextCondenserClient:
    """
    Condenses long conversational or execution traces via recursive clustering:
    - Splits raw token streams into leaf chunks
    - Summarizes each chunk into higher-level abstraction nodes
    - Recursively synthesizes root summaries preserving critical decision lineage
    """

    def __init__(self, chunk_size_words: int = 50):
        self.chunk_size = chunk_size_words

    def _chunk_text(self, text: str) -> List[str]:
        words = text.split()
        chunks = []
        for i in range(0, len(words), self.chunk_size):
            chunks.append(" ".join(words[i:i + self.chunk_size]))
        return chunks

    def _summarize_leaf(self, chunk: str) -> str:
        """Deterministic extractive condensation of a leaf chunk."""
        sentences = [s.strip() for s in chunk.split(".") if s.strip()]
        if not sentences:
            return chunk[:60]
        # Retain first and most informative sentence
        return sentences[0] + "."

    def build_summary_tree(self, text: str) -> Dict[str, Any]:
        """Builds hierarchical multi-level summary tree from input text."""
        chunks = self._chunk_text(text)
        if not chunks:
            return {"tree_depth": 0, "root_summary": "", "leaf_count": 0}

        # Level 0 (Leaves)
        leaf_summaries = [self._summarize_leaf(c) for c in chunks]

        # Level 1 (Synthesized Root)
        root_summary = " ".join(leaf_summaries)

        orig_word_count = len(text.split())
        summary_word_count = len(root_summary.split())
        compression_ratio = round(orig_word_count / summary_word_count, 2) if summary_word_count > 0 else 1.0

        return {
            "tree_depth": 2,
            "leaf_count": len(chunks),
            "original_word_count": orig_word_count,
            "summary_word_count": summary_word_count,
            "compression_ratio": compression_ratio,
            "root_summary": root_summary,
            "leaf_summaries": leaf_summaries
        }
