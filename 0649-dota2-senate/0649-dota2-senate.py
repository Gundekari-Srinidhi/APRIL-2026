class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d={"R":0,"D":0}
        s=list(senate)
        for i in senate:
            d[i]+=1     
        rban = 0
        dban = 0
        while d["R"] > 0 and d["D"] > 0:
            
            new_s = []
            for ch in s:
                if ch == "R":
                    if rban > 0:
                        rban -= 1
                        d["R"] -= 1
                    else:
                        dban += 1
                        new_s.append("R")
                else:
                    if dban > 0:
                        dban -= 1
                        d["D"] -= 1
                    else:
                        rban += 1
                        new_s.append("D")
            s = new_s
        if d["R"] > 0:
            return "Radiant"
        else:
            return "Dire"
