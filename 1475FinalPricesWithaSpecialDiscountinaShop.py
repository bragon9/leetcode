class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        if len(prices) == 1:
            return prices
        # Indexes to check price reduction
        index_list = [0]
        for i in range(1, len(prices)):
            curr = prices[i]
            prev = prices[i-1]
            # If the price is lower than previous, check indexes to reduce
            if curr <= prev:
                for j in range(len(index_list)-1, -1, -1):
                    price_index = index_list[j]
                    compare_price = prices[price_index]
                    # Reduce and remove index
                    if compare_price >= curr:
                        prices[price_index] -= curr
                        index_list.pop(j)
            index_list.append(i)
        return prices
