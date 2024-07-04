
english=float(input("enter english marks "))
physics=float(input("enter physics marks "))
chemistry=float(input("enter chemistry marks"))

total= english + physics + chemistry
percentage= (total/300) * 100

print('                                    marksheet')
print('subjects                                                             marks')
print('english                                                               ', english)
print('physics                                                               ', physics)  
print('chemistry                                                             ', chemistry)

print('                                                          total marks ', total)
print('                                                         percentage  ', percentage)
