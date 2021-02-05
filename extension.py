# UNDER DEVELOPMENT

# Take this as a example if you want to write your own extension.
# The extension wiki will be released soon.

import threading
template_file = open("template.html")
global template
global recordings
template = template_file.read()
recordings = []
def record(message):
  recordings.append(message)
def extension():
  length = 0
  while True:
    if length != len(recordings):
      new_data = recordings[-1]
      # UNDER DEVELOPMENT HERE
