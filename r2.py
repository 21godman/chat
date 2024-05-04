def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:    # -sig 是用來去掉一些編碼的紀錄
		for line in f:
			lines.append(line.strip())    #.strip() 是用來去掉換行符號\n
	return lines

def convert(lines):
	person = None    # 避免若 input 檔第一行不是人名，下面執行會當掉
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_image_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('Allen 說了', allen_word_count)
	print('Allen 傳了', allen_sticker_count, '個貼圖')
	print('Allen 傳了',allen_image_count, '張圖片')
	
	print('Viki 說了', viki_word_count)
	print('Viki 傳了', viki_sticker_count, '個貼圖')
	print('Viki 傳了', viki_image_count, '張圖片')

		# print(s)

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	# write_file('output.txt', lines)

main()