#!/usr/bin/env python3
# ปัทมาพร ถาเป็นบุญ
# 640510668
# Quiz2 1/64
# Problem 2A
# 204111 Sec 001

def splice(rna,start,stop,mode='alpha'):
    # alpha คือการตัด RNA ส่วนที่ต้องการออกไป
    if mode == 'alpha':
        del rna[start:stop+1]
        return rna
    # beta คือการตัด RNA ส่วนที่ต้องการ พลิกด้าน แล้วนำมาต่อกลับที่เดิม
    elif mode == 'beta':
        rev = rna[start:stop+1] # rev คือ RNA ส่วนที่ต้องการ
        rev.reverse()           # reverse rev 
        last = rna[stop+1:]     # เก็บค่าที่อยู่หลังตำแหน่งสุดท้ายของ rev
        del rna[start:]         # ทำการลบทุกตัวที่เริ่มจากตำแหน่ง start
        rna.extend(rev)         # นำส่วน rev มาต่อท้าย
        rna.extend(last)        # นำส่วนที่อยู่หลังตำแหน่งสุดท้ายของ rev มาต่อท้าย
        return rna
    # gamma คือสลับ RNA ในส่วนที่ต้องการเป็นคู่ ๆ
    elif mode == 'gamma':
        rev = rna[start:stop+1] # rev คือ RNA ส่วนที่ต้องการ
        m = []
        count = 0 # count ใช้นับค่าทีละ 1,2 ครั้ง
        # ถ้าความยาวของ rev เป็นเลขคู่ ในการสลับ rna เป็นคู่ๆ จะไม่เหลือตัวสุดท้ายของ rev ไว้ด้านหน้า
        if len(rev) % 2 == 0:
            for i in range(len(rev)):
                m.append(rev[count])
                count += 1
                if count % 2 == 0:
                    count = 0
                    m.reverse()
                    rev.extend(m)
                    del rev[0:2]
                    m = []
        # ถ้าความยาวของ rev เป็นเลขคี่ ในการสลับ rna เป็นคู่ๆ จะเหลือตัวสุดท้ายของ rev ไว้ด้านหน้า
        else:
            for i in range(len(rev)):
                m.append(rev[count])
                count += 1
                if count % 2 == 0:
                    count = 0
                    m.reverse()
                    rev.extend(m)
                    del rev[0:2]
                    m = []
            # ดังนั้นต้องย้ายตัวสุดท้ายที่อยู่ตำแหน่งแรก ไปไว้ตำแหน่งสุดท้ายเหมือนเดิม
            one = rev.pop(0)
            rev.append(one)
        last = rna[stop+1:]     # เก็บค่าที่อยู่หลังตำแหน่งสุดท้ายของ rev
        del rna[start:]         # ทำการลบทุกตัวที่เริ่มจากตำแหน่ง start
        rna.extend(rev)         # นำส่วน rev มาต่อท้าย
        rna.extend(last)        # นำส่วนที่อยู่หลังตำแหน่งสุดท้ายของ rev มาต่อท้าย
        return rna

def main():
    rna = ['A','G','C','T']
    print(rna)
    mode = input("mode: ")
    start = int(input("start: "))
    stop = int(input("stop: "))
    if mode == "":
        print(splice(rna,start,stop,mode='alpha'))
    else:
        mode = str(mode)
        print(splice(rna,start,stop,mode))
    
if __name__ == '__main__':
    main()
