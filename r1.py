
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:    # -sig 是用來去掉一些編碼的紀錄
		for line in f:
			lines.append(line.strip())    #.strip() 是用來去掉換行符號\n
	return lines

def convert(lines):
	new = []
	person = None    # 避免若 input 檔第一行不是人名，下面執行會當掉
	for line in lines:
		if line == 'Allen':
			person = "Allen"
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + ': ' + line)
	return new

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()