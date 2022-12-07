try:
    a = open("kk1.txt","r")
except FileNotFoundError:
    print("exception")

class OurException(Exception):
    def __init__(self,message):
        self.message=message
class UsingUserException:
    try:
        a=int(input("a: "))
        b = int(input("b: "))
        if b==0:
            raise OurException("b should be greater than 0")
        d=a/b
        print("division operation successful with result:",d)
    except OurException as err:
        print("user defined exception:",err.message)

# wap to create a dict in binary form
import pickle
animalDict = {'Car' : 2, 'Dog':7,'Lion':4,'Tiger':9,'Leopard':11,'Bear':8,'Elephant':15}
outfile = open('animals','wb')
pickle.dump(animalDict,outfile)
outfile.close()
fst = open('animals','rb')
data = pickle.load(fst)
try:
    while(True):
        print(data)
        data = pickle.load(fst)
except:
    print("Bye")
