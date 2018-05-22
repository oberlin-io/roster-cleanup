# Student roster TXT to array
with open('roster.txt', 'r') as f:
	roster = f.read()

students = roster.splitlines()



# CAPs to lowercase
low = 'abcdefghijklmnopqrstuvwxyz0123456789.,- '
cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,- '

def char_chng(ch):
	'''
	Converts one character from caps to lowercase
	'''
	
	if ch in cap:
	
		return low[cap.index(ch)]
			
	else:
	
		return ch


def name_chng(n):
	'''
    Iterates char_chng module through a string or abstains for special cases,
	such as first letter of string, letter after a space, and letter after hyphen.
	'''
	
	s = ''
	
	for i in range(len(n)):
		
		# Cap first letter of string
		if i == 0:
			s += n[i]

		# Cap letter after space
		elif n[i-1] == ' ':
			s += n[i]
			
		# Cap letter after hyphen
		elif n[i-1] == '-':
			s += n[i]
		
		else:
			s += char_chng(n[i])
	
	return s


	
# Last and first switch
def switch(name):
	'''
	Reverse Last Name, First Name order
	'''
	
	if ',' in name:
	
		for i in range(len(name)):
			
			if name[i] == ",":
				last = name[:i]
				first = name[i+2:]
	
		return first + " " + last
	
	else:
	
		return name



# Iterate modules through roster
for s in students:

	students[students.index(s)] = name_chng(switch(s))
	
	

# Output as TXT
new_roster = ''
for s in students:
	new_roster += s + '\n'
	
with open('updated-roster.txt', 'w') as f:
	f.write(new_roster)

done = raw_input('Finished')

