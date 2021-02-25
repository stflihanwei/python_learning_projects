from survey import AnonymousSurvey

# define a question, and make a survey

question = "What language do you want to speak?"
my_survey = AnonymousSurvey(question)

# show the question, and store responses to the question.
my_survey.show_question()
print("enter 'q' at any time to quit.\n")
while True:
    response = input('Language: ')
    if response == 'q':
        break
    my_survey.store_response(response)

#Show the survey results.
print ('\n Thank you for participating.')
my_survey.show_results()
