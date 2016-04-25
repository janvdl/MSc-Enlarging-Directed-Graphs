My M.Sc. - Enlarging directed graphs to ensure all nodes are contained in cycles
===
Python source code for my thesis on graph enlargement. I hope someone may find my work useful in the future.

Licence
===
Licenced under GPL v2 (see "licence" file). You *must* open-source any works derived from my programs. 

Conference Proceedings
===
http://dl.acm.org/citation.cfm?id=2815825

Abstract
===
Many algorithms in graph theory add or remove either edges or nodes (or both) to solve a given problem. Graph augmentation typically concerns the addition of edges to a graph to satisfy some connectivity property of the graph. This paper focuses on the addition of vertices to a graph to satisfy a specific connectivity property: ensuring that all the nodes of the graph are contained within cycles. A distinction is made between graph augmentation (edge addition), and graph enlargement (vertex addition).

The particular problem addressed here is the enlarging of a digraph which is an abstraction defined in the "shoe matching problem" and represents people who require different sizes of shoes. To be able to satisfy all of the participants, every node (person) in the digraph must be contained in at least one cycle. This paper looks at ways to improve on the original approach to graph enlargment. It redefines the cost model used in the original work, presents three improvements to the original approach and shows that these approaches do indeed offer benefits in terms of the number of nodes needed to solve the problem and/or the speed of enlargement.

Execution
===
Run any of the main_.py programs. The difference between vanilla, cost, matrix, etc. will be more clear after reading the conference proceeding linked above. The augmentor_.py programs do the work, while files like tarjan.py, tiernan.py, generator.py, rcomb.py, lcs.py are all helper functions.
