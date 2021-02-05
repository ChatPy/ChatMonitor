# DONE, BUT UNTESTED

# Take this as a example if you want to write your own extension.
# The extension wiki will be released soon.

import threading
import time
template_file = open("template.html")
global template
global recordings
template = template_file.read().split()
recordings = []
def record(message):
  global recordings
  recordings.append(message)
def extension():
  global recordings
  length = 0
  start_time = 0
  user = 0
  message = 0
  while True:
    if length != len(recordings):
      new_data = recordings[-1]
      if new_data == "start":
        start_time = time.time()
      if new_data == "join":
        user += 1
      if new_data == "leave":
        user -= 1
      if new_data == "message":
        message += 1
      file = open("index.html","w")
      file.write(template[0] + user + template[1] + str(round((time.time() - start) * 1000 * 60 * 60)) + template[2] + message + template[3])
threading.Thread(target=loop).start()
