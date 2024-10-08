import datetime
import random
capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne"
}
time_limit=90
for quiznum in range(2):
    quizfile=open('capitalquiz%s.txt' % (quiznum + 1), 'w')
    answerfile= open('quiz.txt')

    time= datetime.datetime.now()
    start_time=time.strftime('%H:%M')
    end_time=time + datetime.timedelta(minutes=time_limit)
    period_time=end_time.strftime('%H:%M')
    quizfile.write(f"Name:\nTime:{start_time}\nPeriod:{period_time}\n")
    states=list(capitals.keys())
    
    for questionnum in range(50):
        random.shuffle(states)
        correct_answer=capitals[states[quiznum]]
        wrong_answer=list(capitals.values())
        del wrong_answer[wrong_answer.index(correct_answer)]
        wrong_answer=random.sample(wrong_answer,3)
        answeroption= wrong_answer+[correct_answer]
        random.shuffle(answeroption)
        letters= ['a','b','c','d']
        quizfile.write('%d what is the capital of %s?\n'% (questionnum , states[questionnum]))
        for i,option in enumerate(answeroption):
            quizfile.write(f'{letters[i]}.{option}\n')
    quizfile.close()
    answerfile.close()        