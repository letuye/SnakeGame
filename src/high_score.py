def read_highscore(filename):
	try:
		with open(filename, "r") as file:
			high_score = file.read().strip()
			return int(high_score)
	except FileNotFoundError:
		print(f"File {filename} không tìm thấy")
		return 0
	except ValueError:
		print(f"file {filename} không hợp lệ")
		return 0
	
def write_highscore(filename, score):
	try:
		with open(filename, "w") as file:
			file.write(str(score))	
	except FileNotFoundError:
		print(f"File {filename} không tìm thấy")
	except ValueError:
		print(f"Nội dung trong file {filename} không hợp lệ")
		
	
