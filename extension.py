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
  global recordings
  recordings.append(message)
def extension():
  global recordings
  length = 0
  while True:
    if length != len(recordings):
      new_data = recordings[-1]
      # WAITING FOR CHANGES IN OTHER REPOS
