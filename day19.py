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
    
parts = parts.strip().split('\n')
for idx in range(len(parts)):
    part = parts[idx]
    part = part[1:-1].split(",")
    d = {}
    
    for c in part:
        d[c[0]] = c[2:]
    parts[idx] = d
    
def evaluate(part: dict, condition: str) -> bool:
    return eval(part[condition[0]] + condition[1:])

def check_part(part, workflow_id):
    worflow = workflows[workflow_id]
    rules = worflow["rules"]
    for rule in rules:
        if rule.condition is None:
            if rule.next in ['A', 'R']:
                return rule.next== 'A'
            return check_part(part, workflows_dict[rule.next])
        if evaluate(part, rule.condition):
            if rule.next in ['A', 'R']:
                return rule.next == 'A'
            return check_part(part, workflows_dict[rule.next])
    

ans = 0
for part in parts:
    if check_part(part, workflows_dict['in']):
        for values in part.values():
            ans += int(values)
            
print(ans)

    
input_file.close()