
lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ')
	time = s[0][:5]    # 字串中的每個字符都可以被視為清單中的一個元素
	name = s[0][5:]
	print(time)
	print(name)