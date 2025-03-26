# Beginning: create variables #
smarter_8 = 0
not_smarter = 0

# Middle: Ask question

print("Are you smarter than an 8th grader? Whatever answer you think it is, put the corresponding letter for the following questions:")
answer = input('True or false: The pacific ocean has salt water. A) True, or B) False   ')
if answer == "A" :
    smarter_8 += 1
elif answer == "B" :
    not_smarter += 1

answer = input('True or false: The mitochondria is the power house of the cell. A) True, or B) False   ')
if answer == "A" :
    smarter_8 += 1
elif answer == "B" :
    not_smarter += 1


answer = input('True or false: George Washington wrote the declaration of independence. A) True, or B) False   ')
if answer == "A" :
    not_smarter += 1
elif answer == "B" :
    smarter_8 += 1

answer = input('True or false: France gifted the Statue of Liberty to America as a birthday gift. A) True, or B) False   ')
if answer == "A" :
    smarter_8 += 1
elif answer == "B" :
    not_smarter += 1
 

answer = input('True or false: Scientists are trying to bring Wolly Mammoths back to life. A) True, or B) False   ')
if answer == "A" :
    smarter_8 += 1
elif answer == "B" :
    not_smarter += 1

# End of quiz #

if smarter_8 > not_smarter :
    print(" You are smarter than a 8th Grader!")
elif not_smarter > smarter_8 :
    print( " You are not smarter than an 8th grader..")