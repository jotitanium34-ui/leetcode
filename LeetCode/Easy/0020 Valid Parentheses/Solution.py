class Solution(object):
    def isValid(self, s):
        st=[]
        d={"(":")","{":"}","[":"]"}
        for i in s:
            if i in d.keys():
                st.append(i)
            else:
                if st==[]:
                    return False
                else:
                    if d[st[-1]]==i:
                        st.pop()
                    else:
                        return False
        if st==[]:
            return True
        else:
            return False



            


        
       