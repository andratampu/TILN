import re

regex = r'(\s+)([a-zA-Z0-9 ]+[0-9]+\ +\([0-9]+\)\ +[0-9]+-[0-9]+\n+)(\s+)([A-Za-z0-9 ,;]+)(\s+)(((([A-z][a-z]+(\ +)([A-Z][a-z]+(\ *))+)|([A-Z][a-z]+\ (((([A-Z]\.\ )+)([A-Z][a-z]+))|([A-Z][a-z]+)))))[, \s]+)+'

test_str = ("               Hello my name is Chandler Bing 104 (2017) 78-95\n\n	Title here, well, this should be a title, bla bla bla\n\nPieter V. D. Woude, Josh A. Milne, Gandalf Gray Paloma Siesta\n\n")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    firstlines=match.group()

regex = r'[A-Z][a-z]+\ (((([A-Z]\.\ )+)([A-Z][a-z]+))|([A-Z][a-z]+))'

matches = re.finditer(regex, firstlines, re.MULTILINE)

names=[]
for matchNum, match in enumerate(matches, start=1):
    names.append(match.group())

regex = r'[a-zA-Z0-9 ]+[0-9]+\ +\([0-9]+\)\ +[0-9]+-[0-9]+\n+'

matches = re.finditer(regex, test_str, re.MULTILINE)

firstline=""
for matchNum, match in enumerate(matches, start=1):
    firstline=match.group()
    break

regex=r'\([0-9]+\)'

matches=re.finditer(regex,firstline,re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    year=match.group()
    break

title=firstlines.replace(firstline,'')

for i in names:
    title=title.replace(i,'')

regex=r'[A-Za-z0-9\- ,:]+'

matches=re.finditer(regex,title,re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    title=match.group()
    break

title=title.rstrip()
title=title.lstrip()

firstline=firstline.replace(' '+year,',')

firstline=firstline.rstrip()
firstline=firstline.lstrip()

regex=r'(\d+)[,: ]+(\d+)\-(\d+)'

matches=re.finditer(regex,firstline,re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    capitol=match.group()
    break

jurnal=firstline.replace(capitol,'')
jurnal=jurnal.rstrip()

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
        
output+=" "+year+". "+title+". "+jurnal+", "+capitol+"."