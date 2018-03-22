#
# This does not work right now. What I was going to have it do was look intot he question bank folder and parse out questions, then plug them into moodle using selenium
#

#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from os import listdir
from os.path import isfile, join
from os.path import isdir, join
# For passwords
import getpass
#For list selection in the terminal (https://github.com/wong2/pick)
from pick import pick
driver = webdriver.Firefox()
driver.get("https://jatc669.wccnet.edu/")
assert "JATC" in driver.title
# LOG IN
# SETS USERNAME
usernameInput = raw_input('Username: ')
username = driver.find_element_by_name('username')
username.clear()
username.send_keys(usernameInput)
# SETS PASSWORD
passwordInput = getpass.getpass('Password: ')
password = driver.find_element_by_name("password")
password.clear()
password.send_keys(passwordInput)
#CLICKS LOGIN BUTTON
driver.find_element_by_css_selector('#loginbtn').click()
# OPENS COURSES
driver.find_element_by_xpath('//span[text()="Site administration"]').click();

# CHOOSE CATEGORY TO ADD QUESTION BANK TO
courseCategorySection = driver.find_element_by_xpath('//div[@data-block="course_list"]')
courseCategory = courseCategorySection.find_elements_by_tag_name('a')
categoryList = []

# Get a list of all Categories
for x in range(len(courseCategory) - 1):
    categoryList.append(courseCategory[x].get_attribute('textContent'))

# Selects the course you want to add a bank to
courseTitle = 'Choose a Course Category: '
option, index = pick(categoryList, courseTitle)
driver.find_element_by_link_text(option).click()

# Clicks into a random course because you have to to get access to the bank options (for some reason...)
courseList = driver.find_element_by_class_name('coursename')
courseList.find_element_by_tag_name('a').click()

# Navs to the Categories Functionality
driver.find_element_by_link_text('Question bank').click()
driver.find_element_by_link_text('Categories').click()

### todo: 
### You should move the Bank selection here and put it into a function with a loop that
### 1. Counts the number of lessons in a folder
### 2. Creates a question category
### 3. Adds questions to each category
### 4. Repeats
###

# Looks into the Question Bank folder and opens a list of course Qustions Banks
allQuestionBanks = [f for f in listdir('question-banks') if isdir(join('question-banks', f))]
questionBankSelction = 'Choose a Question Bank: '
selectedBank, index = pick(allQuestionBanks, questionBankSelction)

banks = listdir('question-banks/' + selectedBank)

# for every text file in the question bank folder
for bank in banks:

    # If it is not a text file, ignore
    if bank == '.DS_Store':
        pass

    # if it is a text file...
    else:
        # Selects the "Top" placment in the default for the category
        top = driver.find_elements_by_xpath("//*[contains(text(), 'Top')]")
        top[1].click()
    
        # Removes the suffix of the file
        if bank.endswith('.txt'):
            bank = bank[:-4]

        # Parses the file into questions
        bankText  = open('question-banks/' + selectedBank + '/' + bank + '.txt', 'r')
        content = bankText.readlines() 
        content = [x.strip() for x in content]

        ## Loops over the txt file and sorts questions into a nested list
        questionList = []
        question = []
        for x in content:
            if x == '!!!':
                questionList.append(question)
                question = []
            else:
                question.append(x)
        # Creates the category with the bank name
        driver.find_element_by_id('id_name').send_keys(bank)
        driver.find_element_by_id('id_submitbutton').click()

        # Navs to the questions page
        driver.find_element_by_link_text("Questions").click()

        # Selects the correct pool to add questions to
        bankString = str(bank)
        select = Select(driver.find_element_by_id('id_selectacategory'))
        select.select_by_visible_text(bankString)

        ## todo: add the question adding for loop here
        for x in questionList:

            # Opens the Question Type Menu, selects Multiple Choice
            driver.find_element_by_xpath('/html/body/div[3]/div/section/div/div/div/div[1]/form/div/input[1]').click()
            driver.find_element_by_id('qtype_qtype_multichoice').click()
            driver.find_element_by_class_name('submitbutton').click()

            # Adds question name and description
            
            print 
            
            driver.find_element_by_id('id_name').send_keys(x[1])
            
            driver.find_element_by_class_name('atto_collapse_button').click()
            driver.find_element_by_class_name('atto_html_button').click()
            driver.find_element_by_id('id_questiontext').clear()
            driver.find_element_by_id('id_questiontext').send_keys('<p>' + x[1] + '</p>')


            driver.find_element_by_id('id_answer_0editable').send_keys(x[2])
            answerSelect = Select(driver.find_element_by_id('id_fraction_0'))
            answerSelect.select_by_value('1.0')
            driver.find_element_by_id('id_answer_1editable').send_keys(x[3])
            answerSelect = Select(driver.find_element_by_id('id_fraction_1'))
            answerSelect.select_by_value('0.0')
            driver.find_element_by_id('id_answer_2editable').send_keys(x[4])
            answerSelect = Select(driver.find_element_by_id('id_fraction_2'))
            answerSelect.select_by_value('0.0')
            driver.find_element_by_id('id_answer_3editable').send_keys(x[5])
            answerSelect = Select(driver.find_element_by_id('id_fraction_2'))
            answerSelect.select_by_value('0.0')

            driver.find_element_by_id('id_submitbutton').click()
        # Navs back tot he Category page
        driver.find_element_by_link_text("Categories").click()
            
print "!!! Question banks have been built !!!"        

assert "No results found." not in driver.page_source
#driver.close()