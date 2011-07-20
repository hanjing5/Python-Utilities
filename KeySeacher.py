#----------------------------------------------------------------------
#
# Author:      Han Jing
#
#----------------------------------------------------------------------

class KeySearcher:

  def __init__(self, key, hash):
    self.key = key
    self.hash = hash
    
  def findOneKey(self, hash):
    if self.key in hash.keys():
      return True
    return False
  
  def hasKey(self, hash):
    if type(hash) == type([]) or type(hash)== type(()):
      for h in hash:
        return self.hasKey(h)
    if type(hash) != type({}):
      return False
    if hash.has_key(self.key):
      return True
    for h in hash.values():
      if (self.hasKey(h)):
        return True
    return False
    
  def getValue(self, hash):
    if type(hash) == type([]) or type(hash)== type(()):
      for h in hash:
        return self.getValue(h)
    if type(hash) != type({}):
      return None
    if hash.has_key(self.key):
      return hash[self.key]
    for h in hash.values():
      if (self.getValue(h) != None):
        return self.getValue(h)
    return None
    

if __name__ == '__main__':
'''#testing code
  h = {'a':{'b':{'c':{'d':0}}}, 'e':11, 'g':[{'l':10}]}
  s = KeySearcher('d', h)
  print s.hasKey(h)
  print s.getValue(h)'''
    
      
        