class Solution:
    def minOperations(self, nums: list[int]) -> int:

        ### testing solution by gemma-4-E4B-it-Q6_K, llama-b8763-bin-win-vulkan-x64

        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            
            # Optimization: check divisibility by 6k +/- 1
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True

        total_operations = 0
        
        for i in range(len(nums)):
            current_val = nums[i]
            
            if i % 2 == 0:
                # Even index: Target must be prime.
                target_val = current_val
                # Find the smallest prime >= current_val
                while not is_prime(target_val):
                    target_val += 1
                
                # Calculate cost
                operations = target_val - current_val
                total_operations += operations
                
            else:
                # Odd index: Target must be non-prime.
                target_val = current_val
                
                # Non-prime numbers are 1 or composite.
                # If the current value is non-prime, cost is 0.
                if not is_prime(target_val):
                    # target_val is already non-prime
                    pass
                else:
                    # Current value is prime, find the smallest non-prime >= current_val
                    target_val += 1
                    while is_prime(target_val):
                        target_val += 1
                
                # Calculate cost
                operations = target_val - current_val
                total_operations += operations


        return total_operations