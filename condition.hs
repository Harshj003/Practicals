-- To compile write ghc -o FileName FileName.hs
-- Conditional Expression
main = do
  let var = 23
  if var `rem2`==0
    then putStrLn "Number is Even"
  else putStrLn "Number is Odd"
 
--Guarded Equations
fact::Integer->Integer
fact n|n ==0=1
  |n/=0=n*fact(n-1)
main=do
  putStrLn "The Factorial of 5 is: "
  print(fact 5)
  
--Patern Matching
fact::Int->Int
fact 0=1
fact n = n*fact(n-1)
main = do
  putStrLn "The Factorial of 2 is: "
  print(fact 2)
