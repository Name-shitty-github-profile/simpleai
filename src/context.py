class context:
  def __init__(self, base: str, max_conv_length: int):
    self.base = base
    self.lst = [base]
    self.max_conv_length = max_conv_length

  def delete(self, num):
    del self.lst[num]
    return self
  
  def add(self, author: str, text: str):
    self.lst.append(f"{author} : {text}")
    if len(self.lst) == 5:
      del self.lst[1]
    return self

  def __str__(self):
    if len(self.lst) == self.max_conv_length:
      del self.lst[1]
    ctx = "\n".join(self.lst)
    if len(ctx) > 8000:
      self.lst = [self.base]
    return ctx
