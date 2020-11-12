def lowest_Common_Ancestor(t,n,m):
#function to search for given elements. Returns None if element is not found.
    def search(t,n):
        if (t):
            if (t.data<n):
                return search(t.right,n)
            elif (t.data>n):
                return search(t.left,n)
            else:
                return True
        return False
#function to find LCA of elements.
#'t' is tree, 'n' & 'm' are elements.
    def lca(t,n,m):
        if (t.data<n and t.data<m):
            return lca(t.right,n,m)
        elif (t.data>n and t.data>m):
            return lca(t.left,n,m)
        return t

#check whether the given elements are present or not.
    if (search(t,n) and search(t,m)):
        a=lca(t,n,m)
        return a
    else:
        return None
