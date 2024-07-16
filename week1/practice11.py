print("\n")
dic={
     "Mumbai"	: 12442373 ,	
      "Delhi"	: 11034555	,
     "Bangalore"	: 8443675	,
     "Hyderabad"	: 6993262
}
print("Dictionary :- ",dic)
Get=dic.get("Mumbai")
print("Get of specific city 'Mumbai' :-",Get)
dic.pop("Delhi")
print("Pop in dictionary :- ",dic)
