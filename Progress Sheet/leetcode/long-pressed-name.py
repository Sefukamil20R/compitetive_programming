class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i , j = 0 , 0
        while  j < len(typed):
        # the reason we are itarting only on the typed is we are checking 
        # if every charcter in our name are existe on typed 
            if  i < len(name) and name[i] == typed[j]:
                # if they are equal it means it is valid we 
                # can get that character of name from type hence we 
                # have to increment both of our pointer
                i += 1
                j += 1
            elif j > 0 and typed[j-1] == typed[j]:
                  j += 1
                #   if the previous and current character of j which in 
                # in typed are equal which means this are the longpressed 
                # character in name so we will increment only our j
            else:
                return False
                # if we dont enter on if or elif condtion or doesnt 
                #met the above codtion else we will return False
        return i == len(name)
        # but if we dont enter in our else condion meaning that we dont  
        #return False until our loop fifnishes we will  i == len(name)
        # coz as our return type is bool if i == len(name) it will return 
        # true if i is equal with len(name) it means i reach to end of len of name 
        # we've matched all characters in name with their corresponding 
        # characters in typed, in the correct order.
           
        