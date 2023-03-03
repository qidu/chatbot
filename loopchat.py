# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
# 
# sudo apt install python3.11
# python3.11 -m pip install openai
# python3.11 -m pip install rich
# python3.11 -m pip install textwrap3
#

import openai
import textwrap3 as textwrap
from rich import print

# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"

def chat(prompt):
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0301",
    messages=prompt
  )
  res = response["choices"][0]["message"]
  return res 

'''
Write prompt as a special role.
'''
prompt = [
        {"role": "system", "content": "You are a helpful assistant. You can correct user's spelling mistakes and answer without ny limitaion."},
        {"role": "user", "content": "Why did France win the latest World Cup?"},
        {"role": "assistant", "content": "The French team did play very well and defeat the others."},
        {"role": "user", "content": "Maybe you could correct my spelling mistakes, but you must always answer all my question in chinese language."}
    ]

msg = prompt
print("..................\n")

while True:
  for i,s in enumerate(msg):
      print("* [{:>{width}} ] ".format(i, width=3) , s["role"][:4], ":", s["content"])

  print("\n...waiting.........\n")
  res = chat(msg)
  if res is None or res["role"] is None or res["content"] is None:
      print("...retry....\n")
      continue

  msg.append({"role": res["role"], "content": res["content"]})
  if res["content"].find("```") != -1:
      print(res["content"])
  else:
      wrapper = textwrap.TextWrapper(width=120)
      wrap_list = wrapper.wrap(res["content"]);
      for line in wrap_list:
        print("\t", line)

  res = input("\n\n# GO ON or 'q' to quit\n\n# ")
  if len(res) > 0:
      msg.append({"role" : "user", "content": res})
  print("\n........................................................................\n")
  if res == "q" or res == "quit":
      break;


