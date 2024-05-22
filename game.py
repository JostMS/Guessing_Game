import random


with open('words.txt', 'r') as file:
   words = file.readlines()

words = [line.strip() for line in words]

secret_word = random.choice(words)
answer = secret_word
letters = list(secret_word)
random.shuffle(letters)
print(" ")
print("Can you guess the word the following letters spell? You have 5 attempts to guess correctly")
print(" ")
print(letters)
print(" ")
max_attempts = 5

for attempt in range(max_attempts):
   guess = input(f"Attempt {attempt + 1}/{max_attempts}: Whats your guess? ")

   if guess.lower() == answer:
      print("Well done! You guessed correctly. The word is", answer)
      break
   else:
      print("incorrect guess. please try again")

else:
   print("Sorry, You've used up all your attempts. The correct answer was", answer)

