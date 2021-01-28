import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

follower = Table("follower", Base.Model.metadata,
    Column("id_follower", Integer, ForeignKey("user.id"), primary_key=True),
    Column("id_followed", Integer, ForeignKey("user.id"), primary_key=True)
)

class User(Base.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    firstname = Column(String(80), nullable=False)
    lastname = Column(String(100), nullable=True)
    email = Column(String(70), nullable=False)

class Post(Base.Model):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))

class Comment(Base.Model):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))
    comment_text = Column(Text(), nullable=False)

class Media(Base.Model):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("post.id"))
    media_type = Column(Enum("post","story","reel"))
    url = Column(String, nullable=False)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')