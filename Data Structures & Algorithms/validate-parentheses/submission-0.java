class Solution {
    public boolean isValid(String s) {
    for (int i = 0; i < s.length()/2; i++) {
        System.out.println((int) s.charAt(i));
        System.out.println(s.charAt(s.length()-i-1) + 1);
        if (Math.abs(s.charAt(i) - s.charAt(s.length()-i-1)) >= 3) {
            return false;
        }
    }     
    return true;
    }
}
