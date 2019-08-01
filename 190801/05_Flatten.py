import sys

sys.stdin = open('05_input.txt', 'r')

def sorting_bubble(nums):
    for i in range(len(nums) - 1, 0, -1):
        for comp in range(i):
            if nums[comp] > nums[comp + 1]:
                nums[comp], nums[comp + 1] = nums[comp + 1], nums[comp]
    return nums

for test_case in range(1, 11):
    dump = int(input())
    heights = list(map(int, input().split()))

    heights_s = sorting_bubble(heights)

    for i in range(dump):
        if heights_s[-1] - heights_s[0] > 1:
            heights_s[-1] -= 1
            heights_s[0] += 1
            heights_s = sorting_bubble(heights)
        else:
            break
    print('#{} {}'.format(test_case, heights_s[-1]-heights_s[0]))


