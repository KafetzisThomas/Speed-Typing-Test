#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: Speed Typing Test (https://github.com/KafetzisThomas/Speed-Typing-Test)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)

import random, time

phrases = [
  "python is a high-level general-purpose programming language",
  "eminem made his debut in the film industry with the film 8 Mile",
  "eminem is among the best-selling music artists of all time"
]

print("\n\n> Test your typing skills")
computer_text = random.choice(phrases)

print(f"\nPhrase:\t\t{computer_text}")

start = time.time()
user_text = input("\n\nStart typing here: ")
end = time.time()
time_elapsed = round(end-start)

if user_text == computer_text:
  if time_elapsed <= 10:
    print(f"You passed {time_elapsed} seconds. Pretty good.")
  elif time_elapsed <= 15:
    print(f"You passed {time_elapsed} seconds. You're too close.")
  elif time_elapsed <= 20:
    print(f"You passed {time_elapsed} seconds. You need more exercise.")
  else:
    print(f"You passed {time_elapsed} seconds. Pretty bad.")
else:
  print("Try again.")
