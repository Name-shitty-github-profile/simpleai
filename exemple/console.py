# V1
import simpleai, os
key = os.environ["key"]
ctx = simpleai.context("You are a server in a bar")
while True:
  content = input("Human :")
  ctn, ctx = simpleai.get(content, "Human", ctx, key)
  print(ctn)
