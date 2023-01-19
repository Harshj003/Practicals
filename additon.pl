% Code for addtion
sum(X,Y):-S is X+Y,
write(S).
/*In output we have to write sum(3,3)*/

/*Code for max of the number*/
max(X,Y,Z,M):-X>Y,X>Z,M is X.
max(X,Y,Z,M):-X<Y,Y>Z,M is Y.
max(X,Y,Z,M):-Z>Y,X<Z,M is Z.
max(X,Y,Z,M):-X<Y,X=Z,M is Y.
max(X,Y,Z,M):-Y=Z,X>Y,M is X.
max(X,Y,Z,M):-X=Y,X>Z,M is X.
max(X,Y,Z,M):-X=Z,Y<Z,M is Z.
max(X,Y,Z,M):-Y=Z,X<Z,M is Z.
max(X,Y,Z,M):-X=Y,X=Z,M is X.

%in output we have to write max(1,2,3,M)
