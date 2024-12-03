import os
import re

# with open('../inputs/Day3TestInput.txt', 'r') as file:
with open('../inputs/Day3Input.txt', 'r') as file:
	total = 0
	full_input = ''
	for line in file:
		full_input += line
	muls = re.findall('mul\(\d\d?\d?,\d\d?\d?\)', full_input)
	for mul in muls:
		inputs = mul.strip('mul(,)').split(',')
		total += int(inputs[0]) * int(inputs[1])
	print(total)

# with open('../inputs/Day3TestInputPt2.txt', 'r') as file:
with open('../inputs/Day3Input.txt', 'r') as file:
	total = 0
	full_input = ''
	for line in file:
		full_input += line
	enabled = True
	start = 0
	while enabled:
		donts = re.search('don\'t\(\)', full_input[start:])
		if donts is None:
			muls = re.findall('mul\(\d\d?\d?,\d\d?\d?\)', full_input[start:])
			for mul in muls:
				inputs = mul.strip('mul(,)').split(',')
				total += int(inputs[0]) * int(inputs[1])
			enabled = False
			break
		else:
			end = donts.span()[0] + start
			muls = re.findall('mul\(\d\d?\d?,\d\d?\d?\)', full_input[start:end])
			for mul in muls:
				inputs = mul.strip('mul(,)').split(',')
				total += int(inputs[0]) * int(inputs[1])
			
			dos = re.search('do\(\)', full_input[end:])
			if dos is None:
				enabled = False
				break
			else:
				start = end + dos.span()[1]
	
	print(total)
