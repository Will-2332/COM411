def gang():
    print("Loading gang...")
    friends=[]
    friends.append("Scooby Doo")
    friends.append("Shaggy Rogers")
    friends.append("Fred Jones")
    friends.append("Daphne Blake")
    friends.append("Velma Dinkley")
    for i in range (len(friends)):
        print(friends[i])
    print("...Done!")
    return friends
    
def phrases(friends):
    quotes={}
    for i in range (len(friends)):
        print("What does",friends[i],"say?")
        quote=input()
        quotes[friends[i]] = quote
    return quotes
    
def save(quotes):
    with open("quotes.txt", "wb") as text:
        text.write(str(quotes))
        
save(phrases(gang()))