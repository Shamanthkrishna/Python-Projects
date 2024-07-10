from time import time

start = time()
#Python Program to create acronyms
word = "Data Base Management System"
text = word.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
end = time()


execution_time = end - start

print(f"Generated Acronym: {a}")
print(f"Execution Time is {execution_time} seconds")