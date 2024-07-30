player = input ("do you want to play?")

if player != "yes":
    quit()

print ('ok lets play')

score=0

question = input ("How many days do we have in a week?")
if question =="seven":
    print("correct")
    score +=1
else:
    print('incorret')

question = input ("In which direction does the sun rise?")
if question =="east":
    print("correct")
    score +=1
else:
    print('incorret')

question = input ("what is our national brid?")
if question =="peacock":
    print("correct")
    score +=1
else:
    print('incorrect')  

print("your score"+str (score))  