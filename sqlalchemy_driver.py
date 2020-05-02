from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from sqlalchemy_declarative import Employee, Base, Role
 

# Create an engine that stores data in the local directory's
engine = create_engine('sqlite:///leavemanagment.db')
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
 
 
 # Insert a Role in the Roles table
session.add_all([
   Role(roletitle = 'Manager', roledescription = 'Manager'), 
   Role(roletitle = 'Developer', roledescription = 'Developer')]
)

session.commit()

# Insert a Department in the departments table
new_departments = Department(departmenttitle='IT', departmentdescription = 'IT')
session.add(new_leavetype)
session.commit()

# Insert a LeaveType in the LeaveTypes table
new_leavetype = LeaveType(leavetypetitle='Casual', leavetypedescription = 'Casual')
session.add(new_leavetype)
session.commit()
 
# Insert a manager in the Employees table
manager = session.query(Role).filter(Role.roletitle == 'Manager').first()
new_employee = Employee(firstname='Ryan', lastname='Gordy', mobilenumber='(916) 111-1111', address='', emailaddress='Ryan.Gordy@live.maryville.edu', password='manager', role=manager, department=new_deaprtment)
session.add(new_employee)
session.commit()


# Insert an Employee in the Employees table
developer = session.query(Role).filter(Role.roletitle == 'Developer').first()
new_employee = Employee(firstname='Malli', lastname='Nookala', mobilenumber='(916) 222-2222', address='', emailaddress='mnookala1@live.maryville.edu', password='123456', role=developer, department=new_deaprtment)
session.add(new_employee)
session.commit()


for employee in session.query(Employee).all():
    print(employee)
    
# Insert a leave in the Leaves table
manager = session.query(Employee).filter(Employee.FirstName == 'Ryan').first()
new_leave = Leave(employee=new_employee, manager=manager, leavetype=new_leavetype, fromdate='2020-05-02', todate='2020-05-08', employeenotes='Need a week leave for vacation', managernotes='', status='Pending')
session.add(new_leave)
session.commit()

for leave in session.query(Leave).all():
    print(leave)

