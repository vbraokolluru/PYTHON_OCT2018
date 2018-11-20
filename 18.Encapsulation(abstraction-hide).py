# data / method -  Encapsulation/Abstraction /Hide 

# variable 
class Normalclass: 
   secretvalue = 10 
   
   def dispname(self): 
      self.secretvalue += 1 
      print (self.secretvalue) 
 
hc = Normalclass() 
hc.dispname()
hc.dispname()

hc.secretvalue
 
class Hideclass: 
   __secretvalue = 10 
   
   def dispname(self): 
      self.__secretvalue += 1 
      print (self.__secretvalue) 
 
hc = Hideclass() 
hc.dispname()
hc.dispname()
hc.__secretvalue
# normal calling
print (hc.__secretvalue) 
# secret variables (Abstract/hide) variables calling 
print (hc._Hideclass__secretvalue)

#**********************
# another example for methodsand variable

class Marks:

    def __init__(self):
        self.__totmarks = 200

    def disp(self):
        print("Total marks : {}".format(self.__totmarks))

    def changemarks(self, marks):
        self.__totmarks = marks
    
    def __rank(self):
        print ('rank of the student is here : 1')

c = Marks()
c.disp()

# change the price
c.__totmarks = 232
c.disp()

c._Marks__totmarks=400
c.disp()

# using setter function
c.changemarks(232)
c.disp()
c.__rank()  
c._Marks__rank()
