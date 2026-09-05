class Solution {
    public int search(int[] nums, int target) {
       int left = 0; 
       int right = nums.length-1;
       int index = (right-left)/2;
       while (nums[index] != target) {
        System.out.println("Left: " + left);
        System.out.println("Right: " + left);
         if (right == left && nums[right] != target) {
            return -1;
        }
        if (right == left+1 && nums[right] != target && nums[left] != target) {
            return -1;
        }
        if (nums[index] > target)
        {right = index-1;}
        else if (nums[index] < target) {
            left = index + 1;
        }
       
        index = left + (right-left)/2;
       } 
       return index;
    }
}
