class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
            myhash=defaultdict(list)
            
            for win,los in matches:
                if win not in myhash:
                    myhash[win]=[1,0]
                else:
                    myhash[win][0]+=1
                if los not in myhash:
                    myhash[los]=[0,1]
                else:
                    myhash[los][1]+=1
            ans1=[]
            ans2=[]
            for key,value in myhash.items():
                if value[1]==0:
                        ans1.append(key)
                if  value[1]==1:
                        ans2.append(key)
            ans1.sort()
            ans2.sort()
            return [ans1,ans2]
            
                    
          