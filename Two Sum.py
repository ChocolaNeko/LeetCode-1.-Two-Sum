class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #建立一個dict存放nums內的值
        hash_table = {}
        for i in range(len(nums)):
            hash_table[nums[i]] = i
            
        for i in range(len(nums)):
            if target - nums[i] in hash_table:
                if hash_table[target-nums[i]] != i:  #確認是否有重複取同一個index的值
                    x = i
                    y = hash_table[target-nums[i]]
                    return [x,y]