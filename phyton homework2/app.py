#Tapsiriq 1

a=int(input("Enter a:"))
b=int(input("Enter b:"))
print(a*b)




#Tapsiriq 2

num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
print(bool(num1>num2))


#Tapsiriq 3
#İstifadəçi flaş drive-ın gigabayt ilə ölçüsünü daxil edir. 760 Megabaytlıq kinonun həmin flaşa neçə dəfə yerləşəcəyini tapan program yazın.

flash_size_gb = float(input("Enter the size of the flash in gb: "))


movie_size_mb = 760
flash_size_mb = flash_size_gb * 1024  
times_fit = flash_size_mb / movie_size_mb


print(f"A 760MB movie can fit {int(times_fit)} times on the {flash_size_gb}GB flash.")


#Tapsiriq 4
#İstifadəçi a və b-ni daxil edir, ax+b=0 tənliyini hesablayıb x-i tapan proqram yazın.
a=int(input("Enter a:"))
b=int(input("Enter b:"))
if a == 0:
    print("No solution")
else:
    x = -b / a
    print(f"The solution for {a}x + {b} = 0 is x = {x}")
    



#Tapsiriq 5
#İki rəqəm daxil edilir, onların ədədi ortasını tapan proqram yazın.

a=int(input("Enter a:"))
b=int(input("Enter b:"))
c = (a+b)/2
print(c)




#Tapsiriq 6
def polindrome(n):
    
    a = str(n)
    
    if a == a[::-1]:
        return True
    else:
        return False
    
print(polindrome(90009))
print(polindrome(12321))
print(polindrome(87678))