print("Welcome CLexa shippers")


name = input("What is your name? ")
watched = input("Have you watched The 100 yet?(yes/no) ").lower()

if watched == "yes":
  print("Bravo! Let's see how much do you know about CLexa ship. ")
  
  conclave = int(input("How many iniciates were in Lexa's conclave? ")) 
  if conclave == 9:
    print(name, "correct! That was the number of all the initiates that year. ")

    ran_away = input("And who ran away from the conclave? ")
    if ran_away == "Luna":
      print("Good memory there.")
      
      kissed = int(input("How many times have Clarke and Lexa kissed in the show?(All 7 seasons) "))
      if kissed == 4:
        print("You do know something about CLexa ship. ") 
        
      else:
        print("You need to watch first 3 seasons again. And I'm going to let you.")

    else:
      print("Watch the show again. Life should be more than just serviving. ")

  elif conclave == 8:
    print("Correct,", name +". Luna didn't join the conclave and went back to her people.")

  else:
    print("No shit. You missed the best part of this ship. ")


elif watched == "no":
  print("What a shamed, you should check it out on Netflix now.")
else:
  print("Please answer with yes or no.")


'''
string "str 1", 'str 2'
int 8, -4, 1000
float 6.2, 7.0, -8.1
bool True, False
'''

# comment 1 line
