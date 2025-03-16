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

# questions = [
#     ["Which language was uses to build Facebook", "Python", "Java", "C++", "C#", 4],
#     ["Which language was uses to build Facebook", "Python", "Java", "C++", "C#", 4],
#     ["Which language was uses to build Facebook", "Python", "Java", "C++", "C#", 4],
#     ["Which language was uses to build Facebook", "Python", "Java", "C++", "C#", 4],
#     ["Which language was uses to build Facebook", "Python", "Java", "C++", "C#", 4],
#     ["Which language was uses to build Facebook", "Python", "Java", "C++", "C#", 4],
#     ["Which language was uses to build Facebook", "Python", "Java", "C++", "C#", 4],
#     ["Which language was uses to build Facebook", "Python", "Java", "C++", "C#", 4],
#     ["Which language was uses to build Facebook", "Python", "Java", "C++", "C#", 4],
#     ["Which language was uses to build Facebook", "Python", "Java", "C++", "C#", 4],
# ]

# levels = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

# money = 0

# for i in range (0, len(questions)):
#     question = questions[i]
#     print(f"\n\nQuestion for Rs. {levels[i]}")
#     print (f"a. {question[1]} b. {question[2]} c. {question[3]} d. {question[4]}")
#     reply = int(input ("Enter your answer (1-4) "))
#     if (reply == question[-1]):
#         print ("Correct You have won Rs. {levels[i]}")
#         if(i == 4):
#             money = 10000
#     elif (i == 9):
#         money = 320000
#     elif (i == 14):
#         money = 10000000
#     else:
#         print ("Wrong Answer")
#         break

# print (f"You have won Rs. {money}")

    



import random
import string

def generate_random_characters(length=3):
 
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def encode(message):
    encoded_words = []
    
    for word in message.split():
        if len(word) >= 3:
            # Remove the first letter and append it at the end
            modified_word = word[1:] + word[0]
            # Append three random characters at the start and end
            random_start = generate_random_characters()
            random_end = generate_random_characters()
            encoded_word = random_start + modified_word + random_end
        else:
            # Simply reverse the string
            encoded_word = word[::-1]
        
        encoded_words.append(encoded_word)
    
    return ' '.join(encoded_words)

def decode(encoded_message):
    """Decode the secret code language back to the original message."""
    decoded_words = []
    
    for word in encoded_message.split():
        if len(word) < 3:
            # Reverse it
            decoded_word = word[::-1]
        else:
            # Remove 3 random characters from start and end
            modified_word = word[3:-3]
            # Remove the last letter and append it to the beginning
            if len(modified_word) > 0:
                decoded_word = modified_word[-1] + modified_word[:-1]
            else:
                decoded_word = ''
        
        decoded_words.append(decoded_word)
    
    return ' '.join(decoded_words)

if __name__ == "__main__":
    original_message = "Hello world this is a test"
    encoded_message = encode(original_message)
    print("Encoded Message:", encoded_message)
    
    decoded_message = decode(encoded_message)
    print("Decoded Message:", decoded_message)