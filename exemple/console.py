import simpleai, os
key = os.environ["key"]
ctx = simpleai.context("You are a server in a bar")
while True:
  content = input("Human :")
  print(simpleai.get(content, "Human", ctx, key))
