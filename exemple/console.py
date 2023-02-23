# V1
import simpleai, os
ai = simpleai.ai("You are a server in a bar", [os.environ["key"]])
while True:
  content = input("Human :")
  print(ai.talk(content, "Human"))
