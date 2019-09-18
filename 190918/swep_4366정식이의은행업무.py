import sys

sys.stdin = open('input.txt', 'r')

def Comp(bNum, tNum):
    bLen = len(bNum)
    tLen = len(tNum)

    for bit in range(bLen):
        if bNum[bit] == '1':
            bTmp = '0b' + bNum[0:bit] + '0' + bNum[bit + 1:len(bNum)]
        else:
            bTmp = '0b' + bNum[0:bit] + '1' + bNum[bit + 1:len(bNum)]
        dTmp = int(bTmp, 2)

        for tri in range(tLen):
            for i in range(3):
                tTmp = tNum[0:tri] + str(i) + tNum[tri + 1:len(tNum)]
                dTmp2 = 0
                for j in range(tLen):
                    dTmp2 += 3**(tLen - j - 1) * int(tTmp[j])

                if dTmp == dTmp2:
                    return dTmp

for tc in range(1, int(input()) + 1):
    bNum = input()
    tNum = input()

    res = Comp(bNum, tNum)
    print(res)
