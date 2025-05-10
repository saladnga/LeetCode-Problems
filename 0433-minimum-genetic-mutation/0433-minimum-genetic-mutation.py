class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        graph = defaultdict(list)
        bank.append(startGene)
        for gene in bank:
            for i in range(len(gene)):
                pattern = gene[:i] + "*" + gene[i + 1:]
                graph[pattern].append(gene)
        seen = {startGene}
        queue = deque([startGene])
        res = 0
        while queue:
            for _ in range(len(queue)):
                gene = queue.popleft()
                if gene == endGene:
                    return res
                for i in range(len(gene)):
                    pattern = gene[:i] + "*" + gene[i + 1:]
                    for neighbor in graph[pattern]:
                        if neighbor not in seen:
                            seen.add(neighbor)
                            queue.append(neighbor)
            res += 1
        return -1