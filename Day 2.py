class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
        if k == 0:
            return [0] * n

        result = [0] * n
        code_extended = code * 2

        if k > 0:
            for i in range(n):
                result[i] = sum(code_extended[i + 1:i + 1 + k])
        else:  
            k = abs(k)
            for i in range(n):
                result[i] = sum(code_extended[i + n - k:i + n])

        return result
