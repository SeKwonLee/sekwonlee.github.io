---
title: "SplitFS: Reducing Software Overhead in File Systems for Persistent Memory"
collection: publications
permalink: /publications/sosp19_splitfs
venue: 'The 27th ACM Symposium on Operating Systems Principles (SOSP 2019)'
date: 2019-10-27
citation: 'Rohan Kadekodi, <strong>Se Kwon Lee</strong>, Sanidhya Kashyap, Taesoo Kim, Aasheesh Kolli and Vijay Chidambaram, <strong>SplitFS: Reducing Software Overhead in File Systems for Persistent Memory</strong>, Proceedings of <i>the 27th ACM Symposium on Operating Systems Principles </i> (<strong>SOSP 2019</strong>).'
---
[[paper]](https://sekwonlee.github.io/files/sosp19-splitfs.pdf)
[[code]](https://github.com/utsaslab/SplitFS)
[[slides]](https://sekwonlee.github.io/files/sosp19-splitfs-slides.pdf)

## Abstract
We present SplitFS, a file system for persistent memory (PM) that reduces software overhead significantly compared to state-of-the-art PM file systems. SplitFS presents a novel split of responsibilities between a user-space library file system and an existing kernel PM file system. The user-space library file system handles data operations by intercepting POSIX calls, memory-mapping the underlying file, and serving the read and overwrites using processor loads and stores. Metadata operations are handled by the kernel PM file system (ext4 DAX). SplitFS introduces a new primitive termed relink to efficiently support file appends and atomic data operations. SplitFS provides three consistency modes, which different applications can use choose from without interfering with each other. SplitFS reduces software overhead by up-to 4x compared to the NOVA PM file system, and 17x compared to ext4 DAX. On a number of micro-benchmarks and real applications such as the LevelDB key-value store running the YCSB benchmark, SplitFS increases application performance by 2x compared to ext4 DAX and NOVA while providing similar consistency guarantees.
