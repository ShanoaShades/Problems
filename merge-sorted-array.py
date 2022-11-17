# Variables, we have two lists of numbers.
nums1 = [3, 7, 9, 6, 15, 64, 42]
nums2 = [8, 13, 66, 4, 33, 99, 11]

# The function below will merge these two lists and sort them.
def merge_sort(list1, list2):
    list = list1 + list2
    list.sort()
    return list

# Finally, we print the two lists and the merged sorted one to see the difference.
print("List 1 -> ", nums1, "\nList 2 -> ", nums2, "\nMerged and sorted list -> ", merge_sort(nums1, nums2))