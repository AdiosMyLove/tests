import sys

def min_moves(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    moves = sum(abs(num - median) for num in nums)
    return moves

def main():
    filename = sys.argv[1]
    
    with open(filename, 'r') as file:
        nums = [int(line.strip()) for line in file.readlines()]
    
    result = min_moves(nums)
    print(result)

if __name__ == "__main__":
    main()