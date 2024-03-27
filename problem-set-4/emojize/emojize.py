#install emoji package: pip install emoji

import emoji

text = input()
text_emoji = emoji.emojize(text, language="alias")
print(text_emoji)
