---
title: "iDO: Compiler-Directed Failure Atomicity for Nonvolatile Memory"
collection: publications
permalink: /publications/micro18
date: 2018-10-20
venue: 'The 51st Annual IEEE/ACM International Symposium on Microarchitecture (MICRO 2018)'
citation: 'Qingrui Liu, Joseph Izraelevitz, <strong>Se Kwon Lee</strong>, Michael L. Scott, Sam H. Noh, and Changhee Jung, <strong>iDO: Compiler-Directed Failure Atomicity for Nonvolatile Memory</strong>, Proceedings of <i>the 51st Annual IEEE/ACM International Symposium on Microarchitecture</i> (<strong>MICRO 2018</strong>).'
---
[[paper]](http://sekwonlee.github.io/files/micro18_ido.pdf)

## Abstract
This paper presents iDO, a compiler-directed approach to failure atomicity with nonvolatile memory. Unlike most prior work, which instruments each store of persistent data for redo or undo logging, the iDO compiler identifies idempotent instruction sequences, whose re-execution is guaranteed to be side effect-free, thereby eliminating the need to log every persistent store. Using an extension of prior work on JUSTDO logging, the compiler then arranges, during recovery from failure, to back up each thread to the beginning of the current idempotent region and re-execute to the end of the current failure-atomic section. This extension transforms JUSTDO logging from a technique of value only on hypothetical future machines with nonvolatile caches into a technique that also significantly outperforms state-of-the art lock-based persistence mechanisms on current hardware during normal execution, while preserving very fast recovery times.
