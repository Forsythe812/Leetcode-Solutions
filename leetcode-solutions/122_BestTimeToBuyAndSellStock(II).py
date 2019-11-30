stock_prices = [7,1,5,3,6,4]
stock_prices2 = [1,2,3,4,5]

def maxProfit(prices):
#Always sell everytime there is a profit
    profit = 0
    for i in range(1,len(prices)):
        if prices[i] > prices[i-1] :
            profit += prices[i] - prices[i-1]
    return profit

# def maxProfit(prices):
# #Always sell everytime there is a profit
#     if not prices :
#             return 0

#     profit = 0   
#     for i in range(0,len(prices)) :
#         for j in range (i+1,len(prices)) :
#             if prices[i] < prices[j] :
#                 profit += prices[j] - prices[i]
#             i+=1
#         return profit
# print(maxProfit(stock_prices2))

