
# Linear Search for deletion
# Returns the array to save list
def delete_task(target, arr):
    for i, task in enumerate(arr):
        if task["id"] == target:
            arr.pop(i)
            return arr
     # Only prints False once if no match found
    print(False)
    return arr
