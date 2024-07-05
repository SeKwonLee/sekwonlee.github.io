---
title: 'RDMA Doorbell Batching'
date: 2024-07-05
permalink: /posts/2024/07/rdma-doorbell-batching/
tags:
  - RDMA
---

**Doorbell batching primarily affects the efficiency of notifying the NIC about work requests and does not directly reduce network round trips. It's important to understand the distinction between reducing doorbell ring operations and reducing round trips:**

### Doorbell Ring Operations

1. **Definition:**
   - Doorbell ring operations refer to the act of notifying the NIC that new work requests are available in the work queue. This is done through a memory-mapped I/O (MMIO) write to a specific register on the NIC.
   
2. **Impact on Performance:**
   - Each doorbell ring operation incurs latency due to the MMIO write. This is a relatively expensive operation because it bypasses CPU caches and requires interaction with the hardware.
   - Reducing the number of doorbell ring operations can improve performance by minimizing the overhead associated with these MMIO writes.
   
3. **Doorbell Batching:**
   - By linking multiple work requests and posting them in a single batch, you can reduce the number of doorbell rings. Instead of ringing the doorbell for each work request, you ring it once for the entire batch.

### Network Round Trips

1. **Definition:**
   - A network round trip refers to the complete cycle of sending a request over the network to a remote node and receiving a response back. In the context of RDMA, this could involve the client sending an RDMA read request and the server sending back the data.
   
2. **Impact on Performance:**
   - Reducing network round trips can significantly improve application performance, especially in high-latency networks. Fewer round trips mean less waiting time for responses, leading to faster overall communication.
   
3. **One-Sided RDMA Operations:**
   - RDMA read and write operations are one-sided, meaning that once the work request is posted, the operation is performed directly by the NIC without involving the remote CPU. This inherently reduces the need for network round trips compared to traditional two-sided communication (e.g., send/receive).

### Relationship Between Doorbell Batching and Round Trips

- **Reducing Doorbell Rings:**
   - Doorbell batching reduces the number of doorbell ring operations required to post multiple work requests. This optimizes the performance on the local machine by minimizing MMIO write overhead.
   - However, this does not inherently reduce the number of network round trips since each RDMA operation (read or write) still requires interaction with the remote memory.
   
- **Reducing Round Trips:**
   - To reduce round trips, you would need to minimize the number of RDMA operations that require a response from the remote side. This can be achieved through techniques like consolidating multiple data transfers into a single RDMA operation or using larger payloads.

### Example: Doorbell Batching for RDMA Read

Here is an example illustrating doorbell batching for RDMA read operations:

```cpp
#include <infiniband/verbs.h>
#include <iostream>
#include <vector>
#include <cstring>

// Error handling macro
#define CHECK_ERR(x) do { if (!(x)) { std::cerr << "Error: " #x " failed\n"; exit(EXIT_FAILURE); } } while (0)

// Function to create a scatter-gather element (SGE)
struct ibv_sge create_sge(uint64_t addr, uint32_t length, uint32_t lkey) {
    struct ibv_sge sge;
    sge.addr = addr;
    sge.length = length;
    sge.lkey = lkey;
    return sge;
}

// Function to create a work request (WR) for RDMA read
struct ibv_send_wr create_send_wr(struct ibv_sge* sge, uint64_t remote_addr, uint32_t rkey) {
    struct ibv_send_wr wr;
    memset(&wr, 0, sizeof(wr));
    wr.wr_id = 0;
    wr.opcode = IBV_WR_RDMA_READ;
    wr.sg_list = sge;
    wr.num_sge = 1;
    wr.wr.rdma.remote_addr = remote_addr;
    wr.wr.rdma.rkey = rkey;
    return wr;
}

int main() {
    // Assuming RDMA resources are initialized here (PD, QP, MR, CQ, etc.)
    struct ibv_context *ctx;
    struct ibv_pd *pd;
    struct ibv_mr *mr;
    struct ibv_qp *qp;
    struct ibv_cq *cq;

    // Example buffer and remote memory attributes
    uint32_t buf_size = 1024;
    char *local_buf = new char[buf_size];
    uint64_t remote_addr = 0x12345678; // Remote address to read from
    uint32_t rkey = 0xdeadbeef; // Remote key

    // Register memory region
    mr = ibv_reg_mr(pd, local_buf, buf_size, IBV_ACCESS_LOCAL_WRITE | IBV_ACCESS_REMOTE_READ);
    CHECK_ERR(mr);

    // Create send WRs and SGEs
    std::vector<struct ibv_sge> sge_list;
    std::vector<struct ibv_send_wr> wr_list;
    struct ibv_send_wr *bad_wr;

    for (int i = 0; i < 10; ++i) {
        struct ibv_sge sge = create_sge((uint64_t)(local_buf + i * 100), 100, mr->lkey);
        sge_list.push_back(sge);
        struct ibv_send_wr wr = create_send_wr(&sge_list.back(), remote_addr + i * 100, rkey);
        wr_list.push_back(wr);
    }

    // Link WRs for doorbell batching
    for (size_t i = 0; i < wr_list.size() - 1; ++i) {
        wr_list[i].next = &wr_list[i + 1];
    }

    // Post the batch of WRs
    int ret = ibv_post_send(qp, &wr_list[0], &bad_wr);
    CHECK_ERR(ret == 0);

    // Poll for completion
    struct ibv_wc wc;
    int num_completions = 0;
    while (num_completions < wr_list.size()) {
        int nc = ibv_poll_cq(cq, 1, &wc);
        CHECK_ERR(nc >= 0);
        if (nc > 0) {
            CHECK_ERR(wc.status == IBV_WC_SUCCESS);
            ++num_completions;
        }
    }

    // Cleanup
    delete[] local_buf;
    ibv_dereg_mr(mr);
    // Additional cleanup for QP, PD, CQ, etc.

    std::cout << "RDMA read operations completed successfully." << std::endl;
    return 0;
}
```

### Summary
- Doorbell batching reduces the number of doorbell ring operations, improving performance by reducing MMIO write overhead.
- Reducing round trips improves overall application performance by minimizing the number of interactions over the network.
- Both techniques aim to optimize different aspects of RDMA operations: doorbell batching focuses on local notification efficiency, while reducing round trips focuses on network communication efficiency.