def lovecalculator():
    name1 = input('first name:')
    name2 = input('second name:')
    word1,word2 = list('true'),list('love')
    count1,count2 = 0,0
    for i in name1 + name2:
        if i in word1:
            count1 += 1
    for i in name1 + name2:
        if i in word2:
            count2 += 1
    score = int(str(count1) + str(count2))
    if score<10 or score>90:
        print("Your score is", score, "you go together like coke and mentos.")
    elif score>40 and score<50:
        print("Your score is", score, "you are alright together.")
    else:
        print("your score is", score)
lovecalculator()