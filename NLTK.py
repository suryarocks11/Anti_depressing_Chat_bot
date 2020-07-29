#import nltk
#import textblob
from textblob import TextBlob

def decide_sentiment(line):
    if (TextBlob(line).sentiment.polarity) ==0:
        print("User feels neautal or there is some problem with grammer.")
        return("User feels neautal or there is some problem with grammer.")
    if (TextBlob(line).sentiment.polarity) >0:
            print ("User feels postive about it")
            return("User feels postive about it")
    else :
        print("User feels negative about it")
        return("User feels negative about it")

def predict_Sentiment_score (line):
   # print(line)
    print (TextBlob(line).sentiment)
    print (TextBlob(line).sentiment.polarity)
    #print(decide_sentiment(line))

    return(TextBlob(line).sentiment.polarity)
def overall_senti_score(avg_score):
    avg_score = (avg_score*100)
    if avg_score <-60 :
        return(str(avg_score)+'% Very Negative')
    elif avg_score >-60 and avg_score <0:
        return (str(avg_score)+'% Negative')
    elif avg_score >60 :
        return (str(avg_score)+'% Very Positive')        
    else:
        return (str(avg_score)+'% Positive')

#print(overall_senti_score(-70))
#print(overall_senti_score(-58))
#print(overall_senti_score(65))
#print(overall_senti_score(60))
    
# Main parts
data_file = 'data_senti.csv'
with open(data_file ) as r:
    content = r.readlines()
    for line in content:
        pass
        #print(line)
        #predict_Sentiment(line) 
Answer_list=[]
Ans=''
Thought =''
Thought_list =[]
Thought_Polarity=[]
def chat_bot(feeling):
    Answer_list=[]
    exit_flag=0

    while (exit_flag !=1):
        Thought_list.clear() 
        Answer_list =[]
        predict_Sentiment_list=[]
        print ('Hello I am Emotional Robot . You can share your thoughts')
        Ans = input('Whats Your Name?')
        print (Answer_list)
        Answer_list.append(Ans)
        Ans =input('Whats Your Age?')
        Answer_list.append(Ans)
        Thought =input('Please Share Your Though number 1 ')
        Thought_list.append(Thought)
        Answer_list.append(Thought)
        Thought =input('Please Share Your Though number 2 ')
        Thought_list.append(Thought)
        Answer_list.append(Thought)
        Thought =input('Please Share Your Though number 3 ')
        Thought_list.append(Thought)
        Answer_list.append(Thought)


        


        for ans in Thought_list:
            #predict_Sentiment(ans)
            predict_Sentiment_list.append(decide_sentiment(ans))
            Thought_Polarity.append(predict_Sentiment_score(ans))
        Total_Feelings= sum((Thought_Polarity))
        Average = Total_Feelings/3

        with open ('Feeling.csv','a') as W1:
            W1.write(str(Answer_list[0])+" , "+str(Answer_list[1])+ ' , '+str(Answer_list[2])+' : '+ str(predict_Sentiment_list[0])+' , '+str(Answer_list[3])+ \
                 ":"+ str(predict_Sentiment_list[1])+' , '+str(Answer_list[4])+ ":"+str(predict_Sentiment_list[2]) +" , " +" , " + str(overall_senti_score (Average))+ '\n')  
        print(Total_Feelings)
        print(Average)
        Ans =input('Thanks For you entry. Type bye to exit Or Hi to start the test again. ')
        if Ans =='bye':
            print('Bye Bye . Take Care')


            exit_flag =1
    




chat_bot('Test')
print (Answer_list)
 