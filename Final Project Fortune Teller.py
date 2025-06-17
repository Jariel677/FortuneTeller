#Erik Rivera
#1/9/2025
#Fortune teller



# Outputs inatructions to the user
print("Welcome to the Fortune Teller Please follow the instructions /nin order to get your fortune.")

# First output of the fortune teller
print("""\n_____________
|    |     |
|green | blue |
|________|________|
|    |    |
| black | pink|
|_________|_______|\n""")

# Prompting the user for their code choice until they enter one of the values exactly as shown
color = input("Please select a color: ")
while color != "black" and color !="green" and color!= "blue" and color != "pink":
    print("That is an incorrect color choice!")
    color = input("Please select a color: ")

#if the color chosen is an odd length of characters, then I set the num variable
# to an odd number (1) or else they chose an even length color and I set it to an even number 
(0)
# num is a variable that controls which set of inside value to display and is one of the most 
# essential
# parts to this version of the program
if color == "green" or color == "black":
    num = 1;
else:
    num = 0;

# Defines the fortunes using a list
fortunes = [
    "Of course",  # Fortune for number 1
    "No way",     # Fortune for number 2
    "Not now",    # Fortune for number 3
    "Go away",    # Fortune for number 4
    "Never",      # Fortune for number 5
    "Yes!",       # Fortune for number 6
    "Maybe",      # Fortune for number 7
    "No"          # Fortune for number 8
]


lastNumber = 0
    
# Repeat asking the user for a number three times
for i in range(3):	
# If the original color choice was odd then display output
    if num == 1:
        print("""\n                  /|\\
        /|\\    
       / | \\   
      / 6| 1 \\  
     /____|____\\ 
     \\    |    / 
      \\ 5 | 2 /  
       \\  |  /   
        \\ | /    
         \\|/     \n""")

    else:
        print("""\n                  /|\\
        /|\\    
       / | \\   
      / 8| 3 \\  
     /____|____\\ 
     \\    |    / 
      \\ 7 | 4 /  
       \\  |  /   
        \\ | /    
         \\|/     \n""") 
           
    # Asks user to select a number
    number = int(input("Please select a number: "))
    # Saves the last number selected
    lastNumber = number  
    # Outputs number of times the fortune is flippling
    print("Flipping " + str(number) + " times....")
           
    # Shows the pattern based on selected number
    # Handles when user picks pink or blue
    if num == 1:  
        if number == 1 or number == 4 or number == 5 or number == 8:
            print("""\n               / |\\
                      /  | \\
                     /   |  \\
                    / 4  | 7 \\
                   /_____|____\\
                   \\    |    /
                    \\ 3 | 8 /
                     \\  |  /
                      \\ | /
                       \\|/    \n""")
                   
    # Handles when user picks black or green
    else:  
        valid_numbers = {2, 3, 6, 7}
        if number in valid_numbers:
            print("""\n               / |\\
                      /  |  \\
                     /   |   \\
                    / 6  | 1  \\
                   /_____|_____\\
                   \\    |    /
                    \\ 5 | 2 /
                     \\  |  /
                      \\ | /
                       \\|/    \n""")
        
# Gets fortune based on last number selected by user
fortune = fortunes[lastNumber - 1]  
# Outputs last fortune after three numbers are selected
print("Your fortune is: " + fortune)