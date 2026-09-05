class MinStack {
    private int[] stack;
    private int currIndex;
    private int capacity;
    public MinStack() {
        stack = new int[10];
        currIndex = 0;
        capacity = 10;
    }
    
    public void push(int val) {
    if (currIndex < capacity) {
    stack[currIndex] = val;
    currIndex++;
    } else {
        int[] newStack = new int[capacity*2];
        capacity *=2;
        for (int i = 0; i <= currIndex; i++) {
            newStack[i] = stack[i];
        }
        newStack[currIndex] = val;
        currIndex++;
        stack = newStack;
    }
    
    }
    
    public void pop() {
        currIndex--;
    }
    
    public int top() {
        return stack[currIndex - 1];
    }
    
    public int getMin() {
        int min = stack[0];
        for (int i = 0; i < currIndex; i++) {
            if (stack[i] < min) min = stack[i];
        }
        return min;
    }
}
