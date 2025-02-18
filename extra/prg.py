dict={"movie1":"chhava",
      "movie2":"sanam teri kasam",
      "movie3":"emergency"}

f=open("score.txt","w")

for k,v in dict.items():
    #guess=False
    for i in range(13):
        
        x=input("guess movie here:")
        if x == v:
            guess = True 
            f.write("You get 10 points for guessing correctly\n")
            break  # Exit the loop if the correct guess is made
    if guess:
        break
            
    if not guess:
        f.write(f"Better luck next time, you couldn't guess {v} correctly.\n")
f.close()

# dict = {
#     "movie1": "chhava",
#     "movie2": "sanam teri kasam",
#     "movie3": "emergency"
# }

# # Open file to wchhrite scores
# f = open("score.txt", "w")

# # Loop through each movie in the dictionary
# for k, v in dict.items():
#     guess = False  # Flag to track if the movie is guessed correctly
#     for i in range(13):  # Up to 13 attempts for each movie
#         # Prompt the user to guess the movie
#         x = input("Guess movie here: ").strip()  # .strip() to remove any leading/trailing spaces

#         # Check if the input is empty
#         if not x:
#             print("Input cannot be empty. Please try again.")
#             continue  # Skip this iteration and prompt the user again

#         # Check if the guess is correct
#         if x == v:
#             f.write("You get 10 points for guessing correctly\n")
#             guess = True  # Mark the guess as correct
#         break  # Exit the loop if the correct guess is made
        
#     else:
#         f.write("You lose\n")
    
#     # After 13 attempts, if no correct guess, write a message to the file
#     if not guess:
#         f.write(f"Better luck next time, you couldn't guess {v} correctly.\n")

# f.close()  # Close the file after writing
