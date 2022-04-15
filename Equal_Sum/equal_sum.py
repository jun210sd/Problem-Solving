#Python program to implement
# the above approach
 
# Function to find indices of array elements
# whose removal makes the sum of odd and
# even indexed array elements equal
def removeIndicesToMakeSumEqual(arr):
   
    # Stores size of array
    N = len(arr);
 
    # Store prefix sum of odd
    # index array elements
    odd = [0] * N;
 
    # Store prefix sum of even
    # index array elements
    even = [0] * N;
 
    # Update even[0]
    even[0] = arr[0];
 
    # Traverse the given array
    for i in range(1, N):
 
        # Update odd[i]
        odd[i] = odd[i - 1];
 
        # Update even[i]
        even[i] = even[i - 1];
 
        # If the current index
        # is an even number
        if (i % 2 == 0):
 
            # Update even[i]
            even[i] += arr[i];
 
        # If the current index
        # is an odd number
        else:
 
            # Update odd[i]
            odd[i] += arr[i];
 
    # Check if at least one
    # index found or not that
    # satisfies the condition
    find = False;
 
    # Store odd indices sum by
    # removing 0-th index
    p = odd[N - 1];
 
    # Store even indices sum by
    # removing 0-th index
    q = even[N - 1] - arr[0];
 
    # If p and q are equal
    if (p == q):
        print("0 ");
        find = True;
 
    # Traverse the array arr
    for i in range(1, N):
 
        # # If i is an even number
        # if (i % 2 == 0):
 
        #     # Update p by removing
        #     # the i-th element
        #     #p = even[N - 1] - even[i - 1] - arr[i] + odd[i - 1];
        #     p = even[N - 1] - even[i] + odd[i - 1];
 
        #     # Update q by removing
        #     # the i-th element
        #     q = odd[N - 1] - odd[i - 1] + even[i - 1];
        # else:
 
        # Update q by removing
        # the i-th element
        q = odd[N - 1] - odd[i] + even[i - 1];

        # Update p by removing
        # the i-th element
        p = even[N - 1] - even[i - 1] + odd[i - 1];
 
        # If odd index values sum is equal
        # to even index values sum
        if (p == q):
           
            # Set the find variable
            find = True;
 
            # Print the current index
            print(i, end = "");
 
    # If no index found
    if (find == False):
       
        # Print not possible
        print(-1);
 
# Driver Code
if __name__ == '__main__':
    arr = [0,3,5,7,8,2,4,6];
 
    removeIndicesToMakeSumEqual(arr);
    