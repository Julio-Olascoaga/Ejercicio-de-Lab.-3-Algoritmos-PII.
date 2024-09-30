import time
import random

def merge_and_find_median(nums1, nums2):
    nums1.sort()
    nums2.sort()
    
    merged = []
    i, j = 0, 0
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    
    merged.extend(nums1[i:])
    merged.extend(nums2[j:])
    
    total_length = len(merged)
    if total_length % 2 == 0:
        median = (merged[total_length // 2 - 1] + merged[total_length // 2]) / 2
    else:
        median = merged[total_length // 2]
    
    return median

m = random.randint(0, 100)
n = random.randint(0, 100)

nums1 = [random.randint(-100, 100) for _ in range(m)]
nums2 = [random.randint(-100, 100) for _ in range(n)]

print(f"Lista 1: {nums1}")
print(f"Lista 2: {nums2}")

start_time = time.time()
median = merge_and_find_median(nums1, nums2)
end_time = time.time()

print(f"La mediana es: {median:.5f}")
print(f"Tiempo de ejecución: {end_time - start_time:.10f} segundos")
