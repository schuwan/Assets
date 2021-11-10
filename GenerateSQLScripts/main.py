from faker import Faker
from numpy.random import choice
import random as r
import bcrypt

from entities import Entity
from entities import BranchLocation
from entities import Gender
from entities import User
from entities import Post
from entities import PostComment
from entities import UserLike


fake = Faker();


'''
Create the in-house variables for branches
'''
branch1 = BranchLocation(id = 1, branch_name = 'DC Office', city = 'Reston', state ='VA', country = 'USA')
branch2 = BranchLocation(id = 2, branch_name = 'New York Office', city = 'New York', state ='NY', country = 'USA')
branch3 = BranchLocation(id = 3, branch_name ='Dallas Office', city = 'Dallas', state ='TX', country = 'USA')
branch4 = BranchLocation(id = 4, branch_name ='Orlando Office', city = 'Orlando', state ='FL', country = 'USA')
branch5 = BranchLocation(id = 5, branch_name ='West Virgina University', city = 'Morgantown', state ='WV', country = 'USA')

'''
Create the in-house variables for genders
'''
gender1 = Gender(id=1, gender = "Male")
gender2 = Gender(id=2, gender = "Female")
gender3 = Gender(id=3, gender = "Other")

'''
Create Demo Data
'''

number_of_users = 75
number_of_posts = 200
range_of_comments = (0,10) 
range_of_likes = (0,50)

file_string = ""

universal_password = str(bcrypt.hashpw(b'password',bcrypt.gensalt()))

i = 0
while(i<number_of_users):
  user = User()
  gender = choice([1,2,3],p=[0.47,0.47,0.06])
  if(gender==1):
    fname = fake.first_name_male()
  elif(gender==2):
    fname = fake.first_name_female()
  else:
    fname = fake.first_name()
  lname = fake.last_name()

  username = fname[0]+lname+str(r.randint(1,99))

  branch = choice(Entity.pool.get(BranchLocation.tablename)).get("id")

  user.set("id", i+1)
  user.set("first_name", fname)
  user.set("last_name", lname)
  user.set("gender", gender)
  user.set("email", username+"@email.com")
  user.set("username", username)
  user.set("passwrd", universal_password[2:len(universal_password)-2])
  user.set("date_of_birth", fake.date_between("-40y","-19y"))
  user.set("branch",branch)

  print(user.getInsertStatement()) 
  file_string += user.getInsertStatement()+"\n"

  i+=1

i = 0
while(i<number_of_posts):

  title = ""
  j = r.randint(2,4)
  while(j>0):
    title+=fake.word()
    if(j!=1): 
      title+=" "
    j-=1

  body = ""
  j = r.randint(25,100)
  while(j>0):
    body+=fake.word()
    if(r.randint(1,15)==7):
      body+="."
    if(j!=1): 
      body+=" "
    j-=1

  

  post = Post()
  post.set("id",i+1)
  post.set("poster_id",choice(Entity.pool.get(User.tablename)).get("id"))
  post.set("title", title)
  post.set("body", body)
  post.set("created", fake.date_between("-30d","today"))

  if(r.randint(1,5)==1):
    post.set("last_edited",fake.date_between(post.get("created"), "today"))

  print(post.getInsertStatement())
  file_string += post.getInsertStatement()+"\n"

  j=0
  stop = r.randint(range_of_comments[0],range_of_comments[1])
  while(j<stop):

    body = ""
    h = r.randint(25,100)
    while(h>0):
      body+=fake.word()
      if(r.randint(1,15)==7):
        body+="."
      if(h!=1): 
        body+=" "
      h-=1


    comment = PostComment()
    comment.set("id",j+1)
    comment.set("post_id", i+1)
    comment.set("commenter_id",choice(Entity.pool.get(User.tablename)).get("id"))
    comment.set("message", body)
    comment.set("created",fake.date_between(post.get("created"),"today"))
    
    print(comment.getInsertStatement())
    file_string += comment.getInsertStatement()+"\n"
    j+=1

  j=0
  stop = r.randint(range_of_likes[0],range_of_likes[1])
  users_liked_this_post = []
  while(j<stop):

    user_id = choice(Entity.pool.get(User.tablename)).get("id")
    if(user_id in users_liked_this_post):
      break;
    
    if(user_id == post.get("poster_id")):
      break;

    users_liked_this_post.append(user_id)

    like = UserLike()
    like.set("user_id",user_id)
    like.set("post_id",i+1)

    print(like.getInsertStatement())
    file_string += like.getInsertStatement()+"\n"
    j+=1

  i += 1

file = open("output.txt","w")
file.write(file_string)
file.close()


