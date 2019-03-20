
# ----------------While Loop Games-----------
# Here we asking input from user for a secret word if input word match with 
# hidden word then "You wind!" will show either ask for guess again untill the guess limits over.

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False

while guess != secret_word and not out_of_guess:  
   if guess_count < guess_limit:
       guess = input("Enter guess:")
       guess_count += 1
   else:
       out_of_guess = True

if out_of_guess:
   print("Out of guess, you lose")
else:
   print("You wind!")