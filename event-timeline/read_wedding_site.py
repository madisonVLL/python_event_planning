import sys
from typing import *
from bs4 import BeautifulSoup
time_key_words: list[str] = ["am", "AM", "pm", "PM", "minute", 
                             "minutes", "hour"]

if len(sys.argv) > 1:
    current_file = open(sys.argv[1], "r")
else:
    raise ValueError("must import a file type to traverse them")

#reading the correct file
website_data: BeautifulSoup = BeautifulSoup(current_file.read(), 'xml')
time_set: set[str] = set()

for paragraph in website_data.find_all(['h', 'p', 'div']):
    para_text: list[str] = paragraph.text.split()
    for i, curr_string in enumerate(para_text): 
        if i > 1 and i + 1 <= len(para_text) - 1:
            if curr_string == ":":
                if para_text[i - 1].isdigit() and para_text[i + 1].isdigit():
                    print(curr_string)
                    time_set.add(paragraph.text)
        if curr_string in time_key_words:
            time_set.add(paragraph.text)

print(time_set)        