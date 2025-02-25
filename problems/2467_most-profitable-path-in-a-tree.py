# 2467. Most Profitable Path in a Tree
#
# There is an undirected tree with n nodes labeled from 0 to n - 1, rooted at node 0. You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.
# At every node i, there is a gate. You are also given an array of even integers amount, where amount[i] represents:
# - the price needed to open the gate at node i, if amount[i] is negative, or,
# - the cash reward obtained on opening the gate at node i, otherwise.
# The game goes on as follows:
# - Initially, Alice is at node 0 and Bob is at node bob.
# - At every second, Alice and Bob each move to an adjacent node. Alice moves towards some leaf node, while Bob moves towards node 0.
# - For every node along their path, Alice and Bob either spend money to open the gate at that node, or accept the reward. Note that:
#   - If the gate is already open, no price will be required, nor will there be any cash reward.
#   - If Alice and Bob reach the node simultaneously, they share the price/reward for opening the gate there. In other words, if the price to open the gate is c, then both Alice and Bob pay c / 2 each. Similarly, if the reward at the gate is c, both of them receive c / 2 each.
# - If Alice reaches a leaf node, she stops moving. Similarly, if Bob reaches node 0, he stops moving. Note that these events are independent of each other.
# Return the maximum net income Alice can have if she travels towards the optimal leaf node.

from collections import deque
from typing import List


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj = [[] for _ in amount]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        bob_steps = dict()
        bob_path = [None for _ in amount]
        deq = deque([(bob, 0)])
        while deq:
            curr, step = deq.pop()
            bob_steps[curr] = step
            if curr == 0:
                break

            for next_node in adj[curr]:
                if next_node in bob_steps:
                    continue
                bob_path[next_node] = curr
                deq.append((next_node, step + 1))

        bob_visited = set([bob])
        curr = 0
        while curr != bob:
            bob_visited.add(curr)
            curr = bob_path[curr]

        for node in range(len(amount)):
            if node in bob_visited:
                continue
            bob_steps.pop(node, None)

        result = float("-inf")
        deq = deque([(0, 0, 0)])
        visited = [False for _ in amount]
        while deq:
            curr, step, score = deq.popleft()
            if curr not in bob_steps or step < bob_steps[curr]:
                score += amount[curr]
            elif bob_steps[curr] == step:
                score += amount[curr] // 2

            if len(adj[curr]) == 1 and curr != 0:
                result = max(result, score)
                continue

            for next_node in adj[curr]:
                if visited[next_node]:
                    continue
                visited[next_node] = True
                deq.append((next_node, step + 1, score))

        return result


assert Solution().mostProfitablePath(
    [[0, 2], [1, 4], [1, 6], [2, 4], [3, 6], [3, 7], [5, 7]],
    4,
    [-6896, -1216, -1208, -1108, 1606, -7704, -9212, -8258]
) == -34998

assert Solution().mostProfitablePath(
    [[0, 2], [0, 5], [1, 3], [1, 5], [2, 4]],
    4,
    [5018, 8388, 6224, 3466, 3808, 3456]
) == 20328


assert Solution().mostProfitablePath(
    [[0, 1], [1, 2], [1, 3], [3, 4]],
    3,
    [-2, 4, 2, -4, 6]
) == 6

assert Solution().mostProfitablePath(
    [[0, 1]],
    1,
    [-7280, 2350]
) == -7280
