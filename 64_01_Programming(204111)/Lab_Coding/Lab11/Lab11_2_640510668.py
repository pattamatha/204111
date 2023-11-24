#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Lab 11
# Problem 2
# 204111 Sec 001

def main():
	list_x = [("11/1/1900","Event A"),("5/12/2001","Event B"),
	("5/12/2002","Event C"),("21/8/2008","Event D"),
	("9/3/2013","Event E"),("11/3/2017","Event F"),
	("7/5/2019","Event G"),("29/2/2032","Event H"),
	("9/11/2042","Event I")]
	event = search_event(list_x, "29/02/2032")
	print("---")
	print(event)

def search_event(list_x, key):
	# ทำการเคลียร์ key คือถ้ามีเลขศูนย์หน้าเลขอื่นๆ ให้ทำการลบเลขศูนย์นั้นออก
	k1 = key.split("/")		# k1 = ['29', '02', '2032']
	k2 = []				# สร้าง k2 ที่เป็นlistเปล่า มาเก็บค่าวันเดือนปีที่ลบเลขศูนย์ด้านหน้าออก
	for i in k1:
		j = str(int(i))
		k2.append(j)
	key = "/".join(k2)	# key = "29/2/2032"
	
	dict_x = dict(list_x) # สร้าง dict ของ list_x
	for x in dict_x:	  # วนทีละ x (x คือ keyของdict_x)
		if x == key:
			return (x, dict_x[x])

if __name__ == '__main__':
	main()