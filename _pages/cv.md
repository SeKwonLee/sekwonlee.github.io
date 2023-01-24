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
  * <b>Areas:</b> Storage and File systems, Distributed Systems, Database systems, Operating Systems
  * <b>Focus:</b> Persistent Memory (PM) & Disaggregated Persistent Memory (DPM) aware systems design
      * Designing an elastic and high-performance key-value store for DPM based on RDMA and CXL interconnects
      * Designing index structures for PM-based storage systems
      * Improving the performance and reliability of PM-based file systems

Education
======
* <b>Ph.D.</b> in Computer Science, <b>The University of Texas at Austin</b>, Fall 2018 ~ Summer 2023 (expected)
  * <b>Advisor</b>: Vijay Chidambaram
* <b>M.S.</b> in Computer Science Engineering, <b>UNIST (Ulsan National Institute of Science & Technology)</b>, 2018
  * <b>Advisor</b>: Sam H. Noh
  * Visiting student in Virginia Tech (2017.03 - 2017.05)
      * Co-research advised by Prof. Changhee Jung
      * Participating in the project of a new fault-tolerant programming model for PM
* <b>B.S.</b> in Computer Engineering, <b>Hongik University</b>, 2015

Work experience
======
* <b>Research Intern</b>, 05.2021~08.2021
  * Microsoft Research, Redmond, WA, US
  * Duties included: Elastically scaling out AMBROSIA
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
  * Duties included: Analyzing PM-based file system (PMFS) and evaluating its performance
  * Supervisor: Sam H. Noh

* <b>Republic of Korea Army</b>, 08.2010~05.2012

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

Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

Other Activities
======
* <b>Student Volunteer (Slack Chair)</b>, The 28th ACM Symposium on Operating Systems Principles (SOSP 2021)
* Presented RECIPE: Converting Concurrent DRAM Indexes to Persistent-Memory Indexes at Intel Labs (Oct. 2020)
