#Function to return the ceil of given number in BST.

class Solution:
    def findCeil(self,root, inp):
        # code here
        ans = None
        while root:
            if root.key == inp:
                return root.key
            elif root.key > inp:
                ans = root
                root = root.left
            else:
                root = root.right
        
        return -1 if not ans else ans.key

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.key = val
        self.left = None

# Function to Build Tree  

def buildTree(s):
        #Corner Case
        if(len(s)==0 or s[0]=="N"):           
            return None
            
        # Creating list of strings from input 
        # string after spliting by space
        ip=list(map(str,s.split()))
        
        # Create the root of the tree
        root=Node(int(ip[0]))                     
        size=0
        q=deque()
        
        # Push the root to the queue
        q.append(root)                            
        size=size+1 
        
        # Starting from the second element
        i=1                                       
        while(size>0 and i<len(ip)):
            # Get and remove the front of the queue
            currNode=q[0]
            q.popleft()
            size=size-1
            
            # Get the current node's value from the string
            currVal=ip[i]
            
            # If the left child is not null
            if(currVal!="N"):
                
                # Create the left child for the current node
                currNode.left=Node(int(currVal))
                
                # Push it to the queue
                q.append(currNode.left)
                size=size+1
            # For the right child
            i=i+1
            if(i>=len(ip)):
                break
            currVal=ip[i]
            
            # If the right child is not null
            if(currVal!="N"):
                
                # Create the right child for the current node
                currNode.right=Node(int(currVal))
                
                # Push it to the queue
                q.append(currNode.right)
                size=size+1
            i=i+1
        return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        n=int(input())
        root=buildTree(s)
        obj=Solution()
        print(obj.findCeil(root,n))
# } Driver Code Ends
