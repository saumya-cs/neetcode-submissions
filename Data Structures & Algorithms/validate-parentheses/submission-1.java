class Solution {
    public boolean isValid(String s) {
    Stack <Character> stack = new Stack<Character>();
    Map<Character, Character> map = new HashMap<>();
    map.put(')', '(');
    map.put('}', '{');
    map.put(']', '[');     
    
    for (char c: s.toCharArray()) {
        if (map.containsKey(c)) {
        if (!stack.isEmpty() && (stack.peek() == map.get(c))) {
            stack.pop();
        } else {
            return false;
        }
        }
        else {
            stack.push(c);
        }
    }
    if (stack.isEmpty()) {return true;} else {
        return false;
    }
    }
}
