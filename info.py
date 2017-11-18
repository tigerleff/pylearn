# user_info = dict()
# user_info = {'first_name' : 'Sergei' , 'last_name' : 'Sergei' }
# print(user_info) 
# print(user_info['first_name'])


# {} - словарь
# Primes = [2, 3, 5, 7, 11, 13] список 



# def get_summ(one, two, delimeter=' '):
# 	#str_one = 
#     return one.upper() + str(delimeter) + two.upper()


# one = 'jsdj'
# two = '2'
# print(get_summ(one, two))



def get_answer(question):
	answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
	question = str(question).lower()
	print(answers.get(question, "Я вас не понял"))

question = input("Говорите:")
get_answer(question)








