class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = []
        for i in range(n + 1):
            adj.append([])
        for time in times:
            adj[time[0]].append([time[1], time[2]])
        dist = {}
        for i in range(1, n + 1):
            dist[i] = 10 ** 9
        dist[k] = 0
        
        def dfs(v, cur):
            for i in range(len(adj[v])):
                u = adj[v][i][0]
                w = adj[v][i][1]
                if(cur + w) < dist[u]:
                    dist[u] = cur + w
                    dfs(u, cur + w)
        
        dfs(k, 0)
        if max(dist.values()) != 10 ** 9:
            return max(dist.values())
        else:
            return -1
    
   

                