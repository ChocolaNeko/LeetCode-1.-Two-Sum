建立一個dict存放nums陣列中所有值，dict會將這些值對上一個index

從nums陣列中一一取出，並和target相減，若相減的值出現在dict內，則可以根據此值的index，找出在原本nums陣列中的index

取出的值，以及相減後的值所在的index，即為所需要的輸出

需注意，題目敘述中有提及，「不能使用同一個位置的值兩次」，也就是同一個index的值相加，剛好等於target的狀況是不允許的

              例如 nums = [3,2,4] , target = 6  
              
              若取index 0的值兩次，也就是 3 + 3 ，剛好等於6，但違反上述規則
              
              因此此題正確解應為 [1,2]，也就是index 1的2，和index 2的4相加，2 + 4 = 6 =target
              
參考資料：LeetCode (1) Two Sum (python)

https://medium.com/@havbgbg68/leetcode-1-two-sum-python-8d77c223abd3 
