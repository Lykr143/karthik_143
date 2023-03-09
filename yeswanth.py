#wap to move all zeros of the list
#input = [1,0,1,0,1,0]
#output = [1,1,1,0,0,0]
'''l = [1,0,1,0,1,0]
j = 0
for i in range(len(l)):
	if l[i] != 0:
		l[j],l[i] = l[i],l[j]
		j = j + 1
print(l)'''

#wap to get the difference of sum of odd numbers and sum of even number
#input = [1,2,3,4,5]
#output = [3]
'''l = [1,2,3,4,5]
e_sum = 0
o_sum = 0
for i in l:
	if i%2 == 0:
		e_sum = e_sum + i
	else:
	    o_sum = o_sum + i
print(o_sum - e_sum)'''

#wap to swap the even indeceed number with adjacent odd index of numbers
#input = [1,2,3,4,5,6]
#output = [2,1,4,3,6,5]

'''l = [1,2,3,4,5,6]
for i in range(0, len(l), 2):
	l[i], l[i+1] = l[i+1], l[i]
print(l)'''

#wap to find duplicate elements of the list
#input = [1,2,1,3,1,2,1]
#output = [1,2]
'''l = [1,2,1,3,1,2,1]
l1 = []
for i in range(len(l)):
	for j in range(i+1, len(l)):
		if l[i] == l[j]:
			l1.append(l[j])
print(list(set(l1)))'''

#wap to print the list of elements along with their no of occurance
#input = [1,2,3,4,2,3,2,3,2]
#output = {1:1, 2:4, 3:3, 4:1}	
'''l = [1,2,3,4,2,3,2,3,2]
d = {}
for i in l:
	d[i] = l.count(i)
print(d)'''

#wap to add the elements of given list based on their index position
#l1 = [1,2,3]
#l2 = [4,5,6]
#output = [5,7,9]

'''l1 = [1,2,3]
l2 = [4,5,6]
l3 = []
for i in range(len(l1)):
	add = l1[i] + l2[i]
	l3.append(add)
print(l3)'''	 


'''WAP to print a dictionary which contains the first charecter of every word in below string as Keys
   and list of words which starts with specific charecter as values.

   	input: my_string = "Python is my favorite programming language im"

	# Key => Starting letter each word
	# Value => ['Python', 'Programming']

	output: {
			 'p': ['Python', 'programming'], 'i': ['is'], 'm': ['my'],
			 'f': ['favorite'], 'l': ['language'], 'i': ['im']
			}'''

'''my_string = "Python is my favorite programming language im"
words = my_string.split()
  
# Declaring empty dictionary
dictionary = {}
  
for word in words:
  
    # If key is not present in the dictionary then we
    # will add the key and word to the dictionary.
    if (word[0].lower() not in dictionary.keys()):
  
        # Creating a sublist to store words with same
        # key value and adding it to the list.
        dictionary[word[0].lower()] = []
        dictionary[word[0].lower()].append(word)
  
    # If key is present then checking for the word
    else:/
  
        # If word is not present in the sublist then
        # adding it to the sublist of the proper key
        # value
        if (word not in dictionary[word[0].lower()]):
            dictionary[word[0].lower()].append(word)
  
# Printing the dictionary
print(dictionary)'''
#wap to find out the square root numbers
'''from math import sqrt
l = [9,16,25,49,125]
op = []
for i in l:
	op.append(sqrt(i))
print(op)'''

#wap to print the current date, time and day of the week
'''import datetime
now = datetime.datetime.now()
print(now.strftime('%Y-%m-%d %H-%M-%S %A'))'''

#decorators

data = '''hari  h.sharma212@gmail.com  9533977887
          raja  raj@gmail.com          9399767689
         jana  jana@gmail.com         9887653421'''


def convert_data(f):
	def wrapper(data):
		op = ""
		for row in data.splitlines():
			dt = row.split()
			op += "{}-{} {} {}\n".format(dt[0], dt[1].split('@')[0], dt[1], dt[2])
		return f(op)
	return wrapper


@convert_data
def read_data(data):
	op = {}
	for row in data.splitlines():
		op[row.split()[0]] = {'mail' : row.split()[1], 'mobile': row.split()[2]}
	return op

print(read_data(data))


'''data = """name1 bangalore IBM 15000
name2 bangalore IBM 20000
name3 hyderbad TCS 25000"""


#wap to print average salaries of employees who are working in bangalore
def get_average(data, location):
	op = [int(row.split()[-1]) for row in data.splitlines() if location in row]
	return sum(op) / len(op)
print(get_average(data, ("bangalore")))'''

#wap to print display list of employees names working in bangalore
'''def get_emp_name(data, location):
	op = [row.split()[0] for row in data.splitlines() if location in row]
	return op
print(get_emp_name(data, "bangalore"))

#wap to print company names located in bangalore
def get_company_name(data, location):
	op = [row.split()[2] for row in data.splitlines() if location in row]
	return op
print(get_company_name(data, "bangalore"))'''


#wap to read the above json file and print employee name and age of them
'''import json
finaldata = json.loads(open('yeswanth.json').read())

for name, val in finaldata.items():
	print(name, val['age'])'''


#Read the given "URL" and print all the image names in it
'''href'import requests
from bs4 import BeautifulSoup
 
url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []
for link in soup.find_all('a'):
    print(link.get())

#wap to get your system configuration
import platform
print(platform.system())
print(platform.processor())
print(platform.architecture())
print(platform.platform())
print(platform.python_version())
print(platform.processor())


import json

fp = open('yeswanth.json')
'''

#wap to wait for 5 sec and turn of the laptop
'''import time, os
time.sleep(5)
os.system("shutdown -s")'''

'''wap to print the first character of every word and the words it started with it''' 
'''
s = "I love my country I love python programming"
op = {}
for word in s.split():
	if word[0] not in op:
		op[word[0]] = [word]
	else:
	    op[word[0]].append(word)
print(op)'''
#output:{'I': ['I', 'I'], 'l': ['love', 'love'], 'm': ['my'], 'c': ['country'], 'p': ['python', 'programming']}

s = "Hello world welcome to python programming"
'''wap to print the world which start with either 'w' or 'p' '''
''

def get_words(word):
	if word[0] in 'pw':
		return word
print(list(filter(get_words, s.split())))
            or
print([word for word in s.split() if word[0] in 'pw'])'''


''' wap sort the list without using sort function'''
'''l = [4,5,6,8,-1,9,-2]
for i in range(len(l)):
	for j in range(i, len(l)):
		if l[i] > l[j]:
			l[i], l[j] = l[j], l[i]
print(l)'''


# s = "i am yeswanth i have gone through the important for the system"
# f = enumerate(s)
# print(list(enumerate(s)))


# l = [6,7,9,5,4,0,2,-1,49]
# for i in range(len(l)):
# 	for j in range(i, len(l)):
# 		if l[i] > l[j]:
# 			l[i], l[j] = l[j], l[i]
# print(l)



s = "yeswanth is a good boy for you have in nature"
op = {}
for word in s.split():
	if word[0] not in op:
		op[word[0]] = [word]
	else:
		op[word[0]].append(word)
print(op)		
		
# def get_words(word):
# 	if word[0] in "yi":
# 		return word
# print(list(filter(get_words, s.split())))


# i = 1
# x = 1
# while(i < 4):
# 	x = x + (2*i)
# 	i = i+1
# print(x)


# s = "i am python developer,working@Dell"
# print(list(enumerate(s)))










	
	







			







		



	
	
	



	


























 






































