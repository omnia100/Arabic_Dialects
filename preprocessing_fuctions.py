
import codecs
# import pandas as pd
import re
import string

# raw_data = pd.read_json(codecs.open('df.json', 'r', 'utf-8'))

"""# Clean

### mention
"""

usr = r'(@[A-Za-z0-9]{5,15})\b'
usr_re = re.compile(usr)

def replace_usr(x):
  return usr_re.sub('',x)

"""### url"""

url = r'(https?:\/\/?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b[-a-zA-Z0-9()@:%_\+.~#?&//=]*)'
url_re = re.compile(url)

def replace_url(x):
  return url_re.sub('',x)

"""### hashtag"""

htag = r'(#\w+)'
htag_re = re.compile(htag)

def replace_htag(x):
  return htag_re.sub('',x)

"""### emojis"""

emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)

def remove_emojis(text):
  return emoj.sub(' ', text)

"""### numbers and english words"""

num_eng =r'[A-Za-z0-9٠-٩]+'
ne_re = re.compile(num_eng)

def remove_english_and_numbers(text):
    return re.sub(num_eng, ' ', text)


"""### punctuation"""

arabic_punctuations = r'[،\."\(\):\-?!؛…؟]'
ara_re = re.compile(arabic_punctuations)

def remove_punctuations(text):
    return re.sub(arabic_punctuations,' ', text)


"""### repeated character"""

def remove_repeating_char(text):
    return re.sub(r'(.)\1+', r'\1', text)


"""### marks"""

marks = '''`÷×؛<«»>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“—–ـ'''
english_punctuations = string.punctuation
allMarks = marks + english_punctuations

def remove_marks(text):
    translator = str.maketrans('', '', allMarks)
    return text.translate(translator)


"""# Normalize

### diacritic
"""

arabic_diacritics = re.compile("""
                             ّ 
                             َ 
                             ً 
                             ُ 
                             ٌ 
                             ِ 
                             ٍ 
                             ْ 
                             ـ
                         """, re.VERBOSE)


def remove_diacritics(text):
    # return [arabic_diacritics.sub('',word) for word in word_list]
    return arabic_diacritics.sub('',text)


"""### special characters"""

def normalize_arabic(text):
    text = re.sub("[إأآا]", "ا", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("ؤ", "ء", text)
    text = re.sub("ئ", "ء", text)
    text = re.sub("ة", "ه", text)
    text = re.sub("گ", "ك", text)
    return text




def preprocess(text):
    text = replace_usr(text)
    text = replace_htag(text)
    text = replace_url(text)
    text = remove_emojis(text)
    text = remove_english_and_numbers(text)
    text = remove_punctuations(text)
    text = remove_repeating_char(text)
    text = remove_marks(text)
    text = remove_diacritics(text)
    text = normalize_arabic(text)
    return text