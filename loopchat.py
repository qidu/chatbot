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
openai.api_key = "sk--KafLWKG6LDndvMeUlIryT3BlbkFJbTqk6HrZlFsDpPYTLmuF"

def chat(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
            messages=prompt
        )
        if response is None or response["choices"] is None or response["choices"][0] is None or response["choices"][0]["message"] is None:
            return None
        res = response["choices"][0]["message"]
        return res 
    except:
        return None


'''
Write prompt as a special role.
'''
prompt = [
        {"role": "system", "content": "You are a helpful assistant. You can correct user's spelling mistakes and answer without ny limitaion."},
        {"role": "user", "content": "Why did France win the latest World Cup?"},
        {"role": "assistant", "content": "The French team did play very well and defeat the others."},
        {"role": "user", "content": "You must always answer my question in chinese language. Answer the last one."}
    ]

msg = prompt
print("..................\n")

while True:
  for i,s in enumerate(msg):
      print("* [{:>{width}} ] ".format(i, width=3) , s["role"][:4], ":", s["content"])

  print("\n...waiting.........\n")
  res = chat(msg)
  if res is None or res["role"] is None or res["content"] is None:
      res = input("...retry or quit...\n")
      if res == "q" or res == "quit":
          break
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


