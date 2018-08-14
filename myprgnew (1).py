import string
import nltk
import numpy
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import RegexpTokenizer
import enchant
from enchant.checker import SpellChecker


def filecorrect(token1):
    sentence='';
    #print("i am in filecorrect")
    #print(token1)
    length=len(token1)
    for x in range(0,length):
        token=word_tokenize(token1[x])
        d=enchant.Dict("en_US")
        #token=word_tokenize(sent)
        #print(token)
        length=len(token)
        for a in range(0,length):
            chkr=SpellChecker("en_US")
            #print(a)
            temp=token[a]
            #print(temp)
            x=d.check(temp)
            #chkr.set_text(temp)
            #print(x)
            if x == False:
               # print("it is fales")
                #chkr=SpellChecker("en_US")
                #chkr.set_text(temp)
                #for err in chkr:
                    #b=err.word
                #d=enchant.Dict("en_US")
                #c=d.suggest(a)
                print("there is a mismatch of spelling"+" "+temp+" "+" in this sentence")
                print("do you want to replace type s")
                print("do you want to ignore type i")
                print("do you want to add the word to the dictionary then type a")
                #des='s'
                dec=input("s/i/a")
                if dec=="s":
                    c=d.suggest(temp)
                    print("suggestion",c)
                    token[a]=input("enter replace")
                    print(token)
                elif dec=="i":
                    print("ignored")
                elif dec=='a':
                    d.add(temp)
                    print("added to dictionary")
            sentence=sentence + token[a]+' '
            #print(sentence)
            #print('k')
    ans=sent_tokenize(sentence)
    print(ans)
    length2=len(ans)
    #print(length2)
    print("do you want to save the file")
    e=input("if yes, press k or press n")
    if e == 'k':
        filesavecorrectdivide(ans)
    elif e =='n':
        filecorrectdivide(ans)


def filesavecorrectdivide(ans):
    #print("i am in")
    from nltk.tokenize import sent_tokenize, word_tokenize
    from nltk.tokenize import RegexpTokenizer
    from enchant.checker import SpellChecker
    print("enter the path")
    p=input("path:")
    
    #print("do you want to save the file")
    #e=input("if yes, press k or press n")
    #if e == 'k':
        #print("enter the path where you want to save it")
        #p=input("path")
    #elif e =='n':
        #print("ok")
    
    #ch='yes'
    #no=1
    #while ch=="yes":
    cond_key =["if","when","while","unless","untill","only","whenever","as long as","because","inorder to","after","before","as soon as","if only","only if","since","incase",]
    action_key =["shall","then","do","on","will","please","would","should","could","might",]
    length1=len(ans)
    #print(length1)
    tokenizer = RegexpTokenizer(r'\W+')
    pun = ["[","]","!","{","}","#","@","^","%","-","+","?",".","'","(",")",","]
    #for zz in range(0,length):
        #for z in range(0,len(pun)):
            #if(tokens[zz]==pun[z]):
              # tokens[zz]=''

    

    for h in range(0,length1):
        ans1=0
        ans2=0
        tokens1 = word_tokenize(ans[h])
        length2=len(tokens1)
        #print(length2)
        for a1 in range(0,length2):
            for a2 in range(0,len(pun)):
                if(tokens1[a1]==pun[a2]):
                      tokens1[a1]=''
        length3=len(tokens1)
        #print(length3)
        for a3 in range(0,length3):
            for a4 in range(0,len(cond_key)):
                if(tokens1[a3]==cond_key[a4] and ans1==0):
                    #print(tokens1[a3])
                    ans1=1
        for a5 in range(0,length3):
            for a6 in range(0,len(action_key)):
                if(tokens1[a5]==action_key[a6] and ans2==0):
                    #print(tokens1[a5])
                    ans2=1
        #length2 = len(tokens1)
       # print(length2)
        #print(tokens1)
        #for a in range(0,length2):
         #   for aa in range(0,len(cond_key)):
          #      if(tokens1[a]==cond_key[aa]):
           #        ans='true'
            #    else:
             #       ans='false'
        #for b in range(0,length2):
         #   for bb in range(0,len(action_key)):
          #      if(tokens1[b]==action_key[bb]):
           #                 ans1='true'
            #    else:
             #               ans1='false'
        #print(ans1)
        #print(ans2)
        if(ans1==1 and ans2==1):
             #print("i am in")
                 #ch='yes'
                 #no=1
                 #while ch=="yes":
             tokenizer = RegexpTokenizer(r'\W+')
             pun = ["[","]","!","{","}","#","@","^","%","-","+","?",".","'","(",")",","]
    
                 #example_sent= input("enter the sentence:")
                 #chr = SpellChecker("en_US")  
                 #chr.set_text(example_sent)
                 #for err in chr:
                 #print("error",err.word)
             #print(ans[h])
             #print(tokens1)
             tokens =word_tokenize(ans[h])
                 #tokens=token
             codn = '';
             actions = '';
             act = '';
             acti = '';
             condition = '';
             s1=0
             t1=0
             s=0
             t=0
             cond_flag=0
             action_flag=0
             length = len(tokens)
             #print(length)
             #print(tokens)
             cond_key =["if","when","while","unless","untill","only","whenever","as long as","because","inorder to","after","before","as soon as","if only","only if","since","incase",]
             action_key =["shall","then","do","on","will","please","would","should","could","might",]
             for zz in range(0,length):
                 for z in range(0,len(pun)):
                     if(tokens[zz]==pun[z]):
                        tokens[zz]=''
             for x in range(0, length):
                 for xx in range(0,len(cond_key)):
                      if(tokens[x] == cond_key[xx] and s1==0):
                           s1 = x
                           #print("con")
                           #print(s1)
                           cond_flag=1
                         #for x in range(0, length):
             #print(x)
             if(cond_flag==1):
                  for y in range(0,length):
                        for yy in range(0,len(action_key)):
                             if(tokens[y]==action_key[yy] and t1==0):
                                       t1 = y
                                       #print(t1)

             if(t1<s1):
                  t1=length     
                  #print(t1)
             for st in range(s1+1,t1):
                    #print(st)
                    condition += tokens[st]
                    condition += '\t'
 
             ctok=word_tokenize(condition)

             t1=1
             for cc in range (0,len(ctok)):
                    if(ctok[cc]=="is" or ctok[cc]=="=" or ctok[cc]=="equals" or ctok[cc]=="set"):
                          ctok[cc]="="
                    if(ctok[cc]=="larger" or ctok[cc]==">" or ctok[cc]=="greater" or ctok[cc]=="above" or ctok[cc]=="greater" and ctok[cc+1]=="than"):
                           t1 = 0
                           t2=cc-1
                           ctok[cc]=">"
                    if(ctok[cc]=="smaller" or ctok[cc]=="<" or ctok[cc]=="lesser" or ctok[cc]=="below" or ctok[cc]=="lesser" and ctok[cc+1]=="than"):
                           ctok[cc]="<"
                           t1=0
                           t2=cc-1
                    if(t1==0):
                        if(ctok[t2]=="is"):
                         ctok[t2]=''

             for x1 in range(0, length):
                  for xx in range(0,len(action_key)):
                     if(tokens[x1] == action_key[xx] and s==0):
                             s = x1
                             #print("act")
                             #print(s)
                             action_flag=1
             if(action_flag==1):
                   for x1 in range(0, length):
                       # for y in range(x+1,length):
                       for yy in range(0,len(cond_key)):
                           if(tokens[x1]==cond_key[yy] and t==0):
                            t=x1
             if(t<s):
                  t=length
             for s1 in range(s+1,t):
                  acti += tokens[s1]
                  acti += '\t'
                  act=word_tokenize(acti) 
                     #c.execute("insert into output (req_no, condition, action) values (?, ?, ?)",
                      #       (12, codn, act))
                      #c.execute('''select condition from output''')
                      #rows=c.fetchall()
                      #print(rows[0])
                      #for row in rows:
                      #   print(row)
             for aa in range(0,len(ctok)):
                    codn+=ctok[aa]
                    codn+="\t"
             for aa in range(0,len(act)):
                    actions+=act[aa]
                    actions+="\t"
                  #tab=(['condn','action'],[codn,actions])
                  #tt=tabulate(tab)
             print("condition")
             print(codn)
    
             print("action")
             print(actions)
             m=("condition:"+codn+"action:"+actions)
             with open(p,mode='a')as f:
                 f.write("*")
                 f.write(m)
                 f.write("\n")
                 f.close()
             
        else:
            sent=tokens1
            #transulation=str.maketrans("","",string.punctuation)
            #new=sent.translate(transulation)
            #print(new)
            #lower_case=str.lower(new)
            #print(lower_case)
            stop_words= ('their','be','are','ourselves','these','were','but','because','few','his','and','before','them','me','was','been','so','should','theirs','did','are','yourself','why','being','a','same','our','he','has','have','she','above','my','can','that','each','under','is','won','its','we','isn','just','here','haven','than','again','some','or','her','between','up','of','out','with','had','more','i','there','hadn','from','the','mightn','during','itself','most','herself','ll','very','yours','himself','which','on','when','down','at','mustn','you','does','this','it','who','will','themselves','those','they','wasn','how','hers','myself','would','as','has','whom','own','could','should','didn','once','in','what','against','where','any','other','am','if','for','ours','him','through','ve','all','your','then','too','yourselves','having','weren','an','needn')
            #print(stop_words)
            #words= word_tokenize(sent)
            filtered_sent=[]
            for w in sent:
                if w not in stop_words:
                    filtered_sent.append(w)
            print("statement")        
            print(filtered_sent)
            with open(p,mode='a')as f:
                 f.write("*")
                 f.write("condition and action")
                 f.write(str(filtered_sent))
                 f.write("\n")
                 f.close()


    
def filecorrectdivide(ans):
    #print("i am in")
    from nltk.tokenize import sent_tokenize, word_tokenize
    from nltk.tokenize import RegexpTokenizer
    from enchant.checker import SpellChecker
    #print("do you want to save the file")
    #e=input("if yes, press k or press n")
    #if e == 'k':
        #print("enter the path where you want to save it")
        #p=input("path")
    #elif e =='n':
        #print("ok")
    
    #ch='yes'
    #no=1
    #while ch=="yes":
    cond_key =["if","when","while","unless","untill","only","whenever","as long as","because","inorder to","after","before","as soon as","if only","only if","since","incase",]
    action_key =["shall","then","do","on","will","please","would","should","could","might",]
    length1=len(ans)
    #print(length1)
    tokenizer = RegexpTokenizer(r'\W+')
    pun = ["[","]","!","{","}","#","@","^","%","-","+","?",".","'","(",")",","]
    #for zz in range(0,length):
        #for z in range(0,len(pun)):
            #if(tokens[zz]==pun[z]):
              # tokens[zz]=''

    

    for h in range(0,length1):
        ans1=0
        ans2=0
        tokens1 = word_tokenize(ans[h])
        length2=len(tokens1)
        #print(length2)
        for a1 in range(0,length2):
            for a2 in range(0,len(pun)):
                if(tokens1[a1]==pun[a2]):
                      tokens1[a1]=''
        length3=len(tokens1)
        #print(length3)
        for a3 in range(0,length3):
            for a4 in range(0,len(cond_key)):
                if(tokens1[a3]==cond_key[a4] and ans1==0):
                    #print(tokens1[a3])
                    ans1=1
        for a5 in range(0,length3):
            for a6 in range(0,len(action_key)):
                if(tokens1[a5]==action_key[a6] and ans2==0):
                    #print(tokens1[a5])
                    ans2=1
        #length2 = len(tokens1)
       # print(length2)
        #print(tokens1)
        #for a in range(0,length2):
         #   for aa in range(0,len(cond_key)):
          #      if(tokens1[a]==cond_key[aa]):
           #        ans='true'
            #    else:
             #       ans='false'
        #for b in range(0,length2):
         #   for bb in range(0,len(action_key)):
          #      if(tokens1[b]==action_key[bb]):
           #                 ans1='true'
            #    else:
             #               ans1='false'
        #print(ans1)
        #print(ans2)
        if(ans1==1 and ans2==1):
             #print("i am in")
                 #ch='yes'
                 #no=1
                 #while ch=="yes":
             tokenizer = RegexpTokenizer(r'\W+')
             pun = ["[","]","!","{","}","#","@","^","%","-","+","?",".","'","(",")",","]
    
                 #example_sent= input("enter the sentence:")
                 #chr = SpellChecker("en_US")  
                 #chr.set_text(example_sent)
                 #for err in chr:
                 #print("error",err.word)
             #print(ans[h])
             #print(tokens1)
             tokens =word_tokenize(ans[h])
                 #tokens=token
             codn = '';
             actions = '';
             act = '';
             acti = '';
             condition = '';
             s1=0
             t1=0
             s=0
             t=0
             cond_flag=0
             action_flag=0
             length = len(tokens)
             #print(length)
             #print(tokens)
             cond_key =["if","when","while","unless","untill","only","whenever","as long as","because","inorder to","after","before","as soon as","if only","only if","since","incase",]
             action_key =["shall","then","do","on","will","please","would","should","could","might",]
             for zz in range(0,length):
                 for z in range(0,len(pun)):
                     if(tokens[zz]==pun[z]):
                        tokens[zz]=''
             for x in range(0, length):
                 for xx in range(0,len(cond_key)):
                      if(tokens[x] == cond_key[xx] and s1==0):
                           s1 = x
                           #print("con")
                           #print(s1)
                           cond_flag=1
                         #for x in range(0, length):
             #print(x)
             if(cond_flag==1):
                  for y in range(0,length):
                        for yy in range(0,len(action_key)):
                             if(tokens[y]==action_key[yy] and t1==0):
                                       t1 = y
                                       #print(t1)

             if(t1<s1):
                  t1=length     
                  #print(t1)
             for st in range(s1+1,t1):
                    #print(st)
                    condition += tokens[st]
                    condition += '\t'
 
             ctok=word_tokenize(condition)

             t1=1
             for cc in range (0,len(ctok)):
                    if(ctok[cc]=="is" or ctok[cc]=="=" or ctok[cc]=="equals" or ctok[cc]=="set"):
                          ctok[cc]="="
                    if(ctok[cc]=="larger" or ctok[cc]==">" or ctok[cc]=="greater" or ctok[cc]=="above" or ctok[cc]=="greater" and ctok[cc+1]=="than"):
                           t1 = 0
                           t2=cc-1
                           ctok[cc]=">"
                    if(ctok[cc]=="smaller" or ctok[cc]=="<" or ctok[cc]=="lesser" or ctok[cc]=="below" or ctok[cc]=="lesser" and ctok[cc+1]=="than"):
                           ctok[cc]="<"
                           t1=0
                           t2=cc-1
                    if(t1==0):
                        if(ctok[t2]=="is"):
                         ctok[t2]=''

             for x1 in range(0, length):
                  for xx in range(0,len(action_key)):
                     if(tokens[x1] == action_key[xx] and s==0):
                             s = x1
                             #print("act")
                             #print(s)
                             action_flag=1
             if(action_flag==1):
                   for x1 in range(0, length):
                       # for y in range(x+1,length):
                       for yy in range(0,len(cond_key)):
                           if(tokens[x1]==cond_key[yy] and t==0):
                            t=x1
             if(t<s):
                  t=length
             for s1 in range(s+1,t):
                  acti += tokens[s1]
                  acti += '\t'
                  act=word_tokenize(acti) 
                     #c.execute("insert into output (req_no, condition, action) values (?, ?, ?)",
                      #       (12, codn, act))
                      #c.execute('''select condition from output''')
                      #rows=c.fetchall()
                      #print(rows[0])
                      #for row in rows:
                      #   print(row)
             for aa in range(0,len(ctok)):
                    codn+=ctok[aa]
                    codn+="\t"
             for aa in range(0,len(act)):
                    actions+=act[aa]
                    actions+="\t"
                  #tab=(['condn','action'],[codn,actions])
                  #tt=tabulate(tab)
             print("condition")
             print(codn)
    
             print("action")
             print(actions)
             
        else:
            sent=tokens1
            #transulation=str.maketrans("","",string.punctuation)
            #new=sent.translate(transulation)
            #print(new)
            #lower_case=str.lower(new)
            #print(lower_case)
            stop_words= ('their','be','are','ourselves','these','were','but','because','few','his','and','before','them','me','was','been','so','should','theirs','did','are','yourself','why','being','a','same','our','he','has','have','she','above','my','can','that','each','under','is','won','its','we','isn','just','here','haven','than','again','some','or','her','between','up','of','out','with','had','more','i','there','hadn','from','the','mightn','during','itself','most','herself','ll','very','yours','himself','which','on','when','down','at','mustn','you','does','this','it','who','will','themselves','those','they','wasn','how','hers','myself','would','as','has','whom','own','could','should','didn','once','in','what','against','where','any','other','am','if','for','ours','him','through','ve','all','your','then','too','yourselves','having','weren','an','needn')
            #print(stop_words)
            #words= word_tokenize(sent)
            filtered_sent=[]
            for w in sent:
                if w not in stop_words:
                    filtered_sent.append(w)
            print("statement")        
            print(filtered_sent)



def filesavedivide(token1):
    #print("i am in")
    from nltk.tokenize import sent_tokenize, word_tokenize
    from nltk.tokenize import RegexpTokenizer
    from enchant.checker import SpellChecker
    print("enter the path")
    p=input("path")
    #ch='yes'
    #no=1
    #while ch=="yes":
    cond_key =["if","when","while","unless","untill","only","whenever","as long as","because","inorder to","after","before","as soon as","if only","only if","since","incase",]
    action_key =["shall","then","do","on","will","please","would","should","could","might",]
    length1=len(token1)
    #print(length1)
    tokenizer = RegexpTokenizer(r'\W+')
    pun = ["[","]","!","{","}","#","@","^","%","-","+","?",".","'","(",")",","]
    #for zz in range(0,length):
        #for z in range(0,len(pun)):
            #if(tokens[zz]==pun[z]):
              # tokens[zz]=''

    

    for h in range(0,length1):
        ans1=0
        ans2=0
        tokens1 = word_tokenize(token1[h])
        length2=len(tokens1)
        #print(length2)
        for a1 in range(0,length2):
            for a2 in range(0,len(pun)):
                if(tokens1[a1]==pun[a2]):
                      tokens1[a1]=''
        length3=len(tokens1)
        #print(length3)
        for a3 in range(0,length3):
            for a4 in range(0,len(cond_key)):
                if(tokens1[a3]==cond_key[a4] and ans1==0):
                    #print(tokens1[a3])
                    ans1=1
        for a5 in range(0,length3):
            for a6 in range(0,len(action_key)):
                if(tokens1[a5]==action_key[a6] and ans2==0):
                    #print(tokens1[a5])
                    ans2=1
        #length2 = len(tokens1)
       # print(length2)
        #print(tokens1)
        #for a in range(0,length2):
         #   for aa in range(0,len(cond_key)):
          #      if(tokens1[a]==cond_key[aa]):
           #        ans='true'
            #    else:
             #       ans='false'
        #for b in range(0,length2):
         #   for bb in range(0,len(action_key)):
          #      if(tokens1[b]==action_key[bb]):
           #                 ans1='true'
            #    else:
             #               ans1='false'
        #print(ans1)
        #print(ans2)
        if(ans1==1 and ans2==1):
             #print("i am in")
                 #ch='yes'
                 #no=1
                 #while ch=="yes":
             tokenizer = RegexpTokenizer(r'\W+')
             pun = ["[","]","!","{","}","#","@","^","%","-","+","?",".","'","(",")",","]
    
                 #example_sent= input("enter the sentence:")
                 #chr = SpellChecker("en_US")  
                 #chr.set_text(example_sent)
                 #for err in chr:
                 #print("error",err.word)
             #print(token1[h])
             #print(tokens1)
             tokens =word_tokenize(token1[h])
                 #tokens=token
             codn = '';
             actions = '';
             act = '';
             acti = '';
             condition = '';
             s1=0
             t1=0
             s=0
             t=0
             cond_flag=0
             action_flag=0
             length = len(tokens)
             #print(length)
             #print(tokens)
             cond_key =["if","when","while","unless","untill","only","whenever","as long as","because","inorder to","after","before","as soon as","if only","only if","since","incase",]
             action_key =["shall","then","do","on","will","please","would","should","could","might",]
             for zz in range(0,length):
                 for z in range(0,len(pun)):
                     if(tokens[zz]==pun[z]):
                        tokens[zz]=''
             for x in range(0, length):
                 for xx in range(0,len(cond_key)):
                      if(tokens[x] == cond_key[xx] and s1==0):
                           s1 = x
                           #print("con")
                           #print(s1)
                           cond_flag=1
                         #for x in range(0, length):
             #print(x)
             if(cond_flag==1):
                  for y in range(0,length):
                        for yy in range(0,len(action_key)):
                             if(tokens[y]==action_key[yy] and t1==0):
                                       t1 = y
                                       #print(t1)

             if(t1<s1):
                  t1=length     
                  #print(t1)
             for st in range(s1+1,t1):
                    #print(st)
                    condition += tokens[st]
                    condition += '\t'
 
             ctok=word_tokenize(condition)

             t1=1
             for cc in range (0,len(ctok)):
                    if(ctok[cc]=="is" or ctok[cc]=="=" or ctok[cc]=="equals" or ctok[cc]=="set"):
                          ctok[cc]="="
                    if(ctok[cc]=="larger" or ctok[cc]==">" or ctok[cc]=="greater" or ctok[cc]=="above" or ctok[cc]=="greater" and ctok[cc+1]=="than"):
                           t1 = 0
                           t2=cc-1
                           ctok[cc]=">"
                    if(ctok[cc]=="smaller" or ctok[cc]=="<" or ctok[cc]=="lesser" or ctok[cc]=="below" or ctok[cc]=="lesser" and ctok[cc+1]=="than"):
                           ctok[cc]="<"
                           t1=0
                           t2=cc-1
                    if(t1==0):
                        if(ctok[t2]=="is"):
                         ctok[t2]=''

             for x1 in range(0, length):
                  for xx in range(0,len(action_key)):
                     if(tokens[x1] == action_key[xx] and s==0):
                             s = x1
                             #print("act")
                             #print(s)
                             action_flag=1
             if(action_flag==1):
                   for x1 in range(0, length):
                       # for y in range(x+1,length):
                       for yy in range(0,len(cond_key)):
                           if(tokens[x1]==cond_key[yy] and t==0):
                            t=x1
             if(t<s):
                  t=length
             for s1 in range(s+1,t):
                  acti += tokens[s1]
                  acti += '\t'
                  act=word_tokenize(acti) 
                     #c.execute("insert into output (req_no, condition, action) values (?, ?, ?)",
                      #       (12, codn, act))
                      #c.execute('''select condition from output''')
                      #rows=c.fetchall()
                      #print(rows[0])
                      #for row in rows:
                      #   print(row)
             for aa in range(0,len(ctok)):
                    codn+=ctok[aa]
                    codn+="\t"
             for aa in range(0,len(act)):
                    actions+=act[aa]
                    actions+="\t"
                  #tab=(['condn','action'],[codn,actions])
                  #tt=tabulate(tab)
             print("condition")
             print(codn)
    
             print("action")
             print(actions)
             m=("condition:"+codn+"action:"+actions)
             with open(p,mode='a')as f:
                 f.write("*")
                 f.write(m)
                 f.write("\n")
                 f.close()
             
        else:
            sent=tokens1
            #transulation=str.maketrans("","",string.punctuation)
            #new=sent.translate(transulation)
            #print(new)
            #lower_case=str.lower(new)
            #print(lower_case)
            stop_words= ('their','be','are','ourselves','these','were','but','because','few','his','and','before','them','me','was','been','so','should','theirs','did','are','yourself','why','being','a','same','our','he','has','have','she','above','my','can','that','each','under','is','won','its','we','isn','just','here','haven','than','again','some','or','her','between','up','of','out','with','had','more','i','there','hadn','from','the','mightn','during','itself','most','herself','ll','very','yours','himself','which','on','when','down','at','mustn','you','does','this','it','who','will','themselves','those','they','wasn','how','hers','myself','would','as','has','whom','own','could','should','didn','once','in','what','against','where','any','other','am','if','for','ours','him','through','ve','all','your','then','too','yourselves','having','weren','an','needn')
            #print(stop_words)
            #words= word_tokenize(sent)
            filtered_sent=[]
            for w in sent:
                if w not in stop_words:
                    filtered_sent.append(w)
            print("statement")        
            print(filtered_sent)
            with open(p,mode='a')as f:
                 f.write("*")
                 f.write(str(filtered_sent))
                 f.write("\n")
                 f.close()

            

            
def filedivide(token1):
    #print("i am in")
    from nltk.tokenize import sent_tokenize, word_tokenize
    from nltk.tokenize import RegexpTokenizer
    from enchant.checker import SpellChecker
    #ch='yes'
    #no=1
    #while ch=="yes":
    cond_key =["if","when","while","unless","untill","only","whenever","as long as","because","inorder to","after","before","as soon as","if only","only if","since","incase",]
    action_key =["shall","then","do","on","will","please","would","should","could","might",]
    length1=len(token1)
    #print(length1)
    tokenizer = RegexpTokenizer(r'\W+')
    pun = ["[","]","!","{","}","#","@","^","%","-","+","?",".","'","(",")",","]
    #for zz in range(0,length):
        #for z in range(0,len(pun)):
            #if(tokens[zz]==pun[z]):
              # tokens[zz]=''

    

    for h in range(0,length1):
        ans1=0
        ans2=0
        tokens1 = word_tokenize(token1[h])
        length2=len(tokens1)
        #print(length2)
        for a1 in range(0,length2):
            for a2 in range(0,len(pun)):
                if(tokens1[a1]==pun[a2]):
                      tokens1[a1]=''
        length3=len(tokens1)
        #print(length3)
        for a3 in range(0,length3):
            for a4 in range(0,len(cond_key)):
                if(tokens1[a3]==cond_key[a4] and ans1==0):
                    #print(tokens1[a3])
                    ans1=1
        for a5 in range(0,length3):
            for a6 in range(0,len(action_key)):
                if(tokens1[a5]==action_key[a6] and ans2==0):
                    #print(tokens1[a5])
                    ans2=1
        #length2 = len(tokens1)
       # print(length2)
        #print(tokens1)
        #for a in range(0,length2):
         #   for aa in range(0,len(cond_key)):
          #      if(tokens1[a]==cond_key[aa]):
           #        ans='true'
            #    else:
             #       ans='false'
        #for b in range(0,length2):
         #   for bb in range(0,len(action_key)):
          #      if(tokens1[b]==action_key[bb]):
           #                 ans1='true'
            #    else:
             #               ans1='false'
        #print(ans1)
        #print(ans2)
        if(ans1==1 and ans2==1):
             #print("i am in")
                 #ch='yes'
                 #no=1
                 #while ch=="yes":
             tokenizer = RegexpTokenizer(r'\W+')
             pun = ["[","]","!","{","}","#","@","^","%","-","+","?",".","'","(",")",","]
    
                 #example_sent= input("enter the sentence:")
                 #chr = SpellChecker("en_US")  
                 #chr.set_text(example_sent)
                 #for err in chr:
                 #print("error",err.word)
             #print(token1[h])
             #print(tokens1)
             tokens =word_tokenize(token1[h])
                 #tokens=token
             codn = '';
             actions = '';
             act = '';
             acti = '';
             condition = '';
             s1=0
             t1=0
             s=0
             t=0
             cond_flag=0
             action_flag=0
             length = len(tokens)
             #print(length)
             #print(tokens)
             cond_key =["if","when","while","unless","untill","only","whenever","as long as","because","inorder to","after","before","as soon as","if only","only if","since","incase",]
             action_key =["shall","then","do","on","will","please","would","should","could","might",]
             for zz in range(0,length):
                 for z in range(0,len(pun)):
                     if(tokens[zz]==pun[z]):
                        tokens[zz]=''
             for x in range(0, length):
                 for xx in range(0,len(cond_key)):
                      if(tokens[x] == cond_key[xx] and s1==0):
                           s1 = x
                           #print("con")
                           #print(s1)
                           cond_flag=1
                         #for x in range(0, length):
             #print(x)
             if(cond_flag==1):
                  for y in range(0,length):
                        for yy in range(0,len(action_key)):
                             if(tokens[y]==action_key[yy] and t1==0):
                                       t1 = y
                                       #print(t1)

             if(t1<s1):
                  t1=length     
                  #print(t1)
             for st in range(s1+1,t1):
                    #print(st)
                    condition += tokens[st]
                    condition += '\t'
 
             ctok=word_tokenize(condition)

             t1=1
             for cc in range (0,len(ctok)):
                    if(ctok[cc]=="is" or ctok[cc]=="=" or ctok[cc]=="equals" or ctok[cc]=="set"):
                          ctok[cc]="="
                    if(ctok[cc]=="larger" or ctok[cc]==">" or ctok[cc]=="greater" or ctok[cc]=="above" or ctok[cc]=="greater" and ctok[cc+1]=="than"):
                           t1 = 0
                           t2=cc-1
                           ctok[cc]=">"
                    if(ctok[cc]=="smaller" or ctok[cc]=="<" or ctok[cc]=="lesser" or ctok[cc]=="below" or ctok[cc]=="lesser" and ctok[cc+1]=="than"):
                           ctok[cc]="<"
                           t1=0
                           t2=cc-1
                    if(t1==0):
                        if(ctok[t2]=="is"):
                         ctok[t2]=''

             for x1 in range(0, length):
                  for xx in range(0,len(action_key)):
                     if(tokens[x1] == action_key[xx] and s==0):
                             s = x1
                             #print("act")
                             #print(s)
                             action_flag=1
             if(action_flag==1):
                   for x1 in range(0, length):
                       # for y in range(x+1,length):
                       for yy in range(0,len(cond_key)):
                           if(tokens[x1]==cond_key[yy] and t==0):
                            t=x1
             if(t<s):
                  t=length
             for s1 in range(s+1,t):
                  acti += tokens[s1]
                  acti += '\t'
                  act=word_tokenize(acti) 
                     #c.execute("insert into output (req_no, condition, action) values (?, ?, ?)",
                      #       (12, codn, act))
                      #c.execute('''select condition from output''')
                      #rows=c.fetchall()
                      #print(rows[0])
                      #for row in rows:
                      #   print(row)
             for aa in range(0,len(ctok)):
                    codn+=ctok[aa]
                    codn+="\t"
             for aa in range(0,len(act)):
                    actions+=act[aa]
                    actions+="\t"
                  #tab=(['condn','action'],[codn,actions])
                  #tt=tabulate(tab)
             print("condition")
             print(codn)
    
             print("action")
             print(actions)
             
        else:
            sent=tokens1
            #transulation=str.maketrans("","",string.punctuation)
            #new=sent.translate(transulation)
            #print(new)
            #lower_case=str.lower(new)
            #print(lower_case)
            stop_words= ('their','be','are','ourselves','these','were','but','because','few','his','and','before','them','me','was','been','so','should','theirs','did','are','yourself','why','being','a','same','our','he','has','have','she','above','my','can','that','each','under','is','won','its','we','isn','just','here','haven','than','again','some','or','her','between','up','of','out','with','had','more','i','there','hadn','from','the','mightn','during','itself','most','herself','ll','very','yours','himself','which','on','when','down','at','mustn','you','does','this','it','who','will','themselves','those','they','wasn','how','hers','myself','would','as','has','whom','own','could','should','didn','once','in','what','against','where','any','other','am','if','for','ours','him','through','ve','all','your','then','too','yourselves','having','weren','an','needn')
            #print(stop_words)
            #words= word_tokenize(sent)
            filtered_sent=[]
            for w in sent:
                if w not in stop_words:
                    filtered_sent.append(w)
            print("statement")        
            print(filtered_sent)

            
def correct(token1):
    sentence='';
    #print("i am in filecorrect")
    #print(token1)
    length=len(token1)
    for x in range(0,length):
        token=word_tokenize(token1[x])
        d=enchant.Dict("en_US")
        #token=word_tokenize(sent)
        #print(token)
        length=len(token)
        for a in range(0,length):
            chkr=SpellChecker("en_US")
            #print(a)
            temp=token[a]
            #print(temp)
            x=d.check(temp)
            #chkr.set_text(temp)
            #print(x)
            if x == False:
                #print("it is fales")
                #chkr=SpellChecker("en_US")
                #chkr.set_text(temp)
                #for err in chkr:
                    #b=err.word
                #d=enchant.Dict("en_US")
                #c=d.suggest(a)
                print("there is a mismatch"+" "+temp+" "+" in this sentence")
                print("do you want to replace type s")
                print("do you want to ignore type i")
                print("do you want to add the word to the dictionary then type a")
                #des='s'
                dec=input("s/i/a")
                if dec=="s":
                    c=d.suggest(temp)
                    print("suggestion",c)
                    token[a]=input("enter replace")
                    print(token)
                elif dec=="i":
                    print("ignored")
                elif dec=='a':
                    d.add(temp)
                    print("added to dictionary")
            sentence=sentence + token[a]+' '
            #print(sentence)
            #print('k')
    ans=sent_tokenize(sentence)
    #print(ans)
    length2=len(ans)
    #print(length2)

    divide1(ans)                                    


def divide1(ans):
    #print("i am in")
    from nltk.tokenize import sent_tokenize, word_tokenize
    from nltk.tokenize import RegexpTokenizer
    from enchant.checker import SpellChecker
    #ch='yes'
    #no=1
    #while ch=="yes":
    cond_key =["if","when","while","unless","untill","only","whenever","as long as","because","inorder to","after","before","as soon as","if only","only if","since","incase",]
    action_key =["shall","then","do","on","will","please","would","should","could","might",]
    length1=len(ans)
    #print(length1)
    tokenizer = RegexpTokenizer(r'\W+')
    pun = ["[","]","!","{","}","#","@","^","%","-","+","?",".","'","(",")",","]
    #for zz in range(0,length):
        #for z in range(0,len(pun)):
            #if(tokens[zz]==pun[z]):
              # tokens[zz]=''

    

    for h in range(0,length1):
        ans1=0
        ans2=0
        tokens1 = word_tokenize(ans[h])
        length2=len(tokens1)
        #print(length2)
        for a1 in range(0,length2):
            for a2 in range(0,len(pun)):
                if(tokens1[a1]==pun[a2]):
                      tokens1[a1]=''
        length3=len(tokens1)
        #print(length3)
        for a3 in range(0,length3):
            for a4 in range(0,len(cond_key)):
                if(tokens1[a3]==cond_key[a4] and ans1==0):
                    #print(tokens1[a3])
                    ans1=1
        for a5 in range(0,length3):
            for a6 in range(0,len(action_key)):
                if(tokens1[a5]==action_key[a6] and ans2==0):
                    #print(tokens1[a5])
                    ans2=1
        #length2 = len(tokens1)
       # print(length2)
        #print(tokens1)
        #for a in range(0,length2):
         #   for aa in range(0,len(cond_key)):
          #      if(tokens1[a]==cond_key[aa]):
           #        ans='true'
            #    else:
             #       ans='false'
        #for b in range(0,length2):
         #   for bb in range(0,len(action_key)):
          #      if(tokens1[b]==action_key[bb]):
           #                 ans1='true'
            #    else:
             #               ans1='false'
        #print(ans1)
        #print(ans2)
        if(ans1==1 and ans2==1):
             #print("i am in")
                 #ch='yes'
                 #no=1
                 #while ch=="yes":
             tokenizer = RegexpTokenizer(r'\W+')
             pun = ["[","]","!","{","}","#","@","^","%","-","+","?",".","'","(",")",","]
    
                 #example_sent= input("enter the sentence:")
                 #chr = SpellChecker("en_US")  
                 #chr.set_text(example_sent)
                 #for err in chr:
                 #print("error",err.word)
             #print(ans[h])
             #print(tokens1)
             tokens =word_tokenize(ans[h])
                 #tokens=token
             codn = '';
             actions = '';
             act = '';
             acti = '';
             condition = '';
             s1=0
             t1=0
             s=0
             t=0
             cond_flag=0
             action_flag=0
             length = len(tokens)
             #print(length)
             #print(tokens)
             cond_key =["if","when","while","unless","untill","only","whenever","as long as","because","inorder to","after","before","as soon as","if only","only if","since","incase",]
             action_key =["shall","then","do","on","will","please","would","should","could","might",]
             for zz in range(0,length):
                 for z in range(0,len(pun)):
                     if(tokens[zz]==pun[z]):
                        tokens[zz]=''
             for x in range(0, length):
                 for xx in range(0,len(cond_key)):
                      if(tokens[x] == cond_key[xx] and s1==0):
                           s1 = x
                           #print("con")
                           #print(s1)
                           cond_flag=1
                         #for x in range(0, length):
             #print(x)
             if(cond_flag==1):
                  for y in range(0,length):
                        for yy in range(0,len(action_key)):
                             if(tokens[y]==action_key[yy] and t1==0):
                                       t1 = y
                                       #print(t1)

             if(t1<s1):
                  t1=length     
                  #print(t1)
             for st in range(s1+1,t1):
                    #print(st)
                    condition += tokens[st]
                    condition += '\t'
 
             ctok=word_tokenize(condition)

             t1=1
             for cc in range (0,len(ctok)):
                    if(ctok[cc]=="is" or ctok[cc]=="=" or ctok[cc]=="equals" or ctok[cc]=="set"):
                          ctok[cc]="="
                    if(ctok[cc]=="larger" or ctok[cc]==">" or ctok[cc]=="greater" or ctok[cc]=="above" or ctok[cc]=="greater" and ctok[cc+1]=="than"):
                           t1 = 0
                           t2=cc-1
                           ctok[cc]=">"
                    if(ctok[cc]=="smaller" or ctok[cc]=="<" or ctok[cc]=="lesser" or ctok[cc]=="below" or ctok[cc]=="lesser" and ctok[cc+1]=="than"):
                           ctok[cc]="<"
                           t1=0
                           t2=cc-1
                    if(t1==0):
                        if(ctok[t2]=="is"):
                         ctok[t2]=''

             for x1 in range(0, length):
                  for xx in range(0,len(action_key)):
                     if(tokens[x1] == action_key[xx] and s==0):
                             s = x1
                             #print("act")
                             #print(s)
                             action_flag=1
             if(action_flag==1):
                   for x1 in range(0, length):
                       # for y in range(x+1,length):
                       for yy in range(0,len(cond_key)):
                           if(tokens[x1]==cond_key[yy] and t==0):
                            t=x1
             if(t<s):
                  t=length
             for s1 in range(s+1,t):
                  acti += tokens[s1]
                  acti += '\t'
                  act=word_tokenize(acti) 
                     #c.execute("insert into output (req_no, condition, action) values (?, ?, ?)",
                      #       (12, codn, act))
                      #c.execute('''select condition from output''')
                      #rows=c.fetchall()
                      #print(rows[0])
                      #for row in rows:
                      #   print(row)
             for aa in range(0,len(ctok)):
                    codn+=ctok[aa]
                    codn+="\t"
             for aa in range(0,len(act)):
                    actions+=act[aa]
                    actions+="\t"
                  #tab=(['condn','action'],[codn,actions])
                  #tt=tabulate(tab)
             print("condition")
             print(codn)
    
             print("action")
             print(actions)
             
        else:
            sent=tokens1
            #transulation=str.maketrans("","",string.punctuation)
            #new=sent.translate(transulation)
            #print(new)
            #lower_case=str.lower(new)
            #print(lower_case)
            stop_words= ('their','be','are','ourselves','these','were','but','because','few','his','and','before','them','me','was','been','so','should','theirs','did','are','yourself','why','being','a','same','our','he','has','have','she','above','my','can','that','each','under','is','won','its','we','isn','just','here','haven','than','again','some','or','her','between','up','of','out','with','had','more','i','there','hadn','from','the','mightn','during','itself','most','herself','ll','very','yours','himself','which','on','when','down','at','mustn','you','does','this','it','who','will','themselves','those','they','wasn','how','hers','myself','would','as','has','whom','own','could','should','didn','once','in','what','against','where','any','other','am','if','for','ours','him','through','ve','all','your','then','too','yourselves','having','weren','an','needn')
            #print(stop_words)
            #words= word_tokenize(sent)
            filtered_sent=[]
            for w in sent:
                if w not in stop_words:
                    filtered_sent.append(w)
            print("statement")        
            print(filtered_sent)

    

def divide(token1):
    #print("i am in")
    from nltk.tokenize import sent_tokenize, word_tokenize
    from nltk.tokenize import RegexpTokenizer
    from enchant.checker import SpellChecker
    #ch='yes'
    #no=1
    #while ch=="yes":
    cond_key =["if","when","while","unless","untill","only","whenever","as long as","because","inorder to","after","before","as soon as","if only","only if","since","incase",]
    action_key =["shall","then","do","on","will","please","would","should","could","might",]
    length1=len(token1)
    #print(length1)
    tokenizer = RegexpTokenizer(r'\W+')
    pun = ["[","]","!","{","}","#","@","^","%","-","+","?",".","'","(",")",","]
    #for zz in range(0,length):
        #for z in range(0,len(pun)):
            #if(tokens[zz]==pun[z]):
              # tokens[zz]=''

    

    for h in range(0,length1):
        ans1=0
        ans2=0
        tokens1 = word_tokenize(token1[h])
        length2=len(tokens1)
        #print(length2)
        for a1 in range(0,length2):
            for a2 in range(0,len(pun)):
                if(tokens1[a1]==pun[a2]):
                      tokens1[a1]=''
        length3=len(tokens1)
        #print(length3)
        for a3 in range(0,length3):
            for a4 in range(0,len(cond_key)):
                if(tokens1[a3]==cond_key[a4] and ans1==0):
                    #print(tokens1[a3])
                    ans1=1
        for a5 in range(0,length3):
            for a6 in range(0,len(action_key)):
                if(tokens1[a5]==action_key[a6] and ans2==0):
                    #print(tokens1[a5])
                    ans2=1
        #length2 = len(tokens1)
       # print(length2)
        #print(tokens1)
        #for a in range(0,length2):
         #   for aa in range(0,len(cond_key)):
          #      if(tokens1[a]==cond_key[aa]):
           #        ans='true'
            #    else:
             #       ans='false'
        #for b in range(0,length2):
         #   for bb in range(0,len(action_key)):
          #      if(tokens1[b]==action_key[bb]):
           #                 ans1='true'
            #    else:
             #               ans1='false'
        #print(ans1)
        #print(ans2)
        if(ans1==1 and ans2==1):
             #print("i am in")
                 #ch='yes'
                 #no=1
                 #while ch=="yes":
             tokenizer = RegexpTokenizer(r'\W+')
             pun = ["[","]","!","{","}","#","@","^","%","-","+","?",".","'","(",")",","]
    
                 #example_sent= input("enter the sentence:")
                 #chr = SpellChecker("en_US")  
                 #chr.set_text(example_sent)
                 #for err in chr:
                 #print("error",err.word)
             #print(token1[h])
             #print(tokens1)
             tokens =word_tokenize(token1[h])
                 #tokens=token
             codn = '';
             actions = '';
             act = '';
             acti = '';
             condition = '';
             s1=0
             t1=0
             s=0
             t=0
             cond_flag=0
             action_flag=0
             length = len(tokens)
             #print(length)
             #print(tokens)
             cond_key =["if","whether","when","while","unless","untill","only","whenever","as long as","because","inorder to","after","before","as soon as","if only","only if","since","incase",]
             action_key =["shall","then","do","on","will","please","would","should","could","might",]
             for zz in range(0,length):
                 for z in range(0,len(pun)):
                     if(tokens[zz]==pun[z]):
                        tokens[zz]=''
             for x in range(0, length):
                 for xx in range(0,len(cond_key)):
                      if(tokens[x] == cond_key[xx] and s1==0):
                           s1 = x
                           #print("con")
                           #print(s1)
                           cond_flag=1
                         #for x in range(0, length):
             #print(x)
             if(cond_flag==1):
                  for y in range(0,length):
                        for yy in range(0,len(action_key)):
                             if(tokens[y]==action_key[yy] and t1==0):
                                       t1 = y
                                       #print(t1)

             if(t1<s1):
                  t1=length     
                  #print(t1)
             for st in range(s1+1,t1):
                    #print(st)
                    condition += tokens[st]
                    condition += '\t'
 
             ctok=word_tokenize(condition)

             t1=1
             for cc in range (0,len(ctok)):
                    if(ctok[cc]=="is" or ctok[cc]=="=" or ctok[cc]=="equals" or ctok[cc]=="set"):
                          ctok[cc]="="
                    if(ctok[cc]=="larger" or ctok[cc]==">" or ctok[cc]=="greater" or ctok[cc]=="above" or ctok[cc]=="greater" and ctok[cc+1]=="than"):
                           t1 = 0
                           t2=cc-1
                           ctok[cc]=">"
                    if(ctok[cc]=="smaller" or ctok[cc]=="<" or ctok[cc]=="lesser" or ctok[cc]=="below" or ctok[cc]=="lesser" and ctok[cc+1]=="than"):
                           ctok[cc]="<"
                           t1=0
                           t2=cc-1
                    if(t1==0):
                        if(ctok[t2]=="is"):
                         ctok[t2]=''

             for x1 in range(0, length):
                  for xx in range(0,len(action_key)):
                     if(tokens[x1] == action_key[xx] and s==0):
                             s = x1
                             #print("act")
                             #print(s)
                             action_flag=1
             if(action_flag==1):
                   for x1 in range(0, length):
                       # for y in range(x+1,length):
                       for yy in range(0,len(cond_key)):
                           if(tokens[x1]==cond_key[yy] and t==0):
                            t=x1
             if(t<s):
                  t=length
             for s1 in range(s+1,t):
                  acti += tokens[s1]
                  acti += '\t'
                  act=word_tokenize(acti) 
                     #c.execute("insert into output (req_no, condition, action) values (?, ?, ?)",
                      #       (12, codn, act))
                      #c.execute('''select condition from output''')
                      #rows=c.fetchall()
                      #print(rows[0])
                      #for row in rows:
                      #   print(row)
             for aa in range(0,len(ctok)):
                    codn+=ctok[aa]
                    codn+="\t"
             for aa in range(0,len(act)):
                    actions+=act[aa]
                    actions+="\t"
                  #tab=(['condn','action'],[codn,actions])
                  #tt=tabulate(tab)
             print("condition")
             print(codn)
    
             print("action")
             print(actions)
             
        else:
            sent=tokens1
            #transulation=str.maketrans("","",string.punctuation)
            #new=sent.translate(transulation)
            #print(new)
            #lower_case=str.lower(new)
            #print(lower_case)
            stop_words= ('their','be','are','ourselves','these','were','but','because','few','his','and','before','them','me','was','been','so','should','theirs','did','are','yourself','why','being','a','same','our','he','has','have','she','above','my','can','that','each','under','is','won','its','we','isn','just','here','haven','than','again','some','or','her','between','up','of','out','with','had','more','i','there','hadn','from','the','mightn','during','itself','most','herself','ll','very','yours','himself','which','on','when','down','at','mustn','you','does','this','it','who','will','themselves','those','they','wasn','how','hers','myself','would','as','has','whom','own','could','should','didn','once','in','what','against','where','any','other','am','if','for','ours','him','through','ve','all','your','then','too','yourselves','having','weren','an','needn')
            #print(stop_words)
            #words= word_tokenize(sent)
            filtered_sent=[]
            for w in sent:
                if w not in stop_words:
                    filtered_sent.append(w)
            print("statement")        
            print(filtered_sent)






print("want to read a statement from file or do you want to enter")
print("pree 1 for reading a file")
print("press 2 for entering a requirement" )
print("press 3 for tokenize")
print("press 4 for parts of speech")
a=input("enter your decision")
dec=a
#print(dec)
if dec=='1':    
    count=0
    filename=input("enter the path")
    f=open(filename,mode='r',encoding='utf-8')
    a=f.read()
    print(a)
    f.close()
    token1=sent_tokenize(a)
    length=len(token1)
    for x in range(0,length):

        token=word_tokenize(token1[x])
        d=enchant.Dict("en_US")
        #token=word_tokenize(sent)
        #print(token)
        length=len(token)
        for a in range(0,length):
            chkr=SpellChecker("en_US")
            #print(a)
            temp=token[a]
            #print(temp)
            x=d.check(temp)
            #chkr.set_text(temp)
            #print(x)
            if x == False:
                count=count+1
    if count > 0:
        filecorrect(token1)
    else:
        print("do you want to save the file")
        e=input("if yes, press k or press n")
        if e =='k':
            filesavedivide(token1)
        elif e == 'n':
            filedivide(token1)
            
elif dec=='2':
    count=0
    a=input("enter")
    #filename=input("enter the path")
    #f=open(filename,mode='r',encoding='utf-8')
    #a=f.read()
    #print(a)
    #f.close()
    token1=sent_tokenize(a)
    length=len(token1)
    for x in range(0,length):

        token=word_tokenize(token1[x])
        d=enchant.Dict("en_US")
        #token=word_tokenize(sent)
        #print(token)
        length=len(token)
        for a in range(0,length):
            chkr=SpellChecker("en_US")
            #print(a)
            temp=token[a]
            #print(temp)
            x=d.check(temp)
            #chkr.set_text(temp)
            #print(x)
            if x == False:
                count=count+1
    if count > 0:
        correct(token1)
    else:
        filedivide(token1)
    
elif dec=='3':
    sentence='';
    input_sent=input("enter ")
    token1=sent_tokenize(input_sent)
    #print(token1)
    length=len(token1)
    for x in range(0,length):
        token=word_tokenize(token1[x])
        d=enchant.Dict("en_US")
        #token=word_tokenize(sent)
        #print(token)
        length=len(token)
        for a in range(0,length):
            chkr=SpellChecker("en_US")
            #print(a)
            temp=token[a]
            #print(temp)
            x=d.check(temp)
            #chkr.set_text(temp)
            #print(x)
            if x == False:
                #print("it is fales")
                #chkr=SpellChecker("en_US")
                #chkr.set_text(temp)
                #for err in chkr:
                    #b=err.word
                #d=enchant.Dict("en_US")
                #c=d.suggest(a)
                print("there is a spelling mistake"+" "+temp+" "+ " in this sentence")
                print("do you want to replace type s")
                print("do you want to ignore type i")
                print("do you want to add the word to the dictionary then type a")
                #des='s'
                dec=input("s/i/a")
                if dec=="s":
                    c=d.suggest(temp)
                    print("suggestion",c)
                    token[a]=input("enter replace")
                    print(token)
                elif dec=="i":
                    print("ignored")
                elif dec=='a':
                    d.add(temp)
                    print("added to dictionary")
            sentence=sentence + token[a]+' '
            #print(sentence)
            #print('k')
    ans=sent_tokenize(sentence)
    length1=len(ans)
    for w in range(0,length1):
        print("statement")
        print(ans[w])

    
elif dec=='4':
    sentence='';
    input_sent=input("enter ")
    token1=sent_tokenize(input_sent)
    #print(token1)
    length=len(token1)
    for x in range(0,length):
        token=word_tokenize(token1[x])
        d=enchant.Dict("en_US")
        #token=word_tokenize(sent)
        #print(token)
        length=len(token)
        for a in range(0,length):
            chkr=SpellChecker("en_US")
            #print(a)
            temp=token[a]
            #print(temp)
            x=d.check(temp)
            #chkr.set_text(temp)
            #print(x)
            if x == False:
                #print("it is fales")
                #chkr=SpellChecker("en_US")
                #chkr.set_text(temp)
                #for err in chkr:
                    #b=err.word
                #d=enchant.Dict("en_US")
                #c=d.suggest(a)
                print("there is a spelling mistake"+" "+temp+" "+" in this sentence")
                print("do you want to replace type s")
                print("do you want to ignore type i")
                print("do you want to add the word to the dictionary then type a")
                #des='s'
                dec=input("s/i/a")
                if dec=="s":
                    c=d.suggest(temp)
                    print("suggestion",c)
                    token[a]=input("enter replace")
                    print(token)
                elif dec=="i":
                    print("ignored")
                elif dec=='a':
                    d.add(temp)
                    print("added to dictionary")
            sentence=sentence + token[a]+' '
            #print(sentence)
            #print('k')
    ans=sent_tokenize(sentence)
    length1=len(ans)
    for w in range(0,length1):
        text1=word_tokenize(ans[w])
        a=nltk.pos_tag(text1)
        print("parts of speech")
        print(a)
        
    
    
    
    
