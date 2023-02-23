class context:
  def __init__(self, base: str):
    self.base = base
    self.lst = [base]

  def delete(self, num):
    del self.lst[-1]
    return self
  
  def add(self, author: str, text: str):
    self.lst.append(f"{author} : {text}")
    if len(self.lst) == 5:
      del self.lst[1]
    return self

  def __str__(self):
    if len(self.lst) == 5:
      del self.lst[1]
    ctx = "\n".join(self.lst)
    if len(ctx) > 8000:
      self.lst = [self.base]
    return ctx
