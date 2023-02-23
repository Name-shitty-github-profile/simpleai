# Talking with an AI in your code is hard? Isn't it?
Not anymore with this module !
<br>
You can talk with an AI in a couple of lines only !!!!
### The steps
* You just have to get an openai api key !
* Clone this git
* Import the module
* Make a varible of the class named AI
* Talk with the AI using the talk function and there you go!
<br>
Super simple right?
<br>
Talking with an AI in your code has never been easier !

<br><br><br>
The AI can be anythig, a friend, a girlfriend, anything !
<br>
You just have to provide a base and the AI is yours you can do whatever you want with it!

## The main class
Everything in this module works with this class
<br>
This class is a really simple class that will allows you to chat with an IA really easily
<br>
Here's an example of code to chat with the AI in the console

```python
import simpleai, os
ai = simpleai.ai("You are a server in a bar", [os.environ["key"]])
while True:
  content = input("Human :")
  print(ai.talk(content, "Human"))
```

## Methods
### talk
This function is for talking with the AI
<br>
The first argument is for the content that you wanna send
<br>
The second argument is the name of the person that says that
<br>
Example
```python
content = MyAi.talk("Hello!", "Angelica")
print(content)
```
Console
```
Hello, how are you?
```
### add_conv
This function is to add more data or a conversation to the AI
<br>
Conv structure
<br>
A list of dicts with this structure
```json
{"author": "The author of the message", "content": "The content of the message"}
```
