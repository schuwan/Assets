class EntityPool:

  def __init__(self):
    self._pool = {}

  '''
  entityPool.add(type, entity)
  Adds to the array of entities of the same type. Creates
  the array if it does not already exist
  '''
  def add(self, typ, entity):
    if(typ in self._pool):
      self._pool[typ].append(entity)
    else:
      self._pool[typ] = [entity];

  '''
  entityPool.get(type)
  Retrieves list of entities of a specific type
  '''
  def get(self, type):
    try:
      return self._pool[type]
    except KeyError:
      return None

  '''
  entity.toString()
  Returns a stringified list of all entities in the 
  pool
  '''
  def toString(self):
    string = ""
    for category, lis in self._pool.items():
      string +="\n"+str(category)+"s: "
      for item in lis:
        string+="\n    "+item.toString()
    return string


class Entity:

  pool = EntityPool();

  '''
  entity(type, attribute, kwrgs)
  Initalizes the entity with the following value:

  o type - descriptive string naming the entity         (set in child classes)
  o attributes - list of attributes that the entity has (set in child classes)
  o kwrgs - inital settings of an entity
            (note - must match the attributes list)
           
  example: User(username = 'hello world')
  '''
  def __init__(self, type, attributes, quotedAttributes, kwrgs):
    self.type = type
    self.attributes = attributes;
    self.quotedAttributes = quotedAttributes
    self._values = {}
    
    for key, value in kwrgs.items():
      self.set(key, value)

    Entity.pool.add(self.type, self)
  
  '''
  entity.get()
  Returns a value if it exists as an attribute in the entity
  Retuns none if the attribute has not been set. Raises an 
  exception if the attribute does not exist for this entity
  '''
  def get(self, key):
    try:
      return self._values[key]
    except KeyError:
      if(key in self.attributes):
        return None
      else:
        Entity.NoSuchAttributeException(self.type, key)

  '''
  entity.set()
  Sets an attribute to some value if the attribute exists in 
  the entity's attribute tupple. Raises an exception otherwise
  '''
  def set(self, key, value):
    if(key in self.attributes):
      self._values[key] = value
    else:
        Entity.NoSuchAttributeException(self.type, key)


  '''
  entity.getAll()
  Returns a dictonary of all attributes and their values. Will 
  return None for all unset values
  '''
  def getAll(self):
    dic = {}
    for attr in self.attributes:
      dic[attr] = self.get(attr)
    return dic

  '''
  entity.getAllFilledCols()
  Returns a dictonary of all attributes and their values. Will 
  return None for all unset values
  '''


  '''
  entity.getInsertStatement()
  Returns a string with an SQL query with table name of type.
  Raises an exception if there are no values assigned
  '''
  def getInsertStatement(self):

    if(len(self._values)==0):
      raise Exception("Entity must have at least one value assigned to generate SQL statement")

    string = "INSERT INTO "+self.type+" ("
    i=0
    cols = list(self._values.keys())
    for col in cols:
      if(col != "id"):

        string+=str(col)
        if i!=len(self._values)-1:
          string+=", "
      
      i+=1
    string +=") VALUES ("
    i=0
    for val in self._values.values():
      if(cols[i]!="id"):
        string+= self.quotedIfApplicable(val,cols[i])
        if i!=len(self._values)-1:
          string+=", "
        
      i+=1
    string+=");"
    return string
  '''
  entity.quotedIfApplicable(val,attributeIndex)
  Takes a value that is to be inserted into a table and adds quotes iff that attribute is defined to need them
  '''
  def quotedIfApplicable(self,val,attribute):
    if(attribute in self.quotedAttributes):
      return "\'" + str(val) + "\'"
    else:
      return str(val)

  '''
  entity.toString()
  Returns a stringified version of an entity with all its
  attributes
  '''
  def toString(self):
    string = str(self.type)+":" +str(self.getAll())
    return string

  '''
  Exceptions
  '''
  def NoSuchAttributeException(typ, key):
    raise Exception("\n\nNo such attribute exists in Entity of type '"+str(typ)+"'. \nattribute: "+str(key))

  def DateTimeFormattingException():
    raise Exception("\n\nYear must be written in format YYYY")




class ImageLocation(Entity):
  tablename = "image_locations"
  attributes = ("id","url")
  quotedAttributes = ("url")

  def __init__(self, **kwrgs):
    Entity.__init__(self, ImageLocation.tablename, ImageLocation.attributes, ImageLocation.quotedAttributes, kwrgs)

class Gender(Entity):
  tablename = "genders"
  attributes = ("id","gender")
  quotedAttributes = ("gender")

  def __init__(self, **kwrgs):
    Entity.__init__(self, Gender.tablename, Gender.attributes, Gender.quotedAttributes, kwrgs)

class BranchLocation(Entity):
  tablename = "branch_locations"
  attributes = ("id","branch_name","city","state","country")
  quotedAttributes = ("branch_name","city","state","country")

  def __init__(self, **kwrgs):
    Entity.__init__(self, BranchLocation.tablename, BranchLocation.attributes, BranchLocation.quotedAttributes, kwrgs)


class ProfilePicture(Entity):
  tablename = "profile_pictures"
  attributes = ("id","image_location","image_name")
  quotedAttributes = ("image_name")

  def __init__(self, **kwrgs):
    Entity.__init__(self, ProfilePicture.tablename, ProfilePicture.attributes, ProfilePicture.quotedAttributes, kwrgs)


class User(Entity):
  tablename = "users"
  attributes = ("id","username","email","first_name","last_name","passwrd","date_of_birth","gender","branch","profile_picture")
  quotedAttributes = ("username","email","first_name","last_name","passwrd","date_of_birth")

  def __init__(self, **kwrgs):
    Entity.__init__(self, User.tablename, User.attributes, User.quotedAttributes, kwrgs)


class Post(Entity):
  tablename = "posts"
  attributes = ("id","poster_id","title","body","created","last_edited")
  quotedAttributes = ("title","body","created","last_edited")

  def __init__(self, **kwrgs):
    Entity.__init__(self, Post.tablename, Post.attributes, Post.quotedAttributes, kwrgs)


class PostImage(Entity):
  tablename = "post_images"
  attributes = ("id","post_id","image_location","image_name","image_title")
  quotedAttributes = ("image_name","image_title")

  def __init__(self, **kwrgs):
    Entity.__init__(self, PostImage.tablename, PostImage.attributes, PostImage.quotedAttributes, kwrgs)


class PostComment(Entity):
  tablename = "post_comments"
  attributes = ("id","post_id","commenter_id","message","created")
  quotedAttributes = ("message","created")

  def __init__(self, **kwrgs):
    Entity.__init__(self, PostComment.tablename, PostComment.attributes, PostComment.quotedAttributes, kwrgs)

class UserLike(Entity):
  tablename = "user_likes"
  attributes = ("user_id","post_id")
  quotedAttributes = ()

  def __init__(self, **kwrgs):
    Entity.__init__(self, UserLike.tablename, UserLike.attributes, UserLike.quotedAttributes, kwrgs)

