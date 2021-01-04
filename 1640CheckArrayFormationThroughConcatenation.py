class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        piece_dict = {}
        for piece in pieces:
            piece_dict[piece[0]] = piece[1:]
        ptr = 0
        while ptr < len(arr):
            num = arr[ptr]
            if num not in piece_dict:
                return False
            else:
                ptr += 1
                for num2 in piece_dict[num]:
                    num = arr[ptr]
                    if num == num2:
                        ptr += 1
                    else:
                        return False
        return True
                
