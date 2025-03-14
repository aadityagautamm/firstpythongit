# #functions with nested function

# def talk(phrase):
#     def say(word):
#         print(word)
#     words = phrase.split(' ')
#     for word in words:
#         say(word)

# talk('hello world')
 
def time_input ():
    while True:
        try:
            hours = int(input("Enter hours: "))
            minutes = int(input("Enter minutes: "))
            seconds = int(input("Enter seconds: "))
            
            if 0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
                return f"{hours:02}:{minutes:02}:{seconds:02}"  
            else:
                    print("Invalid input. Please enter hours between 0 and 23, minutes between 0 and 59, and seconds between 0 and 59.")
        
        except ValueError:
          
            print("Invalid input. Please enter numeric values.")
          
timestamp = time_input()
print (timestamp)

if timestamp > '16:00:00':
    print ("Good Evening")
elif timestamp > '12:00:00':
    print ("Good Afternoon")
else:
    print ("Good Morning")


# practice using List and other functions

Questions =[["Which language was used to create Instagram?", "python","javascript", "Ruby", "php", "None", 4],
            ["Which language was used to create Instagram?", "python","javascript", "Ruby", "php", "None", 4],
            ["Which language was used to create Instagram?", "python","javascript", "Ruby", "php", "None", 4],]

levels = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]