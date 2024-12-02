import os
import re


def check_report_safety(levels):
	change = 'inc'
	for i in range(len(levels)-1):
		diff = int(levels[i]) - int(levels[i+1])
		if abs(diff) < 1 or abs(diff) > 3:
			return False, i
		if diff < 0 and i == 0:
			change = 'dec'
		elif diff > 0 and change == 'dec':
			return False, i
		elif diff < 0 and change == 'inc':
			return False, i
	return True, -1

# with open('../inputs/Day2TestInput.txt', 'r') as file:
with open('../inputs/Day2Input.txt', 'r') as file:
	safe_reports = 0
	for report in file:
		levels = report.rstrip('\n').split(' ')
		safe, index = check_report_safety(levels)
		if safe:
			safe_reports += 1
	print(safe_reports)


# with open('../inputs/Day2TestInput.txt', 'r') as file:
with open('../inputs/Day2Input.txt', 'r') as file:
	safe_reports = 0
	for report in file:
		levels = report.rstrip('\n').split(' ')
		safe, index = check_report_safety(levels)
		if index == 1:
			safe, _ = check_report_safety(levels[1:])
		if not safe:
			dampened_list = levels[:index] + levels[index+1:]
			safe, new_index = check_report_safety(dampened_list)
		if not safe:
			dampened_list = levels[:index+1] + levels[index+2:]
			safe, new_index = check_report_safety(dampened_list)
		if safe:
			safe_reports += 1
	print(safe_reports)
