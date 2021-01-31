import random

def hangman():
	fail = 0
	list_word = ["процессор", "видеокарта", "монитор", "клавиатура"]
	rand = random.randint(0, 3)

	word = list_word[rand]
	stages = ["",
			 " ___________",
			 "|          | ",
			 "|          | ",
			 "|          0         ",
			 "|        / | \       ",
			 "|         / \        ",
			 "|                     "
			 ]
	win = False
	rletters = list(word)
	board = ["__"] * len(word)
	while fail < len(stages):
		msg = input("Введите букву: ") 
		if msg in rletters:
			cind = rletters.index(msg)
			board[cind] = msg
			rletters[cind] = '$'
		else:
			fail += 1
			e = fail + 1
		print((" ".join(board)))
		print("\n".join(stages[0 : e]))
		if "__" not in board:
			print("You win!")
			print("Было загадано слово: '{}'".format(word))
			win = True
			break
	if not win:
		print("\n".join(stages[0:fail]))
		print("You lose!")
		print("Было загадано слово {}".format(word))	


hangman()