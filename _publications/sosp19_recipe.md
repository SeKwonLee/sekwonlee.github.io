---
title: "RECIPE : Converting Concurrent DRAM Indexes to Persistent-Memory Indexes"
collection: publications
permalink: /publications/sosp19_recipe
venue: 'The 27th ACM Symposium on Operating Systems Principles (SOSP 2019)'
date: 2019-10-27
citation: '<strong>Se Kwon Lee</strong>, Jayashree Mohan, Sanidhya Kashyap, Taesoo Kim, and Vijay Chidambaram, <strong>RECIPE : Converting Concurrent DRAM Indexes to Persistent-Memory Indexes</strong>, Proceedings of <i>the 27th ACM Symposium on Operating Systems Principles </i> (<strong>SOSP 2019</strong>).'
---
[[paper]](https://sekwonlee.github.io/files/sosp19-recipe.pdf)
[[extended version(arXiv)]](https://arxiv.org/abs/1909.13670)
[[code]](https://github.com/utsaslab/RECIPE)
[[slides]](https://sekwonlee.github.io/files/sosp19-recipe-slides.pdf)
[[poster]](https://sekwonlee.github.io/files/sosp19-recipe-poster.pdf)

## Abstract
We present Recipe, a principled approach for converting concurrent DRAM indexes into crash-consistent indexes for persistent memory (PM). The main insight behind Recipe is that isolation provided by a certain class of concurrent in-memory indexes can be translated with small changes to crash-consistency when the same index is used in PM. We present a set of conditions that enable the identification of this class of DRAM indexes, and the actions to be taken to convert each index to be persistent. Based on these conditions and conversion actions, we modify five different DRAM indexes based on B+ trees, tries, radix trees, and hash tables to their crash-consistent PM counterparts. The effort involved in this conversion is minimal, requiring 30–200 lines of code. We evaluated the converted PM indexes on Intel DC Persistent Memory, and found that they outperform state-of-the-art, hand-crafted PM indexes in multi-threaded workloads by up-to 5.2×. For example, we built P-CLHT, our PM implementation of the CLHT hash table by modifying only 30 LOC. When running YCSB workloads, P-CLHT performs up to 2.4× better than Cacheline-Conscious Extendible Hashing (CCEH), the state-of-the-art PM hash table.
