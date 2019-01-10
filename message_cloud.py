"""Make a wordcloud out the messages

pip install wordcloud

"""

import re
from data import data
from wordcloud import WordCloud

RE_PUNCTUATION = re.compile(r'[)(\.!]')

# Get a uniform text
text = ' '.join(RE_PUNCTUATION.sub(' ', message.lower()) for _, __, message in data)
print(text)
# Generate a word cloud image
wcd = WordCloud().generate(text)
wcd.to_file('out/message-cloud.png')
