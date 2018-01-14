from sklearn.preprocessing import normalize

test = [[7.5,8.4,9,8.3,8.7,9.1,9.4,9.2,9.5]]
test_norm = normalize(test,norm='max')
print "Solution 1 -- But I think it is not correct"
print test[0]
print test_norm[0][8]