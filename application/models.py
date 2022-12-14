from .database import Base
from sqlalchemy import Column, String, ForeignKey, Integer


class Admin(Base):
    __tablename__ = "admin"
    
    login = Column(String(30), primary_key=True, nullable=False, unique=True)
    password = Column(String(100), nullable=False)


class Bank(Base):
    __tablename__ = "bank"
    
    acronym = Column(String(10), primary_key=True, nullable=False, unique=True)
    name = Column(String(100), nullable=False)
    money = Column(Integer, default=10000000)  # 10 000 000 CFA 
    
    
class User(Base):
    __tablename__ = "user"
    
    username = Column(String(30), primary_key=True, nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    money = Column(Integer, default=0)  # 0 FCFA
    bank = Column(String(10), ForeignKey("bank.acronym", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)

