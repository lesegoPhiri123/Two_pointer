def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return "Array length is less than k"

    # Compute sum of first window of size k
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide the window: subtract the element going out and add the element coming in
    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

arr = [1, 2, 5, 4, 6, 3]
k = 3
print(max_sum_subarray(arr, k))
