math = ["charlie", "kevin", "alise", "bob", "leo"]
physic = ["jack", "paolo", "alex", "bob", "charlie"]
N = input("Please enter a name to add to math: ")
math.append(N)
Y = input("Please enter a name to add to physics: ")
physic.insert(2, Y)
math.sort()
physic.sort()
print("math list: ", math)
print("physic list: ", physic)
T = input("Please enter a name to remove from physics: ")
if T in physic:
    physic.remove(T)
print ("math list: ", math)
print("physic list: " ,physic)
