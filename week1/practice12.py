Counties={
        "Indai" :{"capital" : "New Delhi","population ": 1442195981},
        "Japan" :{"capital" : "Tokyo" , "population" : 14094034}	,
        "Russia" :{"capital" :"Moscow" , "population"	 : 13104177}	
}
print("dictionary country :- ")
print(Counties)
access=Counties["Japan"]["capital"]
print("print the capital of one country :- ",access)
print("Update the population of Russia country :-")
Counties["Russia"]["population"]=144713314
print(Counties)
