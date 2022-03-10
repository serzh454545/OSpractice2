import hashlib
import multiprocessing
import time


def hash(hashes):
	word = ""
	letters = list("abcdefghijklmnopqrstuvwxyz")
	result = {}
	for l1 in letters:
		for l2 in letters:
			for l3 in letters:
				for l4 in letters:
					for l5 in letters:
						word = bytes(l1+l2+l3+l4+l5, encoding='utf-8')
						if hashlib.sha256(word).hexdigest() in hashes:
							result[hashlib.sha256(word).hexdigest()] = word
	print(result)


if __name__ == '__main__':
	qwetions = int(input("Сколько хешей вы хотите ввести? "))
	hashes = []
	for i in range(0, qwetions):
		hashes.append(str(input("Хэш: ")))
		i += 1
	
	ptch = input("Введите 1 для однопоточности, введите 2 для многопоточности: ")
	if ptch == '1':
		timer = time.time()
		
		hash(hashes)

		print("Время: ", time.time() - timer)
	elif ptch == '2':
		timer = time.time()
			
		with multiprocessing.Pool(multiprocessing.cpu_count() * qwetions) as p:
			p.map(hash, hashes)

		print("Время: ", time.time() - timer)
