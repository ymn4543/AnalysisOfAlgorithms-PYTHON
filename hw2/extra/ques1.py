import sys


def MYSTERY(left,right):
    if left == right:
        return 1, 1, 1
    else:
        m = (left + right) / 2
        (part1Lrun, part1Rrun, part1maxrun) = MYSTERY(left, m)
        (part2Lrun, part2Rrun, part2maxrun) = MYSTERY(m+1, right)
        if A[m] < A[m+1]:
            maxrun = max(part1maxrun, part2maxrun, part1Rrun+part2Lrun)
            if part1maxrun == m - left + 1:
                Lrun = part1maxrun + part2Lrun
            else:
                Lrun = part1Lrun
            if part2maxrun == right - m:
                Rrun = part2maxrun + part1Rrun
            else:
                Rrun = part2Rrun
        else:
            maxrun = max(part1maxrun, part2maxrun)
            Lrun = part1Lrun
            Rrun = part2Rrun
    return Lrun, Rrun, maxrun



def main():
    array = [4,23,2,4,55,32,84,20,37,12,17]
    l,r,m = MYSTERY(0,10)
    print(l,r,m)


if __name__ == '__main__':
    main()
