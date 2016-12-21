import os,sys,codecs,re

topdir = 'C:\\Users\\Arjun\\Desktop\\USC\\Subjets\\fall2016\\csci544\\Assignment1\\Spam or Ham\\train'
#topdir=sys.argv[1]
exten = '.txt'
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
for root, dirs, files in os.walk(topdir):
    for file in files:
        print(" file: "+file,end=" " )
        if file.endswith(".txt"):
            fpath = os.path.join(root, file)  # fpath contains the fully qualified path
            print("fpath: "+fpath,end=" ")
            if ("ham" in fpath):
                #print(fpath)  # prints all the files with ham names
                hpath = fpath  # hpath contains path to ham files
                hfname = hpath.split("\\")
                hcfname = len(hfname)
                hroot_fname = hcfname - 2
                if (hfname[hroot_fname].lower() == "ham"):
                    #print(hpath)
                    hfobj = open(hpath, "r",encoding="latin1")
                    hst = hfobj.read();
                    hfobj.close()       #close the opened file
                    #create a file to write nbmodel.txt
                    hf=open('nbmodel.txt','a+',encoding="latin1" )      #open the file in append mode
                    hf.write("ham,")
                    #hf.write(hpath+",")
                    #print("ham,", end=""),  # printing at end of file as spam or ham
                    for hword in re.sub('\s\s+',' ',hst).strip().split():
                        if hword.isdigit():
                            continue
                        if hword in l:
                            continue
                        else:
                            hf.write(hword + ',')

                        #print(word,end=",")
                    hf.write("\n")

            if ("spam" in fpath):
                #print(fpath)  # prints all the file names with spam names
                spath = fpath
                sfname = spath.split("\\")
                scfname = len(sfname)
                sroot_fname = scfname - 2
                if (sfname[sroot_fname].lower() == "spam"):
                    # print(hpath,end=",")
                    sfobj = open(spath, "r", encoding="latin1")
                    sst = sfobj.read();
                    sfobj.close()
                    # create a file to write nbmodel.txt
                    sf = open('nbmodel.txt', 'a+', encoding="latin1")  # open the file in append mode
                    sf.write("spam,")
                    #sf.write(spath+",")
                    # print("ham,", end=""),  # printing at end of file as spam or ham
                    for sword in re.sub('\s\s+',' ',sst).strip().split():
                        if sword.isdigit():
                            continue
                        if sword in l:
                            continue
                        else:
                            sf.write(sword + ',')
                        # print(word,end=",")
                    sf.write("\n")

