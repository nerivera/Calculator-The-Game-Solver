from operations import *
def solve(start, goal, moves, ops, dynOps = [], portals = []):
  if moves < 0:
    return solve(goal, start, -moves, ops, dynOps, portals)
  if moves == 0:
    return "" if start == goal else "-1"
  for i in range(len(ops)):
    if ops[i](start) == None:
      continue
    rest = solve(ops[i](start), goal, moves - 1, ops) 
    if(rest != "-1"):
      return str(i) + " " + rest
    i += 1
  return "-1"

# Example (uncomment):
# print(solve(12, 26, 5, [delete, SUM, store, insStore, Inv10]))
