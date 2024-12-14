import os
import re
import collections

def fix_updates(incorrect, rules):
	temp = incorrect.copy()
	fixed = []
	while len(fixed) != len(temp):
		valid = True
		for i in range(len(fixed), len(temp)):
			for j in range(i, len(temp)):
				if temp[j] in rules[temp[i]]:
					valid = False
					temp[i], temp[j] = temp[j], temp[i]
			if valid:
				fixed.append(temp[i])
	return fixed
	

# with open('../inputs/Day5TestInput.txt', 'r') as file:
with open('../inputs/Day5Input.txt', 'r') as file:
	input = file.read().split('\n\n')
	rules = input[0].split('\n')
	updates = input[1].rstrip().split('\n')
	valid_total = 0
	fixed_total = 0

	rules_dict = collections.defaultdict(list)
	for rule in rules:
		nums = rule.split('|')
		rules_dict[nums[1]].append(nums[0])

	for update in updates:
		valid = True
		pages = update.split(',')
		temp = []
		for i in range(len(pages)):
			for j in range(i, len(pages)):
				if pages[j] in rules_dict[pages[i]]:
					valid = False
					break
			if not valid:
				fixed = fix_updates(pages, rules_dict)
				fixed_total += int(fixed[int(len(fixed)/2)])
				break
		if valid:
			valid_total += int(pages[int(len(pages)/2)])

	print(valid_total)
	print(fixed_total)
