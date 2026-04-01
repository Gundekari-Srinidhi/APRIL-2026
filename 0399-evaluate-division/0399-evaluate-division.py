class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)
        v = []
        for i in range(n):
            for j in equations[i]:
                v.append(j)
        v=sorted(set(v))
        d = {}
        for i in range(len(v)):
            d[v[i]]=i
        adj = []
        for _ in range(len(v)):
            adj.append([])
        i = 0
        for n,m in equations:
            adj[d[n]].append((d[m],values[i]))
            adj[d[m]].append((d[n],1/values[i]))
            i+=1
                
        l = []  
        for n,m in queries:
            if n not in d or m not in d:
                l.append(-1.0)
                continue
            if n == m:
                l.append(1.0)
                continue
            
            q = []
            q.append((d[n],1.0))
            v = set()
            found = -1.0
            while q:
                node,prd= q.pop()
                for i,cost in adj[node]:
                    if node in v:
                        continue
                    v.add(node)
                    if node == d[m]:
                        found = prd
                        break
                    for j,cost in adj[node]:
                        if j not in v:
                            q.append((j,prd*cost))
            l.append(found)
        return l


        