
english=float(input("enter english marks "))
nepali=float(input("enter nepali marks "))
math=float(input("enter math marks "))
physics=float(input("enter physics marks "))
chemistry=float(input("enter chemistry marks "))

total = english + nepali + math + physics + chemistry
percentage= (total/500) * 100


print('                                    Marksheet')
print('Subjects                                                               Marks')
print('English                                                                 ',english)
print('Nepali                                                                  ',nepali)
print('Math                                                                    ',math)
print('Physics                                                                 ',physics)
print('Chemistry                                                               ',chemistry)

print("                                                                         total marks", total)
print("                                                                         marks percentage", percentage)
