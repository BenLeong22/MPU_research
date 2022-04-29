def qsort(L):



    return qsort([y for y in L[1:] if y <L[0]]) +L[:1]+qsort([y for y in L[1:] if y >=L[0]]) if len(L)>1 else L
list1 =[123,123,123,12,34,5674,86,453,4,864,53,756,453,4,231,5674,4,654,65,465,74,865,74564,5374,65,7453,4,6,74,56]
a =qsort(list1)

print(a)