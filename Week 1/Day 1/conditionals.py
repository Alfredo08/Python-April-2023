
exam_grade_alex = 8.2
exam_grade_martha = 9.4

if exam_grade_alex >= 8.0:
    print( "Alex passed the exam" )

if exam_grade_martha >= 8.0:
    print( "Martha passed the exam" )
else:
    if exam_grade_martha >= 7.0:
        print( "Martha needs a retake, but she was really close on passing" )

if exam_grade_alex >= 8.0 and exam_grade_martha >= 8.0:
    print( "Both students passed!" )