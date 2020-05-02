from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Role(Base):
    __tablename__ = 'roles'
    # Here we define columns for the table Roles.
    roleid = Column(Integer, primary_key=True)
    roletitle = Column(String(50), nullable=False)
    roledescription = Column(String(50))
    
    
    def __repr__(self):
        return "<Role(Title='%s', Description='%s')>" % (
            self.roletitle, self.roledescription)
    
class Department(Base):
    __tablename__ = 'departments'
    # Here we define columns for the table Departments.
    departmentid = Column(Integer, primary_key=True)
    departmenttitle = Column(String(50), nullable=False)
    departmentdescription = Column(String(50))
    
    
    def __repr__(self):
        return "<Department(Title='%s', Description='%s')>" % (
            self.departmenttitle, self.departmentdescription)

class LeaveType(Base):
    __tablename__ = 'leavetypes'
    # Here we define columns for the table Roles.
    leavetypeid = Column(Integer, primary_key=True)
    leavetypetitle = Column(String(50), nullable=False)
    leavetypedescription = Column(String(50))
    
    
    def __repr__(self):
        return "<LeaveType(Title='%s', Description='%s')>" % (
            self.leavetypetitle, self.leavetypedescription)
    
class Employee(Base):
    __tablename__ = 'employees'
    # Here we define columns for the table Employees.
    employeeid = Column(Integer, primary_key=True)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    mobilenumber = Column(String(20))
    emailaddress = Column(String(150), nullable=False)
    password = Column(String(100), nullable=False)
    address = Column(String(150))
    roleid = Column(Integer, ForeignKey('roles.roleid'))
    role = relationship(Role)
    departmentid = Column(Integer, ForeignKey('departments.departmentid'))
    department = relationship(Department)
    
    def __repr__(self):
        return "<Employee(FirstName='%s', LastName='%s', EmailAddress='%s', Role ='%s')>" % (
            self.firstname, self.lastname, self.emailaddress, self.role)
    
class Leave(Base):
    __tablename__ = 'leaves'
    # Here we define columns for the table Employees.
    leaveid = Column(Integer, primary_key=True)
    employeeid = Column(Integer, ForeignKey('employees.employeeid'))
    employee = relationship(Employee, foreign_keys=[employeeid])
    managerid = Column(Integer, ForeignKey('employees.employeeid'))
    manager = relationship(Employee, foreign_keys=[managerid])
    leavetypeid = Column(Integer, ForeignKey('leavetypes.leavetypeid'))
    leavetype = relationship(LeaveType)
    fromdate = Column(DateTime(timezone=True), default=func.now())
    todate = Column(DateTime(timezone=True), default=func.now())
    employeenotes = Column(String(500))
    managernotes = Column(String(500))
    status = Column(String(100), nullable=False)
    
    def __repr__(self):
        return "<Leave(FromDate='%s', ToDate='%s', Status='%s', Employee ='%s')>" % (
            self.fromdate, self.todate, self.emailaddress, self.employee)