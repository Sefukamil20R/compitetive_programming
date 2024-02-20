class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x : x[1] - x[0], reverse = True)
        print(tasks)
        task = tasks[0][1]
        res = task
        for s in tasks:
            if task >= s[1]:
                task -= s[0]
            else:
                res += s[1] - task
                task += s[1] - task 
               
                task -= s[0]
        return res
            





        