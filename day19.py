class Rule:
    def __init__(self, s: str):
        p = s.find(':')
        if p == -1:
            self.condition = None 
            self.next = s 
        else:
            self.condition = s[:p].replace('=', '==')
            self.next = s[p + 1:]
            
    def __str__(self) -> str:
        return f"Rule({self.condition}:{self.next})"
    
    def __repr__(self) -> str:
        return str(self)
    
    

input_file = open("day19.in", "r")

workflows, parts = input_file.read().split("\n\n")

workflows = workflows.split("\n")
workflows_dict = {} # maps names to idx in the workflows list
for w in range(len(workflows)):
    workflow = workflows[w]
    l = workflow.find('{')
    name = workflow[:l]
    rules = workflow[l + 1:-1].split(',')
    rules = [Rule(r) for r in rules]
    workflows[w] = {"name": name,"rules" : rules}
    workflows_dict[name] = w
    
workflows.append({"name": "A", "rules": []})
workflows.append({"name": "R", "rules": []})
workflows_dict["A"] = len(workflows) - 2
workflows_dict["R"] = len(workflows) - 1

# explore the graph
start = workflows_dict["in"]
finish = workflows_dict["A"]

visited = [0] * len(workflows)
is_tree = True
is_dag = True
topo_order = []

def dfs(node):
    global is_tree, is_dag
    visited[node] = 1
    for rule in workflows[node]["rules"]:
        new_node = workflows_dict[rule.next]
        if visited[new_node] == 0:
            dfs(new_node)
        elif visited[new_node] == 1:
            print("cycle")
            is_dag = False
            is_tree = False
        else:
            is_tree = False
    visited[node] = 2
    topo_order.append(node)

dfs(start)
print("is_tree", is_tree)
print("is_dag", is_dag)


dp = [0] * len(workflows)
dp[finish] = 1

reverse_graph = [[] for _ in range(len(workflows))]
for node in range(len(workflows)):
    for rule in workflows[node]["rules"]:
        new_node = workflows_dict[rule.next]
        reverse_graph[new_node].append((node, rule))

for node in topo_order:
    if dp[node] == 0:
        continue 
    for (new_node, rule) in reverse_graph[node]:
        dp[new_node] += dp[node]

print(dp[start])

answer = 0

def backtrack(node: int, ranges : dict):
    global answer 
    if node == finish:
        current = 1
        for key in 'xmas':
            current *= ranges[key][1] - ranges[key][0] + 1
        answer += current
        return
    
    for rule in workflows[node]["rules"]:
        if rule.condition is not None:
            p = rule.condition.find('<')
            if p == -1:
                p = rule.condition.find('>')
            key = rule.condition[:p]
            value = int(rule.condition[p + 1:])
        
        
        new_node = workflows_dict[rule.next]
        
        if dp[new_node] > 0:
            if rule.condition is None:
                backtrack(new_node, ranges)
            else:
                l, r = ranges[key]
                new_ranges = ranges.copy()
                if rule.condition[p] == '<':
                    new_ranges[key] = (l, min(r, value - 1))
                else:
                    new_ranges[key] = (max(l, value + 1), r)
                backtrack(new_node, new_ranges)
        
        if rule.condition is None:
            break 
               
        l, r = ranges[key]
        if rule.condition[p] == '<':
            ranges[key] = (max(l, value), r)
        elif rule.condition[p] == '>':
            ranges[key] = (l, min(r, value))
        
    
backtrack(start, {'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)})

print(answer)

input_file.close()