class Solution:
    def secondHighest(self, s: str) -> int:
        largest=-1
        secondLargest=None

        for ch in s:
            if ch.isdigit():
                if int(ch)>largest:
                    secondLargest=largest
                    largest=int(ch)
                if int(ch)<largest and int(ch)>secondLargest :
                    secondLargest=int(ch)
        if secondLargest==None or largest==-1:
            return -1
        else:
            return  secondLargest