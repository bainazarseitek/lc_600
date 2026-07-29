class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # price1, price2 = 0,0
        # for n in cost:
        #     temp = n + min(price1, price2)
        #     price1=price2
        #     price2=temp
        # return min(price2, price1)

        cost.append(0)
        for i in range(len(cost)-3, -1, -1):
            cost[i] +=min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])

        