actual_ham_count=0
actual_spam_count=0
classified_ham_count=0
classified_spam_count=0
correct_ham=0
correct_spam=0
with open('nboutput.txt', "r", encoding="latin1") as f:
    for line in f:
        #print(line)
        classified = line.split(' ',maxsplit=1)[0]
        if(classified=="ham"):
            classified_ham_count=classified_ham_count+1
        if(classified=="spam"):
            classified_spam_count=classified_spam_count+1
        #print(classified, end=" ")
        path=line.split(' ',maxsplit=1)[1]
        #print(path)
        actual=path.split('\\')[12]
        #print(actual)
        if(actual=="ham"):
            actual_ham_count=actual_ham_count+1
        if(actual=="spam"):
            actual_spam_count=actual_spam_count+1
        if(actual==classified and actual=="ham"):
            correct_ham=correct_ham+1
        if(actual==classified and actual=="spam"):
            correct_spam=correct_spam+1

    print("Classified ham count: " +str(classified_ham_count))
    print("Classified spam count: "+str(classified_spam_count))
    print("Actual ham count: "+str(actual_ham_count))
    print("Actual spam count: "+str(actual_spam_count))
    print("correctly classified as ham: "+str(correct_ham))
    print("correctly classified as spam: "+str(correct_spam))

    accuracy=(correct_ham+correct_spam)/(actual_spam_count+actual_spam_count)
    print("Accuracy: "+str(accuracy))

    precision_spam=correct_spam/classified_spam_count
    print("Precesion of spam: "+str(precision_spam))

    precision_ham=correct_ham/classified_ham_count
    print("Precision of ham: "+str(precision_ham))

    recall_spam=correct_spam/actual_spam_count
    recall_ham=correct_ham/actual_ham_count

    print("Recall of spam: "+str(recall_spam))
    print("Recall of ham: "+str(recall_ham ))

    f1_spam=(2*(precision_spam)*recall_spam)/(precision_spam+recall_spam)
    print("F1 of spam: "+str(f1_spam))

    f1_ham=(2*(precision_ham)*recall_ham)/(precision_ham+recall_ham)
    print("F1 of ham: "+str(f1_ham))


