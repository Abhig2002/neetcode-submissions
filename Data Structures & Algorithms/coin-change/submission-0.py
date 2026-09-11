class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def dfs(amount):
            if amount < 0:
                return -1

            if amount == 0:
                return 0

            if amount in memo:
                return memo[amount]

            min_coins = -1

            for coin in coins:
                curr = dfs(amount - coin)

                if curr != -1:
                    curr += 1  # count the coin we just used

                    if min_coins == -1 or curr < min_coins:
                        min_coins = curr

            memo[amount] = min_coins
            return min_coins

        return dfs(amount)