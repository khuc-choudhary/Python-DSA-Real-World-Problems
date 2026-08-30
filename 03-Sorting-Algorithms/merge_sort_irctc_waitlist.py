"""3) Merge Sort — The IRCTC Waitlist Merger
IRCTC has two separately sorted waitlists — one from its mobile app, one from railway counters.
To produce a final unified waitlist, they don't re-sort from scratch.
They merge both sorted lists in one pass — compare the front of each list, pick the smaller token,
 and advance.
This is exactly merge sort's merge step."""
list1 = [2, 5, 8, 12]
list2 = [1, 4, 9, 10]

i = j = 0
merged = []

while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        merged.append(list1[i])
        i += 1
    else:
        merged.append(list2[j])
        j += 1

merged.extend(list1[i:])
merged.extend(list2[j:])

print(merged)
