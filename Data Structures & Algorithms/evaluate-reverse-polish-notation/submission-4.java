class Solution {
    public int evalRPN(String[] tokens) {
        String[] operators = {"+", "-", "*", "/"};
        int total = Integer.parseInt(tokens[0]);
        Stack<Integer> stack = new Stack<>();
        for (int i = 1; i < tokens.length; i++) {
            String s = tokens[i];
            if (Arrays.asList(operators).contains(s)) {
                int index = Arrays.asList(operators).indexOf(s);
                if (!stack.isEmpty()) {
                    if (index == 0) total += stack.pop();
                    else if (index == 1) total -= stack.pop();
                    else if (index == 2) total *= stack.pop();
                    else {
                        total = (int)Math.ceil(total/=(double)stack.pop());
                    }
                    System.out.println(total);
                    
                }
            }
            else {
                stack.push(Integer.parseInt(s));
            }
        }
        return total;

    }
}
