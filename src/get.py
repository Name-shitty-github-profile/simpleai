import openai
from .context import context

def get(prompt: str, username: str, ctx: context, key: str) -> tuple[str, context]:
  openai.api_key = key
  ctx.add(username, prompt)
  try:
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=str(ctx) + '\nAI : ',
      temperature=0.5,
      max_tokens=1085,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )["choices"][0]['text']
  except Exception as e:
    print(e)
    ctx.delete(-1)
    return get(prompt, username, ctx, key)
  ctx.add("AI", prompt)
  return response, ctx
