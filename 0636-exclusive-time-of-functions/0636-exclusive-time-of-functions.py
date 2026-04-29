class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev_time = 0
        
        for log in logs:
            f_id_str, T, timestamp_str = log.split(':')
            f_id, timestamp = int(f_id_str), int(timestamp_str)
            
            if T == "start":
                if stack:
                    res[stack[-1]] += timestamp - prev_time
                stack.append(f_id)
                prev_time = timestamp
            else:
                res[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1
                

        return res