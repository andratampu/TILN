import re

test_str=""
with open("wihler2017.txt",'r',encoding="utf-8") as f:
    for line in f.readline():
        test_str+=line+'\n'

regex = r'[\s\w]+([0-9]+(\s+)(\((\d+)\)(\s+)(\d+)[\–\-]+(\d+)))(([\w\s:\/.]+)(\s+))([A-Za-z0-9\- ,:]+)(((\n)[A-Za-z0-9\- ,:]+|[A-Za-z0-9\- ,:]+)*)(\s+)(([A-Z][a-z]+(\s+)((([A-Z][a-z]+(\s*))+)|([A-Z][a-z]+(\s+)[A-Z]+\.(\s+)[A-Z][a-z]+(\s+)))((.|\s)+))+)'

matches = re.finditer(regex, test_str, re.MULTILINE | re.DOTALL)

for matchNum, match in enumerate(matches, start=1): 
    firstlines=match.group()

regex=r'[\s\w]+([0-9]+(\s+)(\((\d+)\)(\s+)(\d+)[\–\-]+(\d+)))'

matches = re.finditer(regex, firstlines, re.MULTILINE | re.DOTALL)

for matchNum, match in enumerate(matches, start=1): 
    primalinie_efectiv=match.group()

primalinie_efectiv=primalinie_efectiv.lstrip()
primalinie_efectiv=primalinie_efectiv.rstrip()

regex = r'([A-Z][a-z]+(\s+)(([A-Z][a-z]+(\ +))|(([A-Z]\.)(\ +)([A-Z][a-z]+[\ ,]+))))(.,)'

matches = re.finditer(regex, firstlines, re.MULTILINE | re.DOTALL)

names=[]
for matchNum, match in enumerate(matches, start=1):
    names.append(match.group())

regex=r'\([0-9]+\)'

matches=re.finditer(regex,primalinie_efectiv,re.MULTILINE | re.DOTALL)

for matchNum, match in enumerate(matches, start=1):
    year=match.group()
    break

firstlines=firstlines.replace(primalinie_efectiv,'')

for i in names:
    firstlines=firstlines.replace(i,'')

jurnal=primalinie_efectiv.replace(' '+year,',')

regex = r'(\d+)[,\ ]+(\d+)(\-|\–)(\d+)'

matches=re.finditer(regex,jurnal,re.MULTILINE | re.DOTALL)

for matchNum, match in enumerate(matches, start=1):
    capitol=match.group()
    break

regex=r'\n[A-Z][a-z]*,[, a-zﬁ:\n]*[A-Z]'

matches=re.finditer(regex,firstlines,re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    titlu=match.group()
    break

jurnal=jurnal.replace(capitol,'')
jurnal=jurnal.rstrip()

low = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for i in names:
    i.replace("",'')
    i=i[::-1]
    for c in i:
        if c not in low:
            i.replace(c,'')

output=""
for j,n in enumerate(names):
    if j>0 and j==len(names)-1:
        output+=" & "
    x=n.split(' ')
    x.reverse()
    for i,item in enumerate(x):
        if i:
            output+=item[0]+'.'
        else:
            output+=item+", "
        if j<len(names)-2 and i!=0:
            output+=", "
        
# output+=" "+year+". "+title+". "+jurnal+", "+capitol+"."

output+=" "+year+"."+jurnal+", "+capitol+"."

print(output)