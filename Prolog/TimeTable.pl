timetable(place1, place2, [depHour,depMin, arrHour,arrMin, flightNumber, listOfDays]).

timetable( london, edinburgh, [ 9,40,  10,50, ba4733, alldays]).
timetable( london, edinburgh, [ 19,40, 20,50, ba4833, [mo,tu,we,th,fr,su]]).
timetable( london, athens,	  [ 13,20, 16,20, ju201,  [fr]]).
timetable( london, athens,	  [ 13,20, 16,20, ju2l3,  [su]]).
timetable( london, zurich, 	  [ 9,10,  11,45, ba6l4,  alldays]).
timetable( london, zurich, 	  [ 14,45, 17,20, sr805,  alldays] ).
timetable( london, milan,	  [ 8,30,  11,20, ba5l0,  alldays]).
timetable( london, milan,	  [ 11,00, 13,50, a2459,  alldays]).
timetable( athens, zurich,	  [ 11,30, 12,40, ju322,  [tu,th] ]).
timetable( athens, london,	  [ 11,10, 12,20, yu200,  [fr]] ).
timetable( athens, london,	  [ 11,25, 12,20, yu212,  [sul]] ).
timetable( milan,  london,	  [ 9,10,  10,00, a2458,  alldays] ).
timetable( milan,  london,	  [ 12,20, 13,10, ba5lI,  alldays] ).
timetable( milan,  zurich,	  [ 9,25,  10,15, sr621,  alldays]).
timetable( milan,  zurich,	  [ 12,45, 13,35, sr623,  alldays ]).
timetable( zurich, athens,	  [ 13,30, 14,4,  yu323,  [tu,th]] ).
timetable( zurich, london,	  [ 9,00,  9,40,  ba6l3,  [mo,tu,we,th,fr,sa]] ).
timetable( zurich, london,	  [ 16,10, 16,55, sr806,  [mo,tu,we,th,fr,su]] ).
timetable( zurich, milan,	  [ 7,55,  8,45,  sr620,  alldays] ).

flight( Place1, Place2, Day, FlightNumber, DepHour,DepMin, ArrHour,ArrMin):-
	timetable(Place1, Place2, [DepHour,DepMin, ArrHour,ArrMin, FlightNumber, ListOfDays ]),
	(member(Day, ListOfDays); ListOfDays == alldays).

deptime(DepHour,DepMin, [X|Route]):-
	timetable(_, _, [DepHour,DepMin, _,_, X, _]), Route == Route.

transfer(ArrHour,ArrMin, DepHour,DepMin):-
	(ArrHour =:= DepHour, ArrMin =< DepMin - 40);
	(ArrHour < DepHour -1);
	(ArrHour =:= DepHour - 1, ArrMin =< DepMin + 60 - 40).

route(Place1, Place2, Day, [Route]):-
	flight(Place1, Place2, Day, Route, _,_, _,_).

route(Place1, Place2, Day, [R|Route]):-
	route(Connection, Place2, Day, Route), 
	flight(Place1, Connection, Day, R, _,_, ArrHour,ArrMin),
	deptime(DepHour,DepMin, Route),
	transfer(ArrHour,ArrMin, DepHour,DepMin).


