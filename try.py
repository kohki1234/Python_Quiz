def choose_difficulty ():
    # this function is used for users to choose the difficulty of the quiz. There are 3 types.

    while True:
		
		print """
		Please choose the difficulty of the Quiz!!, you can simlpy type the number beside the difficulty
		-----------------------------------------
		 0 - easy
		 1 - normal
		 2 - hard
		 -----------------------------------------
		"""
		user_input = raw_input("I want to challenge...: ")
		while user_input not in ['0','1','2']:
			print "Please enter the number from 0 to 2"
			user_input	= raw_input	()

		return user_input
        		

TEXT, ANSWERS = 0, 1 
# tuples level = (TEXT, ANSWERS)
easy = ("# If we use python, and put the code : print 5 + 5, then the answer will be __1__,\
    however, if we put the code : print '5' + '5', then it print out __2__.\
    For the first example, 5 is exact number 5. We call it as __3__,\
    For the second case, we treat the '5' not as a number, we call it __4__",
    ['10', '55', 'interger', 'string'])

medium	= ("There is string , Text = ' A GENTLEMAN took his suitcase.'\
    You want to print out only GENTLEMAN, you can use __1__ function to\
    search the first position of the word. The code will be __2__. (you don't have to put print) \
    Once you find the start position of the word, then you can specify \
    the end position of the word,  which will be __3__. \
    Finally you can write code to print out the word GENTLEMAN, which will be \
    __4__",
    ['find', "Text.find('GENTLEMAN')", '11', "print text[2:11]"])

hard = ("You have an existing list, which is list = [0,1,2,3].\
    If you write a line of code : print list[1], then it prints out __1__\
    Then if you add some numbers by : list = list + [4,5]. Then you write a code : print list[5]\
    It prints out __2__.\
    After that,You write a line of code :list.append([6,7]. Then you write a line of code : print list[6]\
    It prints out __3__.\
    If you put a line of code : print len(list), it prints out __4__",
    ['1', '2', '[6:7]', '7'])

game_data = {
	'0':{
		'text': easy[TEXT],
		'answers': easy[ANSWERS]
	},

	'1': {
		'text': medium[TEXT],
		'answers': medium[ANSWERS]
	},

	'2': {
		'text': hard[TEXT],
		'answers': hard[ANSWERS]
	}

}


def quiz():
	"""
	Args:

    level = choose_difficulty() : it calls choose difficulity function

	text = game_data[level]['text'] : it is text depending on the difficulity
	answer = game_data[level]['answers'] :it is answer depending on the difficulity
	attempts : max number which users can fail to put answer 
	number_of_correct_answer : Max number of correct answer for each quiz.

    Behavior:
    	Users need to put answer and function check if it is correct or not.

    Returns:
    	 correct answer 4 times : return 'you won!'
    	 Failed 3 times : return 'GAME OVER !'

	"""

	level = choose_difficulty()
	text = game_data[level]['text']
	answer = game_data[level]['answers']
	attempts = 3 # attempts means the number that user can answer the same quiz.
	user_score = 0 # This runs thuorgh the dictionary answers = game_data[level]['answers'].
		# if the user got correct answer, it will be increased.
		# = user_score

	number_of_correct_answer = 4 
	# This is the maximum number which users can have correct answer for 1 quiz

	while user_score < number_of_correct_answer:
		print text # print out the question whole text
		user_answer = raw_input("The answer for the __{blank}__".format(blank = user_score + 1))
       
		if user_answer == answer[user_score]:
			print 'Great !!the answer is correct!'
			text = text.replace(str(user_score + 1), answer[user_score])
			user_score = user_score + 1 

			if user_score == number_of_correct_answer:
				return 'You won!! You got evrey correct answers to this quiz!!' 

		else:
			print "Wrong !! Unfortunately your answer is incorrect...!"
			attempts = attempts - 1 

			if attempts == 0:
				return 'GAME OVER!!'

#TEST print out
#print choose_difficulty()
print quiz()