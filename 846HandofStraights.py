class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand_dict = Counter(hand)

        for _ in range(len(hand) // groupSize):
            curr = min(hand_dict)

            for i in range(curr, curr+groupSize):
                hand_dict[i] -= 1

                if hand_dict[i] == 0:
                    del hand_dict[i]

                if hand_dict[i] < 0:
                    return False

            if len(hand_dict) == 0:
                break
        
        return True
        
