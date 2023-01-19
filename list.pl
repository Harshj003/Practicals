% Create a list containing all integers within a given range.
range(I,I,[I]).
range(I,K,[I|L]) :- I < K, I1 is I + 1, range(I1,K,L).
%in output we have to write range(2,8,L).

%To count no of elements in a list.
size([],0).
size([_|T],N):- size(T,N1), N is N1+1.
%in output we have to write size([1,2,3,4,5,6],N).

%To check if an element is a member of the list
onTheGuestList(Name,[Name|_RestOfTheList]).
onTheGuestList(Name,[_FirstPerson|RestofTheList])
onTheGuestList(Name,RestofTheList).
%in output we have to write onTheGuestList(robin,[kartik,anushka,goku]).

%To append a list at the back of an existing list
append1([],L1,L2).
append1([H|T],L2,[H|L3]):- append1(T,L2,L3).
%in output we have to write append1([1,2,3,4,5],[4,5,6,7,8]).
