let a = [1,2,3,4]
tail a
head a
tail (tail(tail(a)))
5:[]
1:5:[]
6:[1,5]
init a
last a
reverse a
safetail xs = if null xs then[] else tail xs
safetail [1,2,3,4,5,6]
safetail []
tail[1,2,3,4,5,6]
