stock_prices = [7,1,5,3,6,4]

def maxProfit(prices) -> int:
        
        minPrice, profit = float('inf'), 0
        
        for price in prices :
            if minPrice > price :
                minPrice = price
            if profit < price - minPrice :
                profit = price - minPrice
                
        return profit

print(maxProfit(stock_prices))

# def maxProfit(prices) -> int:
#     if len(prices) == 0 :
#         return 0
        
#     minPrice = float('inf')
#     profit = 0
#     i = 0
#     bound = len(prices)

#     while i < bound :
#         if minPrice > prices[i] :
#             minPrice = prices[i]
#         if profit < prices[i] - minPrice :
#             profit = prices[i] - minPrice
#         i+=1
#     return profit
    

# def maxProfit (prices) :

#     current_stock = prices[0]
#     i = j = 0
#     bound = len(prices)

#     while i < bound :
#         if current_stock > prices [i] :
#             current_stock = prices[i]
#             j = i
#         i+=1 

#     highest_price = prices[j]

#     while j < bound :
#         if highest_price < prices[j] :
#             highest_price = prices[j]
#         j+=1

#     max_profit = highest_price - current_stock
#     return max_profit

# print(maxProfit(stock_prices))