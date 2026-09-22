class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        last = 1
        tmp_sum = 0

        for arrival, time in customers:
            
            if arrival > last:
                tmp_sum += time
                last = arrival+time
            else:
                value = (time+last-arrival)
                tmp_sum += value
                last += time
            
        return tmp_sum/len(customers)
