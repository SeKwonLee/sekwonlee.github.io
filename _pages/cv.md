---
layout: archive
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

[<span style="color:navy">[Download CV]</span>](http://sekwonlee.github.io/files/cv.pdf)

Research interest
=====
* <b>Computer Systems</b>
  * <b>Areas:</b> Storage and File systems, Distributed systems, Operating systems, Database systems
  * <b>Focus:</b> Next‑generation systems for emerging memory (PM) and disaggregation (RDMA, CXL) technologies
      * Designing elastic, high‑performance, scalable, crash‑recoverable key‑value stores
      * Designing concurrent, crash‑consistent index structures for storage systems
      * Improving the performance and reliability of file systems

Education
======
* <b>Ph.D.</b> in Computer Science, <b>The University of Texas at Austin</b>, 2023
  * <b>Advisor</b>: Vijay Chidambaram
* <b>M.S.</b> in Computer Science Engineering, <b>UNIST (Ulsan National Institute of Science & Technology)</b>, 2018
  * <b>Advisor</b>: Sam H. Noh
* <b>B.S.</b> in Computer Engineering, <b>Hongik University</b>, 2015

Work experience
======
* <b>Research Engineer</b>, 01.2024~Present
  * Hewlett Packard Labs, Austin, TX, US

* <b>Research Intern</b>, 05.2021~08.2021
  * Microsoft Research, Redmond, WA, US
  * Duties included: Scaling out AMBROSIA, a general framework to build resilient distributed systems
  * Mentor: Jonathan Goldstein

* <b>Research Associate Intern</b>, 06.2019~08.2019
  * Hewlett Packard Labs, Palo Alto, CA, US
  * Duties included: Designing far-memory data structures optimized for one-sided operation
  * Mentors: Kimberly Keeton and Sharad Singhal

* <b>Researcher</b>, 03.2018~07.2018
  * UNIST (Ulsan National Institute of Science & Technology), Ulsan, South Korea
  * Duties included: Providing the compiler-directed crash consistency for PM-based systems
  * Supervisor: Sam H. Noh

* <b>Research Associate Intern</b>, 06.2017~09.2017
  * Hewlett Packard Labs, Palo Alto, CA, US
  * Duties included: Designing DRAM cache for key-value stores working on Fabric-attached memory
  * Mentors: Kimberly Keeton, Haris Volos, and Yupu Zhang

* <b>Researcher</b>, 10.2015~02.2016
  * UNIST (Ulsan National Institute of Science & Technology), Ulsan, South Korea
  * Duties included: Analyzing performance implications of index structures in PM‑based file systems
  * Supervisor: Sam H. Noh

* <b>Signaller</b>, 08.2010~05.2012
  * ROK DCC, Republic of Korea Armed Forces

Honors & Awards
======
* <b>UT Austin Dean's Prestigious Fellowship Supplement</b>, 2022
* <b>UT Austin Dean's Prestigious Fellowship Supplement</b>, 2021
* <b>2021 Microsoft Research PhD Fellowship</b>, 2021~2023

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

Skills
======
* <b>Languages</b>
  * C, C++, Python, x86 assembly, Bash script
* <b>System programming</b>
  * Linux kernel, Memcached, Tizen
* <b> Tools and libraries</b>
  * Kubernetes, Docker, ZeroMQ, protobuf, YCSB benchmarks

Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

Professional Activities
======
* PC Member for SoCC (2024)
* Reviewer for IEEE Transactions on Knowledge and Data Engineering, ACM Transactions on Architecture and Code Optimization, ACM Transactions on Storage (2024)
* Reviewer for IEEE Transactions on Computers (2023)
* Invited talk at IBM Research (May. 2023). Data‑Intensive Systems for Emerging Memory and Disaggregation Technologies
* Volunteered as Slack Co‑Chair for SOSP 2021
* Invited talk at Intel Labs (Oct. 2020). RECIPE : Converting Concurrent DRAM Indexes to Persistent‑Memory Indexes
