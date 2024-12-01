import os
import re
import bisect

# with open('../inputs/Day1Testinput.txt', 'r') as file:
with open('../inputs/Day1Input.txt', 'r') as file:
	first_list = []
	second_list = []
	for line in file:
		splitline = line.replace('\n', '').split(' ')
		bisect.insort(first_list, int(splitline[0]))
		bisect.insort(second_list, int(splitline[-1]))
	total = 0
	for i in range(len(first_list)):
		total += abs(first_list[i] - second_list[i])
	
	print('Day 1 Part 1 Solution:' + str(total))

# with open('../inputs/Day1Testinput.txt', 'r') as file:
with open('../inputs/Day1Input.txt', 'r') as file:
	first_list = []
	second_dict = {}
	for line in file:
		splitline = line.replace('\n', '').split(' ')
		first_list.append(int(splitline[0]))
		second_num = int(splitline[-1])
		if second_num in second_dict:
			second_dict[second_num] += 1
		else:
			second_dict[second_num] = 1
	similarity_score = 0
	for i in first_list:
		count = 0
		if i in second_dict:
			count = second_dict[i]
		similarity_score += i * count
	
	print('Day 1 Part 2 Solution:' + str(similarity_score))
