class Game:
	def __init__(self,player1,player2):
		guess = list("apricot")
		secret = list(len(guess) * "*")
		gameover = True
		while gameover:
			player1 = input("Player1 tell a letter to guess the word - ::")
			if player1 in guess:
				for x in range(len(guess)):
					if guess[x] == player1:
						secret[x] = player1
						print(secret)
					if guess == secret:
						print("Player1 you win!!!!")
						gameover = False
						break

			if list(player1) == guess:
				print("Player1 you win!!!!")
				gameover = False
				break

			player2 = input("Player2 tell a letter to guess the word - ::")
			if player2 in guess:
				for x in range(len(guess)):
					if guess[x] == player2:
						secret[x] = player2
						print(secret)
					if guess == secret:
						print("Player2 you win!!!!")
						gameover = False
						break

			if list(player1) == guess:
				print("Player1 you win!!!!")
				gameover = False
				break


