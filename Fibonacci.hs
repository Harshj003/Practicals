[x*2 | x<- [1..10]]
[(x,y) | x<- [1,4] , y<- [2..5]]
[x*2 | x<- [1..10], x*2 >= 12]
zip ['a','b','c'][1,2,3,4]
take 10[1..20]
take 10(iterate(2*)1)
take 10(iterate (\x->(x+3)*2)1)
take 4(repeat 3)
replicate 3 5
take 10(cycle[1,2,3])
