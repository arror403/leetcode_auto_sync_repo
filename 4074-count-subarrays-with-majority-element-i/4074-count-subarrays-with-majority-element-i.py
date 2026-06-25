class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        L = len(nums)
        prefix_sums = [0]*(L+1)
        current_sum = 0
        for i in range(L):
            current_sum += (1 if nums[i]==target else -1)
            prefix_sums[i+1] = current_sum

        def merge_sort_and_count(arr, low, high):
            if low >= high: return 0
            mid = (low+high)//2
            count = merge_sort_and_count(arr, low, mid)
            count += merge_sort_and_count(arr, mid + 1, high)
            l, r = low, mid + 1
            while l<=mid and r<=high:
                if arr[l]<arr[r]:
                    count += (high-r+1)
                    l+=1
                else:
                    r+=1

            arr[low:high+1] = sorted(arr[low:high+1])
            return count

        return merge_sort_and_count(prefix_sums, 0, L)