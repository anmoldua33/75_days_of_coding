class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        dic = dict()
        ans = []
        
        for trans in transactions:
            t = trans.split(',')
            if t[0] in dic:
                dic[t[0]] += t[1:],
            else:
                dic[t[0]] = t[1:],
        
        for trans in transactions:
            t = trans.split(',')
            if int(t[2]) > 1000:
                ans += trans,
                continue
            if t[0] in dic:
                for i in dic[t[0]]:
                    if i[-1] != t[-1] and abs(int(i[0]) - int(t[1])) <= 60:
                        ans += trans,
                        break
        return ans
