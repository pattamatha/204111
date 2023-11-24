#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 09
# Problem 4
# 204111 Sec 001

def main():
	list_a = [1, 2, [[3, 0], 4], 8]
	print(sum_nested_list(list_a))
	print(sum_nested_list([1, 2, [[2, [[145], 34]], [48, 22]]]))
	print(sum_nested_list([58, [31, [90]]]))
	print(sum_nested_list([61, [[2, [75]], 8000, [39]], [58, [46]]]))
	print(sum_nested_list([81, [[31, [159]], 9577, [22, [181, [41]]]]]))

def sum_nested_list(list_a):
	# ทำให้ nested list กลายเป็น list 1D
	list_b = []	# สร้างlistเปล่า เพื่อเก็บค่าในแต่ละครั้ง เพื่อทำให้เป็น list1D
	for i in list_a:
		item = [i].pop() #เลือกวัตถุในแต่ครั้งและลบไปพร้อมๆกัน
		if isinstance(item, list) == True:
			list_a.extend(item)
		else: 
			list_b.append(item)
	# เมื่อเป็น list 1D ก็จะสามารถหาผลรวมได้เลย
	result = sum(list_b)
	return result

	'''
	note : 	extend ต่างจาก append ...?
			extend จะเพิ่มวัตถุ(วัตถุนี้อยู่ในiterableอีกที)ในตำแหน่งสุดท้ายของlist
			append จะเพิ่มวัตถุในตำแหน่งสุดท้ายของlist(ซึ่งวัตถุนั้นจะเป็น int, list หรืออื่นๆ)
	'''

if __name__ == '__main__':
	main()