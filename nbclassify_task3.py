import os,re,math,sys

l=set()       # this is set for the stop words
l.add("i")  #stop word
l.add("me") #stop word
l.add("my") #stop word
l.add("myself") #stop word
l.add("we") #stop word
l.add("to") #stop word
l.add("and")    #stop word
l.add("the")    #stop word
l.add("our")    #stop word
l.add("ours")   #stop word
l.add("ourselves")  #stop word
l.add("you")    #stop word
l.add("your")   #stop word


op=open("nboutput.txt", "a+",encoding="latin1")


def classifier(fpath):
    sp_msg_spam = 0
    hp_msg_spam = 0
    #print(fpath)
    hfobj = open(fpath, "r", encoding="latin1")
    hst = hfobj.read()
    hfobj.close()
    for hword in re.sub('\s\s+', ' ', hst).strip().split():
        tword = hword.lower()  # tword contains the lower case of each word
        #print(tword)
        pmsg_spam=1
        if tword.isdigit():
            continue

        if tword in l:
            continue

        if tword in scount:
            snum=scount[tword]
            sdeno=sword_count
            #print(" tword : "+tword+" spam: num "+ str(snum) +" spam deno "+str(sdeno))
            sp_msg_spam=math.log((snum+1)/(sdeno+len(vocab)))+sp_msg_spam
            #print(sp_msg_spam)
            #print(scount[tword])
            #snum=scount[tword]
            #sdeno=len()


        else:                                           #case for add one smoothing where the word is not present in the dictionary
            #continue
            sp_msg_spam=math.log((1)/(sword_count+len(vocab))) +sp_msg_spam    #add one smoothing applied!!!!!!!!!!!!!!!!
        #pmsg_spam*=scount[tword]

        if tword in hcount:
            #print(hcount[tword])
            hnum=hcount[tword]
            hdeno=hword_count
            #print(" num " + str(hnum) + " deno " + str(hdeno),end="              ")
            hp_msg_spam=math.log((hnum+1)/(hdeno+len(vocab)))+hp_msg_spam
            #print(hp_msg_spam)
        else:                                           #case for add one smoothing where the word is not present in the dictionary
            #continue
            hp_msg_spam = math.log((1) / (hword_count + len(vocab))) + hp_msg_spam       #add one smoothing applied!!!!!!!!!!!!!!!!
    #print(fpath + " spam " + str(sp_msg_spam) +" ham "+str(hp_msg_spam))
    #print(" Prob of spam: "+str(math.log(pspam))+" Prob of ham "+str(math.log(pham)))
    sfinal_prob=math.log(pspam) +sp_msg_spam        #the final probaility of entire message
    hfinal_prob=math.log(pham) +hp_msg_spam         #the final probability of entire message

    #print(fpath+ " spam "+str(sfinal_prob) + " ham "+str(hfinal_prob))

    if(sfinal_prob>hfinal_prob):
        greater="spam"

    else:
        greater="ham"


    op.write(greater+" "+fpath+"\n")

    return



tot_spam_ham_files=0
hfilecount=0
sfilecount=0
hcount={}   #dictionary for ham files key:value pairs
scount={}   #dictionary for spam files key:value pairs
vocab={}    #total vocabulary of all words in the training data


#method to find the file nbmodel.txt


with open('nbmodel.txt', "r", encoding="latin1") as f:
    for line in f:
        tot_spam_ham_files += 1  # this stores the total count of spam and ham files
        class_ham_spam=line.split(",",1)[0].lower()     #class_ham_spam checks if 1st word in the nbmodel.txt file is ham or spam
        if((class_ham_spam=="ham") or (class_ham_spam=="spam")):
            for word in line.split(","):
                if word.isdigit():
                    continue
                if word.lower() in l:
                    continue
                if word.lower() in vocab:
                    vocab[word.lower()]+=1
                else:
                    vocab[word.lower()]=1


        if(class_ham_spam=="ham"):    # this checks for all ham files
            #print(line)
            hfilecount += 1     #count of total ham files
            for word in line.split(","):
                if word.isdigit():
                    continue
                if word.lower() in l:
                    continue
                if word.lower() in hcount:
                    hcount[word.lower()]+=1
                else:
                    hcount[word.lower()]=1



        if(class_ham_spam=="spam"):   # this checks for all spam files
            #print(line)
            sfilecount+=1       #count of total spam files
            for word in line.split(","):
                if word.isdigit():
                    continue
                if word.lower() in l:
                    continue
                if word.lower() in scount:
                    scount[word.lower()]+=1
                else:
                    scount[word.lower()]=1


        count={}
        #for word in line.split(","):
            #print(word, end=" ")
            #if(word.lower()=="ham"):
               #print(word)

        #print(line)
    print(tot_spam_ham_files)       #total count of files
    print(hfilecount)               #total ham files count
    print(sfilecount)               #total spam files coount
    print(len(hcount))              #total number of words in ham dictionary
    print(len(scount))              #total number of words in spam dictionary
    print(len(vocab))               #total vocabulary

    vcount=len(vocab)               #count of distinct vocabulary
    pspam=sfilecount/tot_spam_ham_files     #probability of spam
    pham=hfilecount/tot_spam_ham_files      #probability of ham

    print(pspam)
    print(pham)
    #vc=open('vocabuary.txt','a+',encoding="latin1")
    #vc.write(str(vocab))

#Now we will process the Development data

sword_count=0   #this has the sum of all words in the spam dictionart
hword_count=0   #this has the sum of all words in the ham dictionary

for sval in scount.values():
    sword_count+=sval

for hval in hcount.values():
    hword_count+=hval

print("sum of all words in spam " +str(sword_count))
print("sum of all words in ham " +str(hword_count))


#topdir = 'C:\\Users\\Arjun\\Desktop\\USC\\Subjets\\fall2016\\csci544\\Assignment1\\Spam or Ham\\dev'              #path to the Development data
topdir=sys.argv[1]
print(topdir)
exten = '.txt'
for root, dirs, files in os.walk(topdir):
    for file in files:
        if file.endswith(".txt"):
            fpath = os.path.join(root, file)  # fpath contains the fully qualified path
            classifier(fpath)


