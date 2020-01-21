add = lambda n : lambda x : x + n
sub = lambda n : lambda x : x - n
mul = lambda n : lambda x : x * n
div = lambda n : lambda x : int(x / n) if x % n == 0 else None
exp = lambda n : lambda x : x ** n
SUM = lambda x : 0 if x == 0 else abs(x) * sum([int(f) for f in list(str(abs(x)))]) // x
Inv10 = lambda x : 0 if x == 0 else abs(x) * int(''.join([f if f == '0' else str(10 - int(f)) for f in list(str(abs(x)))])) // x
insert = lambda n : lambda x : int(str(x) + str(n))
shift = lambda d : lambda x : int(str(x)[-1] + str(x)[:len(str(x)) - 1]) if d == 1 else int(str(x)[1:] + str(x)[0])
mirror = lambda x : int(str(x) + str(x)[::-1])
reverse = lambda x : abs(x) * int(str(abs(x))[::-1]) // x
delete = lambda x : x // 10
pm = lambda x : -x
def replace(n, m):
  def rep(x):
    r, l, s = str(abs(x)), len(str(n)), str(abs(x))
    for i in range(0, len(s) - l + 1, l):
      if s[i:i + l] == str(n):
        r = r[0:i] + str(m) + s[i + l:]
    return abs(x) * int(r) // x
  return rep
stored = None
def store(x):
  global stored
  stored = x
  return x
insStore = lambda x : int(str(x) + str(stored))
def dyn(f, df):
  if f(1) == f(3) - 2 or f(.5) == None or f(1) * 5 == f(5) or "14" + str(f(12))[2:] == f(14):
    return lambda x : df(f(x))
  return f
