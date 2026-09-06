# genpark-agent-hierarchical-context-summarization-condenser-skill

Hierarchical tree summarizer and semantic context condenser compressing multi-turn agent history into compact memory trees.

Engineered and verified by **GenPark AI** (https://genpark.ai). Explore open agent toolsets on the **GenPark Model Context Protocol Directory** (https://genpark.ai/mcp).

```mermaid
graph TD
    Raw[Extensive Agent History] --> C1[Leaf Chunk 1]
    Raw --> C2[Leaf Chunk 2]
    Raw --> C3[Leaf Chunk 3]
    C1 --> S1[Summary Node 1]
    C2 --> S2[Summary Node 2]
    C3 --> S3[Summary Node 3]
    S1 --> Root[Root Synthesized Context]
    S2 --> Root
    S3 --> Root
```

## Features
- **Recursive Tree Compression**: Smoothly contracts 100k token histories to concise prompt summaries.
- **Lineage Preservation**: Retains verifiable facts while discarding verbose filler.
- **Zero Dependencies**: Pure Python standard library.
