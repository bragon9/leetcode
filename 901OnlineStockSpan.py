class StockSpanner:
    
    def __init__(self):
        self.prev_node = None
        self.max = 0
        self.len = 0
        self.last_ans = 0
        
    def next(self, price: int) -> int:
        self.len += 1
        # price is same as the last price
        if self.prev_node:
            if self.prev_node.price == price:
                self.prev_node.add()
                self.last_ans += 1
                return self.last_ans
        # >= Max price
        if price >= self.max:
            self.last_ans = self.len 
            self.max = price
            new_node = Node(price, self.prev_node)
            self.prev_node = new_node
            return self.last_ans
        # Walk backwards to get the answer
        else:
            ptr_node = self.prev_node
            new_node = Node(price, self.prev_node)
            self.prev_node = new_node
            ans = 1
            while ptr_node:
                if ptr_node.price > price:
                    self.last_ans = ans
                    return ans
                ans += ptr_node.count
                ptr_node = ptr_node.previous
            self.last_ans = self.len
            return self.len
        
class Node:
    
    def __init__(self, price, prev_node):
        self.price = price
        self.count = 1
        self.previous = prev_node
        
    def add(self):
        self.count += 1
        
## List solution.

#     def __init__(self):
#         self.prices = []
#         self.max = 0
#         self.last_change = 0
#         self.last_answer = 0

#     def next(self, price: int) -> int:
#         self.prices.append(price)
#         if price >= self.max:
#             self.max = price
#             return len(self.prices)
#         if price == self.prices[-2]:
#             self.last_answer += 1
#             return self.last_answer
#         self.last_change = 0
#         ptr = 2
#         while ptr <= len(self.prices):
#             if self.prices[-ptr] > price:
#                 self.last_answer = ptr-1
#                 return ptr-1
#             ptr += 1
#         self.last_answer = ptr-1
#         return ptr-1
            
