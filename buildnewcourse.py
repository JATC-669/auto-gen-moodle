#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

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
print "Logging in..."

#CLICKS LOGIN BUTTON
driver.find_element_by_css_selector('#loginbtn').click()

# OPENS COURSES
###### driver.find_element_by_xpath('//span[text()="Site administration"]').click();

# WAITS THEN CLICKS COURSES
###### driver.implicitly_wait(2) # seconds
###### driver.find_element_by_xpath('//span[text()="Courses"]').click()

# WAITS THEN OPENS MANAGE COURSE AND CATEGORIES
###### driver.implicitly_wait(2) # seconds
###### driver.find_element_by_xpath('//span[text()="Manage courses and categories"]').click()

# CHOOSE CATEGORY TO ADD COURSE TO
# CHRIS - FIX THIS TO AUTO GEN THE LIST


##### OLD WORKING CODE
##### courseTitle = 'Choose a Course Category: '
##### courseCategory = ['SPF 01: Job Safety and Health','SPF 02: Your Heritage and Future in the Pipe Trades','SPF 03: The Use and Care of Tools','SPF 04: Basic Drawing for the Sprinkler Fitter','SPF 05: Introduction to Automatic Sprinklers','SPF 06: Reading Automatic Sprinkler Piping Drawings','SPF 07: Math for the Sprinkler Fitter','SPF 08: Installation of Sprinkler Systems ','SPF 09: The Automatic Sprinkler','SPF 10: Architectural Working Drawings for Sprinkler Fitters','SPF 11: Blueprint Reading for the Sprinkler Fitter','SPF 12: Sprinkler System Water Supply','SPF 13: Types of Fire Protection Systems','SPF 14: Special Application Sprinkler Systems','SPF 15: Hydraulics for the Sprinkler Apprentice','SPF 16: Sprinkler System Alarms','SPF 17: Economics of the Sprinkler Industry','SPF 18: Human Relations','SPF 19: Technical Reports','SPR 01: Job Safety and Health for Residential Sprinkler Installers','SPR 02: Your Heritage and Future in the Residential Pipe Trades','SPR 03: Use and Care of Tools in the Residential Pipe Trades','SPR 04: Reading Blueprints','SPR 05: Math for the Residential Sprinkler Fitter','SPR 06: Installation of Residential Sprinkler Systems','SPR 07: The Automatic Sprinkler for the Residential Helper','CHRIS 01: How to Make Moodle Work',]
##### option, index = pick(courseCategory, courseTitle)

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

# SELECTS THE CHOSEN CATEGORY AND CLICKS CREATE A NEW COURSE
driver.find_element_by_link_text(option).click()
driver.implicitly_wait(2) # seconds
driver.find_element_by_xpath("//input[@value='Add a new course']").click()

# POPULATES THE NEW COURSE FULL NAME
versionInput = raw_input('What version (e.x. A, B, C, D ...) is this new course? ')
courseFullname = driver.find_element_by_id("id_fullname")
courseFullname.clear()

# POPULATES THE NEW COURSE SHORT NAME
new_name = option.split()
cleanCourseNumber = str(new_name[1][:-1])
newShortname =  str(new_name[0] + cleanCourseNumber)
revisionInput = raw_input('What revision (e.x. 01, 02, 03 ...) is this new course? ')
courseShortname = driver.find_element_by_id("id_shortname")
courseShortname.clear()
courseShortname.send_keys(newShortname + versionInput + revisionInput)
courseFullname.send_keys(option + ' - ' + versionInput + ' - Rev: ' + revisionInput)
courseIdNumber = driver.find_element_by_id('id_idnumber')
courseIdNumber.clear()
courseIdNumber.send_keys(newShortname + versionInput + revisionInput)

# OPENS AND POPULATES THE COURSE DESCRIPTION
driver.find_element_by_class_name('atto_collapse_button').click()
driver.find_element_by_xpath("//button[@title='HTML']").click()

# PROMPTS FOR THE NUMBER OF LESSONS IN THE COURSE
lessonNumberInput = raw_input('How many lessons are in this course? ')
lessonNumberCourseDescriptionOutput = str('<p>' + lessonNumberInput + ' Online Lessons + Final Exam</p>')

# POPULATES THE COURSE DESCRIPTION BASED ON THE INDEX OF THE CATEGORY NUMBER
spf01Description = '<p>Placeholder Description</p>'
spf02Description = '<p>Placeholder Description</p>'
spf03Description = '<p>Placeholder Description</p>'
spf04Description = '<p>Placeholder Description</p>'
spf05Description = '<p>Placeholder Description</p>'
spf06Description = '<p>Placeholder Description</p>'
spf07Description = '<p>This two-part course reviews basic mathematical concepts (Lessons 1-7) as well as applied mathematics in the sprinkler fitter trade with a focus on the use of a calculator in solving problems (Lessons 9-17). It also includes a midterm exam (Lesson 8) that must be passed (> 60 percent) before submitting the remainder of your lessons. A calculator will be provided to you.</p>'
spf08Description = '<p>Placeholder Description</p>'
spf09Description = '<p>Placeholder Description</p>'
spf10Description = '<p>Placeholder Description</p>'
spf11Description = '<p>Placeholder Description</p>'
spf12Description = '<p>Placeholder Description</p>'
spf13Description = '<p>Placeholder Description</p>'
spf14Description = '<p>Placeholder Description</p>'
spf14Description = '<p>Placeholder Description</p>'
spf15Description = '<p>Placeholder Description</p>'
spf16Description = '<p>Placeholder Description</p>'
spf17Description = '<p>Placeholder Description</p>'
spf18Description = '<p>Placeholder Description</p>'
spf19Description = '<p>Placeholder Description</p>'
spr01Description = '<p>Placeholder Description</p>'
spr02Description = '<p>Placeholder Description</p>'
spr03Description = '<p>Placeholder Description</p>'
spr04Description = '<p>Placeholder Description</p>'
spr05Description = '<p>Placeholder Description</p>'
spr06Description = '<p>Placeholder Description</p>'
spr07Description = '<p>This two-part course reviews basic mathematical concepts (Lessons 1-7) as well as applied mathematics in the sprinkler fitter trade with a focus on the use of a calculator in solving problems (Lessons 9-17). It also includes a midterm exam (Lesson 8) that must be passed (> 60 percent) before submitting the remainder of your lessons. A calculator will be provided to you.</p>'
chris01Description = '<p>Wow cool description</p>'

courseDescriptions = [spf01Description, spf02Description, spf03Description, spf04Description, spf05Description, spf06Description, spf07Description, spf08Description, spf09Description, spf10Description, spf11Description, spf12Description, spf13Description, spf14Description, spf14Description, spf15Description, spf16Description, spf17Description, spf18Description, spf19Description, spr01Description, spr02Description, spr03Description, spr04Description, spr05Description, spr06Description, spr07Description, chris01Description]
courseDescription = driver.find_element_by_id('id_summary_editor')
courseDescription.clear()
courseDescription.send_keys(lessonNumberCourseDescriptionOutput + courseDescriptions[index + 1] + '<p><strong>Attention: There may have been minor editing changes to the questions found in your study guide.  Always answer questions as they appear online, not what is in your book.</strong></p>')

# SETS THE NUMBER OF TOPICS IN THE COURSE FORMAT TO THE NUMBER OF LESSONS PLUS ONE FOR THE FINAL
driver.find_element_by_link_text('Course format').click()
selectNumberOfSections = Select(driver.find_element_by_name('numsections'))
selectNumberOfSections.select_by_index(str(int(lessonNumberInput) + 1))

# CLICKS ON SAVE AND DISPLAY AND CREATES THE COURSE
driver.find_element_by_name('saveanddisplay').click()

# NAVS AWAY FROM THE ENROLL PAGE AND TO THE COURSE
driver.find_element_by_xpath("//a[@title='"+ option + ' - ' + versionInput + ' - Rev: ' + revisionInput + "']").click()
driver.implicitly_wait(10) # seconds

#TURNS EDITING ON
driver.find_element_by_xpath("//input[@value='Turn editing on']").click()

### FUTURE: Add a list of everyone that needs to be enrolled in the course here.abs
# OPENS MAIN TOPIC SECTION EDITING
driver.implicitly_wait(2) # seconds
courseSectionTitle = driver.find_element_by_xpath("//li[@id='section-0']")
courseSectionTitle.find_element_by_xpath(".//a[@class='toggle-display textmenu']").click()
driver.find_element_by_xpath("//a[@title='Edit section']").click()

# ADDS NAME AND DESCRIPTION TO THE TOPIC BLOCK
#Populates the Section Name
driver.implicitly_wait(3) # seconds
driver.find_element_by_id("id_usedefaultname").click()
courseTopicName = driver.find_element_by_id("id_name")
courseTopicName.clear()
courseTopicName.send_keys(option)

#Populates the Section Summary
courseTopicName = driver.find_element_by_id("id_summary_editoreditable")
courseTopicName.clear()
driver.find_element_by_class_name('atto_collapse_button').click()
driver.find_element_by_class_name('atto_html_button').click()
courseTopicName = driver.find_element_by_id("id_summary_editor")
courseTopicName.send_keys(lessonNumberCourseDescriptionOutput + courseDescriptions[index + 1] + '<p><strong>NOTE: There may have been minor editing changes to the questions found in your study guide.  Always answer questions as they appear online, not what is in your book.</strong></p>')
driver.find_element_by_id("id_submitbutton").click()



# Loops through #of Topics and Adds Blank Quizzes to the Lessons Topics
for x in range(int(lessonNumberInput)):

    # Quiz Options go here
    lessonTopic = driver.find_element_by_id('section' + str(x+1))
    quizSelect = Select(lessonTopic.find_element_by_tag_name('select'))

    # Opens the Add Quiz Function
    quizSelect.select_by_visible_text("Quiz")
    quizName = driver.find_element_by_id('id_name').send_keys("Lesson " + str(x+1) + " Quiz")

    # Sets the review options
    quizReviewOptions = driver.find_element_by_id('id_reviewoptionshdr')
    quizReviewOptions.find_element_by_tag_name('a').click()
    driver.find_element_by_id('id_rightanswerimmediately').click()
    driver.find_element_by_id('id_correctnessopen').click()
    # REMOVED TO SHOW GRADE TO STUDENT: driver.find_element_by_id('id_marksopen').click()
    driver.find_element_by_id('id_specificfeedbackopen').click()
    driver.find_element_by_id('id_generalfeedbackopen').click()
    driver.find_element_by_id('id_rightansweropen').click()
    driver.find_element_by_id('id_overallfeedbackopen').click()
    driver.find_element_by_id('id_attemptopen').click()
    driver.find_element_by_id('id_correctnessclosed').click()
    # REMOVED TO SHOW GRADE TO STUDENT: driver.find_element_by_id('id_marksclosed').click()
    driver.find_element_by_id('id_specificfeedbackclosed').click()
    driver.find_element_by_id('id_generalfeedbackclosed').click()
    driver.find_element_by_id('id_rightanswerclosed').click()
    driver.find_element_by_id('id_overallfeedbackclosed').click()
    driver.find_element_by_id('id_attemptclosed').click()

    # Sets Extra restrictions on Attempts
    quizIdSecurity = driver.find_element_by_id('id_security')
    quizIdSecurity.find_element_by_tag_name('a').click()

    ## Sets a day delay in the first attempt
    driver.find_element_by_id('id_delay1_enabled').click()
    driver.find_element_by_id('id_delay1_number').clear()
    driver.find_element_by_id('id_delay1_number').send_keys('1')
    retakeDelay1Time = Select(driver.find_element_by_id('id_delay1_timeunit'))
    retakeDelay1Time.select_by_visible_text("days")

    ## Sets a day delay in the other attempts
    driver.find_element_by_id('id_delay2_enabled').click()
    driver.find_element_by_id('id_delay2_number').clear()
    driver.find_element_by_id('id_delay2_number').send_keys('1')
    retakeDelay2Time = Select(driver.find_element_by_id('id_delay2_timeunit'))
    retakeDelay2Time.select_by_visible_text("days")

    # Sets requirment for student to have a grade before lesson is complete
    quizCompleationSection = driver.find_element_by_id('id_activitycompletionheader')
    quizCompleationSection.find_element_by_tag_name('a').click()
    compleationTracking = Select(driver.find_element_by_id('id_completion'))
    compleationTracking.select_by_index(2)
    driver.find_element_by_id('id_completionusegrade').click()

    # Saves Quiz
    driver.find_element_by_id('id_submitbutton2').click()

# Creates Final Exam
finalTopic = driver.find_element_by_id('section' + str(int(lessonNumberInput) + 1))
finalSelect = Select(finalTopic.find_element_by_tag_name('select'))
finalSelect.select_by_visible_text("Quiz")
finalName = driver.find_element_by_id('id_name').send_keys("FINAL EXAM GRADE")


# Adds password instructions ot the final exam description
driver.find_element_by_class_name('atto_collapse_button').click() # opens extra editing options
driver.find_element_by_class_name('atto_html_button').click() # enables html input

passwordHTMLtext = '<p><strong>This final is password protected</strong>. To receive a password, complete the form below. The current password will be emailed to your <a href="https://gateway.wccnet.edu/gateway/base/index.html">WCC Student Email address</a>. After you receive the password, click the <code style="color: #0f75bc; border: 3px solid #0f75bc; font-family: "Roboto", sans-serif; font-weight: bold;">ATTEMPT QUIZ NOW</code> button and enter the password.</p><ul> <li><strong>Finals must be completed by the apprentice requesting the final</strong>, under penalty of expulsion from the program.</li><li><strong>Apprentices that attend formal classes are required to take finals with their Instructor</strong>. Do not attempt a final outside of class unless you are authorized, under penalty of expulsion from the program.</li><li>Passwords are valid until midnight on the day they are requested. <strong>You may request additional passwords if you need to</strong>.</li></ul><form action="" id="passwordForm" style="border: 1px solid #ccc; padding: 1em; border-radius: .3em;"> <h2>Request a Password</h2> <label for=""><strong>Enter Your WCC Email Address</strong><br><input id="apprenEmail" placeholder="you@wccnet.edu" type="text"> </label> <label for=""><strong>Do you attend formal classes with an instructor?</strong><br><select name="" id="independentInd"> <option disabled="disabled" selected="selected">Choose one...</option> <option value="0">Yes, I attend classes with an instructor.</option> <option value="1">No, I am not required to attend classes.</option> </select> </label><br><button type="button" value="GET PASSWORD" onclick="getPasswords()">GET PASSWORD</button></form>'

driver.find_element_by_id('id_introeditor').send_keys(passwordHTMLtext)

# Sets the time limit for the final exam
quizTimingOptions = driver.find_element_by_id('id_timing')
quizTimingOptions.find_element_by_tag_name('a').click()
driver.find_element_by_id('id_timelimit_enabled').click() # Enables a time limit
driver.find_element_by_id('id_timelimit_number').send_keys("3") # Sets hour number
timingTimeUnitSelect = Select(driver.find_element_by_id('id_timelimit_timeunit'))
timingTimeUnitSelect.select_by_visible_text("hours")

# Sets final submissions to submit if timer runs out
timingTimeEpSubmissionOption = Select(driver.find_element_by_id('id_overduehandling'))
timingTimeEpSubmissionOption.select_by_visible_text("Open attempts are submitted automatically")

# Sets final attempt ammout to 1
quizGradingOptions = driver.find_element_by_id('id_modstandardgrade')
quizGradingOptions.find_element_by_tag_name('a').click()
sys.exit("Halted. Caught fire.")

# Sets the review options
quizReviewOptions = driver.find_element_by_id('id_reviewoptionshdr')
quizReviewOptions.find_element_by_tag_name('a').click()
driver.find_element_by_id('id_rightanswerimmediately').click()
driver.find_element_by_id('id_correctnessopen').click()
driver.find_element_by_id('id_marksopen').click()
driver.find_element_by_id('id_specificfeedbackopen').click()
driver.find_element_by_id('id_generalfeedbackopen').click()
driver.find_element_by_id('id_rightansweropen').click()
driver.find_element_by_id('id_overallfeedbackopen').click()
driver.find_element_by_id('id_attemptopen').click()
driver.find_element_by_id('id_correctnessclosed').click()
driver.find_element_by_id('id_marksclosed').click()
driver.find_element_by_id('id_specificfeedbackclosed').click()
driver.find_element_by_id('id_generalfeedbackclosed').click()
driver.find_element_by_id('id_rightanswerclosed').click()
driver.find_element_by_id('id_overallfeedbackclosed').click()
driver.find_element_by_id('id_attemptclosed').click()

# Sets Extra restrictions on Attempts
quizIdSecurity = driver.find_element_by_id('id_security')
quizIdSecurity.find_element_by_tag_name('a').click()
driver.find_element_by_id('id_quizpassword').send_keys("thisisthepassword")


# Sets a day delay in the first attempt
# driver.find_element_by_id('id_delay1_enabled').click()
# driver.find_element_by_id('id_delay1_number').clear()
# driver.find_element_by_id('id_delay1_number').send_keys('1')
# retakeDelay1Time = Select(driver.find_element_by_id('id_delay1_timeunit'))
# retakeDelay1Time.select_by_visible_text("days")
# Sets a day delay in the other attempts
# driver.find_element_by_id('id_delay2_enabled').click()
# driver.find_element_by_id('id_delay2_number').clear()
# driver.find_element_by_id('id_delay2_number').send_keys('1')
# retakeDelay2Time = Select(driver.find_element_by_id('id_delay2_timeunit'))
#retakeDelay2Time.select_by_visible_text("days")

# Sets Restrict Access
## Opens the Header
quizIdSecurity = driver.find_element_by_id('id_availabilityconditionsheader')
quizIdSecurity.find_element_by_tag_name('a').click()

# Add conditions for Lesson compleation.
for x in range(int(lessonNumberInput)):
    driver.find_element_by_class_name('availability-button').click()
    availButton = driver.find_element_by_class_name('availability-button')
    availButton.find_element_by_tag_name('button').click()
    driver.find_element_by_id('availability_addrestriction_completion').click()
    lessonQuiz = Select(driver.find_elements_by_name('cm')[x])
    lessonQuiz.select_by_index(x+1)

# Adds condition for 60% average on all lessons
driver.find_element_by_class_name('availability-button').click()
availButton = driver.find_element_by_class_name('availability-button')
availButton.find_element_by_tag_name('button').click()
driver.find_element_by_id('availability_addrestriction_grade').click()
finalRestriction = Select(driver.find_element_by_name('id'))
finalRestriction.select_by_index(1)
driver.find_element_by_name('min').click()
driver.find_element_by_name('minval').send_keys('60.00')

# Sets requirment for student to have a grade before lesson is complete
quizCompleationSection = driver.find_element_by_id('id_activitycompletionheader')
quizCompleationSection.find_element_by_tag_name('a').click()
compleationTracking = Select(driver.find_element_by_id('id_completion'))
compleationTracking.select_by_index(2)
driver.find_element_by_id('id_completionusegrade').click()

# Saves 
driver.find_element_by_id('id_submitbutton2').click()
print "Your course is built."
assert "No results found." not in driver.page_source
#driver.close()