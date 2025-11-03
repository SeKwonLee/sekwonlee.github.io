---
title: "PMAL: Enabling Lightweight Adaptation of Legacy File Systems on Persistent Memory Systems"
collection: publications
permalink: /publications/ispass17
date: 2017-04-24
venue: 'The 2017 IEEE International Symposium on Performance Analysis of Systems and Software (ISPASS 2017)'
citation: 'Hyunsub Song, Young Je Moon, <strong>Se Kwon Lee</strong>, and Sam H. Noh, <strong>PMAL: Enabling Lightweight Adaptation of Legacy File Systems on Persistent Memory Systems</strong>, Proceedings of <i>the 2017 IEEE International Symposium on Performance Analysis of Systems and Software</i> (<strong>ISPASS 2017</strong>).'
---
[[paper]](http://sekwonlee.github.io/files/ispass17.pdf)

## Abstract
The advent of Persistent Memory (PM), which is anticipated to have byte-addressable access latency in par with DRAM and yet nonvolatile, has stepped up interest in using PM as storage. Hence, PM storage targeted file systems are being developed under the premise that legacy file systems are suboptimal on memory bus attached PM-based storage. However, many years of time and effort are ingrained in legacy file systems that are now time-tested and mature. Simply scrapping them altogether may be unwarranted. In this paper, we look into how we can leverage the maturity ingrained in legacy file systems to the fullest, while, at the same time, reaping the high performance offered by PM. To this end, we first go through a thorough analysis of legacy Ext4 file systems, and compare it with NOVA, PMFS, and Ext4 with DAX extension, which are new PM file systems available in Linux. Based on these analyses, we then propose the Persistent Memory Adaptation Layer (PMAL) module that is lightweight (roughly 180 LoC) and can easily be integrated into legacy file systems to take advantage of PM storage. Using Ext4, we show that the performance of PMAL integrated Ext4 is in par with PM file systems for the Filebench and key-value store benchmarks.
