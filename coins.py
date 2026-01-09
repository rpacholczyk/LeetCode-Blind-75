class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize dimensions: number of coin types and target amount
        num_coins = len(coins)
      
        # Create 2D DP table
        # dp[i][j] represents minimum coins needed to make amount j using first i coin types
        dp = [[float('inf')] * (amount + 1) for _ in range(num_coins + 1)]
      
        # Base case: 0 coins needed to make amount 0
        dp[0][0] = 0
      
        # Fill the DP table
        for coin_idx in range(1, num_coins + 1):
            current_coin_value = coins[coin_idx - 1]
          
            for current_amount in range(amount + 1):
                # Option 1: Don't use the current coin type
                dp[coin_idx][current_amount] = dp[coin_idx - 1][current_amount]
              
                # Option 2: Use the current coin if possible
                if current_amount >= current_coin_value:
                    # Compare with using one more of the current coin
                    dp[coin_idx][current_amount] = min(
                        dp[coin_idx][current_amount],
                        dp[coin_idx][current_amount - current_coin_value] + 1
                    )
      
        # Return result: -1 if impossible, otherwise the minimum number of coins
        return -1 if dp[num_coins][amount] == float('inf') else dp[num_coins][amount]
        
        
