class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        right = len(people) - 1
        left = 0
        boats = 0
        prev = 0
        while (left < right):
            if people[right] == limit:
                print("first if")
                right -= 1
                boats += 1
            elif people[right] + people[left] == limit:
                right -= 1
                left += 1
                boats += 1
            else: #people[right] + people[left] < limit [1,2,2,3,3]
                right -= 1
                left += 1
                boats += 1
        if left == right:
            return boats + 1
        return boats

        