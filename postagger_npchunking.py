from nltk import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
import re
import string

with open("wihler2017.txt",'r',encoding="utf-8") as f:
    text = f.read()
        
text.replace("\\n",'')
text.replace("\n-",' ')
text.replace("-",'')

stop_words = set(stopwords.words('english'))

for x in stop_words:
    text.replace(x, '')

sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)
semne=[',','.','?','!','(',')','[',']','@','*','=','-']

litere=list(string.ascii_lowercase)+list(string.ascii_uppercase)

adjective_tags = ["JJ", "JJR", "JJS"]
noun_tags=["NN","NNP","NNS"]
adverb_tags=["RB","RBR","RBS"]
verb_tags=["VB","VBD","VBG","VBN","VBP","VBZ"]

adverbe=[]
adjective=[]
substantive=[]
verbe=[]

for s in sentences:
    words=s.split(' ')
    words=[x for x in words if x not in stop_words]
    ready=""
    for w in words:
        if w not in semne:
            ready+=w+' '
    text=word_tokenize(ready)
    tags=pos_tag(text)
    for tag in tags:
        if tag[0] in semne:
            tags.remove(tag)
        if tag[0] in litere:
            tags.remove(tag)
    for tag in tags:
        if bool(re.match(r"[a-zA-Z]+([-–][a-zA-Z]+)*", tag[0])) and not bool(re.match(r"\w+[-–]|[-–]\w+", tag[0])) and not litere.__contains__(tag[0]):
            if(tag[1] in adjective_tags):
                adjective.append(tag[0].lower())
            if(tag[1] in adverb_tags):
                adverbe.append(tag[0].lower())
            if(tag[1] in noun_tags):
                substantive.append(tag[0].lower())
            if(tag[1] in verb_tags):
                verbe.append(tag[0].lower())
    #print(tags)

print("ADVERBE")
print(adverbe)
print("ADJECTIVE")
print(adjective)
print("SUBSTANTIVE")
print(substantive)
print("VERBE")
print(verbe)
