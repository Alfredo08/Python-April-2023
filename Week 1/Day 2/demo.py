class Stack:
    def __init__( self, name, grade ):
        self.name = name
        self.grade = grade
    
    def print_info( self ):
        print( f"Stack: {self.name} Grade: {self.grade}" )

class Student:
    list_of_students = []

    def __init__( self, first_name, last_name, id, current_stack ):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.current_stack = current_stack
        Student.list_of_students.append( self )
    
    def print_student_info( self ):
        print( f"First name: {self.first_name} Last name: {self.last_name} Id: {self.id}" )
        self.current_stack.print_info()
    
    @classmethod
    def print_all_students( cls ):
        for student in cls.list_of_students:
            student.print_student_info()    
    
    @classmethod
    def find_student_by_id( cls, id ):
        for student in cls.list_of_students:
            if student.id == id:
                student.print_student_info()
                return student
        print( f"The student with id: {id} is not yet in our list!" )
    
    @staticmethod
    def generate_average_of_all_students( student_list ):
        sum = 0.0
        for student in student_list:
            sum += student.current_stack.grade
        return sum / len( student_list )

alex_python = Stack( "Python", 8.6 )
martha_java = Stack( "Java", 9.4 )
roger_python = Stack( "Python", 10.0 )
julie_mern = Stack( "MERN", 7.2 )

alex = Student( "Alex", "Miller", 12345, alex_python )
martha = Student( "Martha", "Smith", 67890, martha_java )
roger = Student( "Roger", "Anderson", 55555, roger_python )
julie = Student( "Julie", "Winston", 12121, julie_mern )

# Student.print_all_students()
# Student.find_student_by_id( 55556 )

print( Student.generate_average_of_all_students( Student.list_of_students ) )

