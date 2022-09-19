import re
import pyttsx3

'''
takes .txt of readings and turns it into an .mp3
make file called chapter.txt in cwd and put reading into it
'''
page_reg = re.compile(r'[^\n]*(Building a Chinese Nation-State)[^\n]*') #regex to remove page numbers and headings, reprogram as neeeded
word_break_reg= re.compile('[-]+\n+') #regex to deal with line breaks mid word, probably dont touch this
break_reg= re.compile('\n+') #regex to deal with all other line breaks, probably dont touch this

with open('chapter.txt', 'r', encoding="utf8") as chapter:
    print('editing and saving chapter...')
    s = chapter.read()
    s=page_reg.sub('',s)
    s=word_break_reg.sub('', s)
    s=break_reg.sub(' ', s)
    with open('chapter edit.txt', 'w') as out:
        out.write(s)
    print('done\n')

    print('initializing tts engine...')
    engine = pyttsx3.init()
    engine.setProperty('rate', 175)
    print('done\n')

    file = 'chapter edit.mp3'
    print('tts in progress...')
    engine.save_to_file(s, file)
    engine.runAndWait()
    print('done')