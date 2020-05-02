from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy_declarative import Employee, Base, Role, Department, LeaveType, Leave
 

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
new_department = Department(departmenttitle='IT', departmentdescription = 'IT')
session.add(new_department)
session.commit()

# Insert a LeaveType in the LeaveTypes table
new_leavetype = LeaveType(leavetypetitle='Casual', leavetypedescription = 'Casual')
session.add(new_leavetype)
session.commit()
 
# Insert a records in the Employees table
manager = session.query(Role).filter(Role.roletitle == 'Manager').first()
developer = session.query(Role).filter(Role.roletitle == 'Developer').first()

session.add_all([
   Employee(firstname='Ryan', lastname='Gordy', mobilenumber='(916) 111-1111', address='', emailaddress='Ryan.Gordy@live.maryville.edu', password='manager', role=manager, department=new_department),
   Employee(firstname='Malli', lastname='Nookala', mobilenumber='(916) 222-2222', address='', emailaddress='mnookala1@live.maryville.edu', password='123456', role=developer, department=new_department)]
)
session.commit()


for employee in session.query(Employee).all():
    print(employee)
    
# Insert a leave in the Leaves table
manager = session.query(Employee).filter(Employee.firstname == 'Ryan').first()
employee = session.query(Employee).filter(Employee.firstname == 'Malli').first()
new_leave = Leave(employee=employee, manager=manager, leavetype=new_leavetype, fromdate= datetime(2012, 5, 2, 0, 0, 0), todate=datetime(2012, 3, 13, 0, 0, 0), employeenotes='Need a week leave for vacation', managernotes='', status='Pending')
session.add(new_leave)
session.commit()

new_leave.status = 'Rejected'
new_leave.managernotes = 'I can''t give 12 days leave.'
session.commit()

new_leave = Leave(employee=employee, manager=manager, leavetype=new_leavetype, fromdate= datetime(2020, 5, 2, 0, 0, 0), todate=datetime(2020, 5, 8, 0, 0, 0), employeenotes='Need a week leave for vacation', managernotes='', status='Pending')
session.add(new_leave)
session.commit()

new_leave.status = 'Approved'
new_leave.managernotes = 'Enjoy the vacation.'
session.commit()

for leave in session.query(Leave).all():
    print(leave)


