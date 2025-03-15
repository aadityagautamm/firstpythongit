# #functions with nested function

# def talk(phrase):
#     def say(word):
#         print(word)
#     words = phrase.split(' ')
#     for word in words:
#         say(word)

# talk('hello world')
 
# def time_input ():
#     while True:
#         try:
#             hours = int(input("Enter hours: "))
#             minutes = int(input("Enter minutes: "))
#             seconds = int(input("Enter seconds: "))
            
#             if 0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
#                 return f"{hours:02}:{minutes:02}:{seconds:02}"  
#             else:
#                     print("Invalid input. Please enter hours between 0 and 23, minutes between 0 and 59, and seconds between 0 and 59.")
        
#         except ValueError:
          
#             print("Invalid input. Please enter numeric values.")
          
# timestamp = time_input()
# print (timestamp)

# if timestamp > '16:00:00':
#     print ("Good Evening")
# elif timestamp > '12:00:00':
#     print ("Good Afternoon")
# else:
#     print ("Good Morning")


# practice using List and other functions

questions = [
    ["Which language was uses to build Facebook", "Python", "Java", "C++", "C#", 4],
    ["Which language was uses to build Facebook", "Python", "Java", "C++", "C#", 4],
    ["Which language was uses to build Facebook", "Python", "Java", "C++", "C#", 4],
    ["Which language was uses to build Facebook", "Python", "Java", "C++", "C#", 4],
    ["Which language was uses to build Facebook", "Python", "Java", "C++", "C#", 4],
    ["Which language was uses to build Facebook", "Python", "Java", "C++", "C#", 4],
    ["Which language was uses to build Facebook", "Python", "Java", "C++", "C#", 4],
    ["Which language was uses to build Facebook", "Python", "Java", "C++", "C#", 4],
    ["Which language was uses to build Facebook", "Python", "Java", "C++", "C#", 4],
    ["Which language was uses to build Facebook", "Python", "Java", "C++", "C#", 4],
]

levels = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

money = 0

for i in range (0, len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print (f"a. {question[1]} b. {question[2]} c. {question[3]} d. {question[4]}")
    reply = int(input ("Enter your answer (1-4) "))
    if (reply == question[-1]):
        print ("Correct You have won Rs. {levels[i]}")
        if(i == 4):
            money = 10000
    elif (i == 9):
        money = 320000
    elif (i == 14):
        money = 10000000
    else:
        print ("Wrong Answer")
        break

print (f"You have won Rs. {money}")

    