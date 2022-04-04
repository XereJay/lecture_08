import json



def main():
    with open("new_criminals.json", "r") as data_file:
        new_criminals = json.load(data_file)
    print(type(new_criminals))
    names = ["Pablo Escobar", "Joaqim Guzmán", "Ismael Garcia"]
    production = [(138, 164, 151), (125, 113, 113), (52, 50, 63)]
    most_wanted = dict(zip(names, production))
    # print(most_wanted)

    def criminals(present_criminals, new_criminals):
        #print(present_criminals)
        #print(new_criminals)
        for name in new_criminals.keys():
            if name in present_criminals:
                most_wanted[name] = new_criminals[name]
            else:
                most_wanted[name] = new_criminals[name]
        #print(most_wanted)

    criminals(most_wanted, new_criminals)
    print(most_wanted)
    origin = {
    "Mexico": {"Manuel Noriega", "Pablo Escobar", "Joaqim Guzmán", "Ismael Garcia"},
    "Columbia": {"Rick Ross", "William Jardine"}}



if __name__ == "__main__":
    main()

