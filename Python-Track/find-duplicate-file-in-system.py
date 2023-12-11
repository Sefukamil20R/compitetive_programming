class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
            dis=defaultdict(list)
            for path in paths:
                allcontent=path.split()
                root=allcontent[0]
                for files in allcontent[1:]:
                        content=files.split(".txt")
                        filecontent=content[1]
                        file=content[0]
                        dis[filecontent].append((root,file))
                        
            
            res=[]
            for key,value in dis.items():
                if len(value) > 1:
                    tempo=[]
                    for path,file in value:
                        tempo.append(path + "/" + file+ ".txt")
                    res.append(tempo)
            return res

                
            
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            # dup=defaultdict(list)
            # for path in paths :
            #       file=path.split()
            # print(file)
            # root=file[0]
            # for s in range(1,len(file)):
            #     ssp=file[s].split(".txt")
            #     print(ssp)
            # res=[]
            # for files in range(1,len(file)):
            #     dup[ssp[1]].append(root,path[1])
            #      print(dup)
            
                
                 
                
                
           
                
                    
                    
                    
            
          

        