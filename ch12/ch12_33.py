from typing import List

class Solution:
    def letterCom(self, digits:str) -> List[str]: #digits="23"
        def dfs(index,path): # dfs(0,"")
            # 끝까지 탐색(찾아낸조합길이=digits길이)하면 백트래킹
            if len(path) == len(digits):
                result.append(path)
                return
            
            #입력값 자릿수 단위 반복
            for i in range(index,len(digits)): #"234"이라면 i=2>3>4
                #숫자에 해당하는 모든 문자열 반복
                for j in dic[digits[i]]: #i=2(abc)라면 a>b>c
                    dfs(i+1,path+j)
        if not digits:
            return []
        
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        dfs(0, "")

        return result

print(Solution().letterCom('24'))
# ['ag', 'ah', 'ai', 'bg', 'bh', 'bi', 'cg', 'ch', 'ci'] 