#----------------------------------------------------------------------
#
# Author:      Han Jing
#
#----------------------------------------------------------------------

class KeySearcher:

  def __init__(self, key, hash):
    self.key = key #maybe change this later to expand database coverage?
    self.hash = hash
    
  def findOneKey(self, hash):
    if self.key in hash.keys():
      return True
    return False
  
  def hasKey(self, hash):
    print hash
    #print hash.keys()
    if type(hash) == type([]) or type(hash)== type(()):
      for h in hash:
        return self.hasKey(h)
    if type(hash) != type({}):
      return False
    if hash.has_key(self.key):
      return True
    #print hash.values()
    for h in hash.values():
      #print 'hash is:', hash
      #print 'hash value is:' , h
      #if type(h) != type({}):
        #print h, 'is not a hash'
      #  continue
      #this is a hash
      if (self.hasKey(h)):
        return True
    return False
    
  def getValue(self, hash):
    #print hash
    #print hash.keys()
    if type(hash) == type([]) or type(hash)== type(()):
      for h in hash:
        return self.getValue(h)
    if type(hash) != type({}):
      return None
    if hash.has_key(self.key):
      return hash[self.key]
    for h in hash.values():
      #print 'hash is:', hash
      print 'hash value is:' , h
      #this is a hash
      if (self.getValue(h) != None):
        return self.getValue(h)
    return None
    

if __name__ == '__main__':
  h = {'a':{'b':{'c':{'d':0}}}, 'e':11, 'g':[{'l':10}]}
  s = KeySearcher('d', h)
  print s.hasKey(h)
  print s.getValue(h)
    
      
        