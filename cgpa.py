
# to calculate gp in most if not nigerian schools that i'm presently aware of, you get the cummulative point gotten by the student and divide by the cummulative credit load of all the courses


no = 1
yes = 2

# create an empty list to store the gps()
gps = []

# create the main gp calculation function 
def maincalc():
  courseamount = int(input('''how many courses do you offer:'''))

  def course_score_input():
      courses_point = dict()
      creditload = []
      # keep asking input from the user till the number of courses he inputed is met 
      for i in range(courseamount):
        point = 0
        print(str(i)+ ' course(s) inputed')
        course = input('''please enter your course: ''')
        score = int(input('''please enter your score: '''))  
        for v in range(i in range(courseamount)):
          cl = int(input('creditload: '))
          creditload.append(cl)

          # defining points gotten for all score ranges
          # a: 1 cuv
          if cl == 1 and score >= 70 and score <=100:
            point = 5
          # a: 2 cuv
          elif cl == 2 and score >= 70 and score <=100:
            point = 10
          # a: 3 cuv
          elif cl == 3 and score >= 70 and score <=100:
            point = 15


          # b: 1 cuv
          elif cl == 1 and score >= 60 and score <=69:
            point = 4
          # b: 2 cuv
          elif cl == 2 and score >= 60 and score <=69:
            point = 8
          # b: 3 cuv
          elif cl == 3 and score >= 60 and score <=69:
            point = 12         


          # c: 1 cuv
          elif cl == 1 and score >= 50 and score <=59:
            point = 3
          # c: 2 cuv
          elif cl == 2 and score >= 50 and score <=59:
            point = 6
          # c: 3 cuv
          elif cl == 3 and score >= 50 and score <=59:
            point = 9


          # d: 1 cuv
          elif cl == 1 and score >= 40 and score <=45:
            point = 2
          # d: 2 cuv
          elif cl == 2 and score >= 40 and score <=45:
            point = 4
          # d: 3 cuv
          elif cl == 3 and score >= 40 and score <=45:
            score = 6


          # f: 1 cuv
          elif cl == 1 and score >= 1 and score <=44:
            point = 1
          # f: 2 cuv
          elif cl == 2 and score >= 1 and score <=44:
            point = 2
          # f: 3 cuv
          elif cl == 3 and score >= 1 and score <=44:
            point = 3

          # 0 
          elif cl == 1 and score == 0:
            point = 0
          elif cl == 2 and score == 0:
            point = 0
          elif cl == 3 and score == 0:
            point = 0
          else:
            print('invalid grade details, please start all over')
            course_score_input()
        # assigning the point to the course
        courses_point[course]=point
      #summing up credit loads for calculation 
      totalCreditLoad = sum(creditload)

      #summing up student's points for calculation 
      userTotalPoints = sum(courses_point.values())
        
      # getting students the gp 
      gPA =  userTotalPoints/totalCreditLoad
      rgpa = round(gPA, 2)
      n = len(gps)+1
      sumgps = sum(gps)
      cgpa = (sumgps + gPA)/n 
      rcgpa = round(cgpa, 2)
      
      print('Total credit unit value: '+ str(userTotalPoints))
      print('Total credit load: '+ str(totalCreditLoad)) 
      print('GPA: ' + str(rgpa) ) 
      print(r'Total\Cummulative GPA: ' +str(rcgpa))
  course_score_input()

# incase user has previous gps to calculate
def previousR():
  amountpgp = int(input('how many gp do you want to  calculate: '))
  
  for i in range(amountpgp):
    previousGP = float(input('what is|are your previous GP(s): '))
    gps.append(previousGP)

# checking if user is a new student to know if to ask them for previous gp scores
def studentstatusFunc():
  studentstatus = int(input('''
Are you a new student
1. yes
2. no
'''))
  if studentstatus == 2:
    def askextragp():
      extragp = int(input('Do you want to plan with your previous GPA(s)\n1. yes\n2. no\n'))
      if extragp == 1:
        previousR()
        maincalc()
      elif extragp == 2:
        maincalc()  
      else:
        print('invalid choice, please select a valid option\n')
        askextragp()
    askextragp()
  elif studentstatus == 1:
      maincalc()
  else:
      print('''
invalid selection!!! please select a number in the range of choices''')
      studentstatusFunc() 
studentstatusFunc() 
           
     
     
     
     