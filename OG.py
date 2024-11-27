import pandas as pd
while (True):

    print("")
    print("")
    print("       WELCOME TO THE QUIZ GAME        ")
    print("")
    print("")
    print(" || Game Requirements || ")

    print('')
    print("1.  Eligibility: Only players aged 13-19 are eligible.")
    print('')
    print("2.  School Registration Number: Required for participation.")
    print('')
    print("3.  Game Mechanics: ")
    print('')
    print("       - Five rounds, each with one question.Five rounds, each   with one question.")
    print('')
    print("       - Each correct answer allows access to the next question. ")
    print('')
    print("       - Each question is worth 20 points (total score of 100).  ")
    print('')
    #print("4.  Answer Format: All questions are YES/NO type.")

    print("")


    print("____LET'S START THE GAME!!!_____")

    print   ("_____________________________________________________________________    _________")
    print("")



   


    # Initialize the DataFrame
    data = pd.DataFrame(columns=["Index No","Name","Age","Points"])
#while (True):
    # Collect user input
    print("")
    indexno=int(input("Enter Your Index No: "))
    name=str(input("Enter Your Name : "))
    age=int(input("Enter Your Age : "))
    print("")
    if (age>=13 and age<=19):

        import random

        global points
        points=0
        global count
        count=1
        while (count<=5):
            question_list=[ "Which scientist is known for the Theory of relativity?",
                    "Who is the author of the “Harry Potter” series?",
                    "Who painted the “Mona Lisa”?",
                    "Who won the FIFA World Cup in 2022?",
                    "Who is the CEO of Tesla?",
                    "Who played Iron Man in the Marvel Cinematic Universe?",
                    "What is the name of the tallest building in the world?",
                    "Which planet is known as the Red Planet?",
                    "What is the most popular social media platform in 2022?",
                    "What is the longest river in the world?",
                    "Who created Facebook?",
                    "Who is the author of “The Fault in Our Stars”?",
                    "What is another term for the number 0 in a game of cricket?",
                    "What is the coldest planet in our solar system?",
                    "What is the name of the largest ocean on earth?",
                    "Who is the CEO of Spotify?",
                    "Who is the music composer of “Titanic”?",
                    "What is the highest-grossing movie of all time?",
                    "How many bones are in the human body(In numbers)?",
                    "What is the largest animal on Earth?",
                    "What is the name of the highest mountain in Africa?",
                    "Which country has won the most FIFA World Cup titles?",
                    "Which country has won the most cricket World Cup titles?",
                    "Who was the youngest person to win a Nobel Prize?",
                    "What is the most common letter in the English alphabet",
                    "Which animal has the largest brain compared to its body size?",
                    "What’s the rarest blood type?",
                    "How many sides does a hexagon have(In numbers)?",
                    "Who was the first African U.S. president?",
                    "What city was the first to be attacked with an atomic bomb?",
                    "Which animal sleeps standing up?",
                    "Which animal has the longest lifespan in the world?",
                    "Which social media app is known for its “ghost” logo?",
                    "Which car company is known for the slogan “The Ultimate Driving Machine”?",
                    "Which company owns Lamborghini, Ducati, Porsche, Audi and Bugatti?",
                    "Who is known as the 'Father of the Nation' in India?",
                    "Which famous detective was created by Arthur Conan Doyle?",
                    "What is the name of the President of India?",
                    "Which country won the first-ever Cricket World Cup in 1975?",
                    "Which country is Mount Everest located in?",
                    "Name the largest organ in the human body?",
                    "What is the world’s smallest country?",
                    "How many Harry Potter films have been made?",
                    "The place where Jesus was born?",
                    "Which festival is known as the festival of colors?",
                    "What country first granted women the right to vote?",
                    "What is the best-selling book series of the 21st century?",
                    "Who is the highest-paid football player of all time?",
                    "Who was the first woman to become Prime Minister of India?",
                    "Which country is known for originating the sport of cricket?"]



            Answer_list=["Albert Einstein","J.K.Rowling","Leonardo Da Vinci","Argentina","Elon Musk","Robert Downey Jr","Burj Khalifa","Mars","Instagram","Nile","Mark Zurckerburg","John Green","Duck","Neptune","Pacific","Daniel Ek","James Horner","Avengers Endgame","206","Blue Whale","Kilimanjaro","Brazil","Australia","Malala Yousafzai","E","Ant","AB Negative","6","Barack Obama",  "Hiroshima","Horse","Tortoise","Snapshot","BMW","Volkswagen","Mahatma Gandhi","Sherlock Holmes","Ram Nath Kovind", "West Indies","Nepal","Skin","Vatican","Eight","Bethlehem","Holi","New-Zealand","Harry Potter","Lionel Messi","Indira Gandhi","England"]

            random_question=random.choice(question_list)
            index=question_list.index(random_question)
            Answer=Answer_list[index]

            #user_input=input("Enter the anwser: ")

            def game(question,answer):
                global points
                #global count

                print("====",name,", Your question_",count,"====")
                print(question)

                user_input=input("Enter the anwser: ")

                if (user_input.lower()==answer.lower() ):
                    print("---------",name,", Congratualtions!!! Your answer is correct----------")
                    #print(answer)
                    points=points+20
                    print("-----------------------")
                    return True #continue the loop 
                else:
                    print("")
                    print(name,", Unfortunately Your answer is incorrect. Try Again!!!")
                    print("The correct answer is ",Answer)
                    print(" ")
                    return False #exit the loop

            if not game(random_question,Answer):
                break #stop if the answer is incorrect
            
         
            count+=1
           
        print("Your Total points ",points)

        # Append the new data as a dictionary
        #data=pd.concat([data,pd.DataFrame({"Index No": [indexno],"Name":[name],"Age":[age],"Points": [points]})])
        data=pd.concat([pd.DataFrame({"Index No": [indexno],"Name":[name],"Age":[age],"Points": [points]})])
        #data=pd.concat([data,pd.DataFrame([indexno,name,age,points])])

        file_name="GAME_SUMMARY.csv"
        # Save the data to a CSV file
        if (count==1):
           data.to_csv(file_name,index=False,mode="a",header=True)
           
        else:
            data.to_csv(file_name,index=False,mode="a",header=False)

        #Ask if the user wants to add more entries
        opinion=str(input("Do you wish to continue: (Yes/No)")) 
        if (opinion=="No" or opinion=="no" or opinion=="NO"):
            print("See you, next time!!!")
            break   
        elif (opinion=="Yes" or opinion=="yes" or opinion=="YES"):
            continue             
    
    else:
        print("You are not a teenager, Better luck next time!!!")
        opinion_1=str(input("Do you want to replay: "))
        if (opinion_1=="No" or opinion_1=="no" or opinion_1=="NO"):
            print("See you, next time!!!")

            data=pd.concat([data,pd.DataFrame({"Name":[name],"Age":[age],
                "Points": "No Marks","Index No": [indexno]})])
            # Save the data to a CSV file
            file_name="GAME_SUMMARY.csv"
            data.to_csv(file_name,index=False)
            break   
        elif (opinion_1=="Yes" or opinion_1=="yes" or opinion_1=="YES"):
            continue             



    print("")
    print("Data has been written to ",file_name)
    print("")

    # Read and display the data
df=pd.read_csv("GAME_SUMMARY.csv")
print(df)