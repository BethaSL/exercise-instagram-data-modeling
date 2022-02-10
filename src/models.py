import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User (Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(220), nullable=False)
    user_id = Column(String(200), nullable=False)
    password = Column(String(10), nullable=False)

    post= relationship("Post", back_populates="parent")
    followers= relationship("Followers", back_populates="parent")
    following= relationship("Following", back_populates="parent")

class Post (Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    likes = Column(Integer, nullable=False)
    comments = Column(String(140))
    user_id= Column(Integer, ForeignKey("user.id"))

    user= relationship("User", back_populates="children")


class Followers (Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    follower_id = Column(String(200), nullable=False)
    user_id= Column(Integer, ForeignKey("user.id"))

    user= relationship("User", back_populates="children")

class Following (Base):
    __tablename__ = 'following'
    id = Column(Integer, primary_key=True)
    follower_id = Column(String(200), nullable=False)
    user_id= Column(Integer, ForeignKey("user.id"))

    user= relationship("User", back_populates="children")

    def to_dict(self):
       return {}

  




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')