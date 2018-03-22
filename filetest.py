from os import listdir
from os.path import isfile, join
from pick import pick

allQuestionBanks = [f for f in listdir('question-banks') if isfile(join('question-banks', f))]

questionBankSelction = 'Choose a Question Bank: '
option, index = pick(allQuestionBanks, questionBankSelction)
