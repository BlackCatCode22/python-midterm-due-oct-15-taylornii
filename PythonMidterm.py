
# PythonMidterm.py
# Name: Taylor Nii
# Class: CIT-95
# Date: 10-13-2023


import random
today = {"year": 2023, "month": 10, "day": 13}
today_str = f"{today['year']}-{today['month']}-{today['day']}"


class Animal:
    # Static class variable to keep track of the number of animals
    numOfAnimals = 0
    NUM_OF_HYENAS = 0
    NUM_OF_LIONS = 0
    NUM_OF_BEARS = 0
    NUM_OF_TIGERS = 0

    HABITAT_CAPACITY = 4

    hyena_habitat = []
    lion_habitat = []
    bear_habitat = []
    tiger_habitat = []
    zoo_habitat = []

    hyena_names = []
    lion_names = []
    bear_names = []
    tiger_names = []


    def __init__(self, species, name=None, age=99, birth_season="season", color="a color", weight="99 pounds",
                 originating_zoo="from where?", birthdate="", unique_id=None, sex=""):
        self.species = species
        self.name = name
        self.age = age
        self.birth_season = birth_season
        self.color = color
        self.weight = weight
        self.originating_zoo = originating_zoo
        self.birthdate = birthdate
        self.unique_id = unique_id
        self.sex = sex
        self.infostring = ""  # a string formatted for zooPopulation, will eventually be appended to correct animal habitat list

        # Increment the static variable when a new object is created
        # this is the only place this field's value should be changed
        Animal.numOfAnimals += 1


    def genBirthDay(self):
        """takes object season and age -> assigns randomly generated birthday to the object"""
        season_input = self.birth_season
        age_input = self.age

        def genMonth(season):
            """takes season -> returns randomly generated birth month within season;
            assumptions: no leap year, used meteorological season dates"""
            spring_mos = [3, 4, 5]  # spring (March 1 to May 31)
            summer_mos = [6, 7, 8]  # summer (June 1 to August 31)
            fall_mos = [9, 10, 11]  # fall (September 1 to November 30)
            winter_mos = [12, 1, 2]  # winter (December 1 to February 28 w/o leap year)

            if season == "spring":
                return random.choice(spring_mos)
            elif season == "summer":
                return random.choice(summer_mos)
            elif season == "fall":
                return random.choice(fall_mos)
            elif season == "winter":
                return random.choice(winter_mos)
            else:
                return 0

        def genDay(month):
            """takes randomly generated month -> returns randomly generated birth day"""
            months_31days = [1, 3, 5, 7, 8, 10, 12]  # jan, mar, may, jul, aug, oct, dec
            months_30days = [4, 6, 9, 11]  # apr, jun, sep, nov
            months_29days = [2]  # feb
            # return a random day from the assigned birth month
            if months_31days.count(month) == 1:
                return random.choice(range(1, 32))
            elif months_30days.count(month) == 1:
                return random.choice(range(1, 31))
            elif months_29days.count(month) == 1:
                return random.choice(range(1, 30))
            else:
                return 0

        def genYear(age, month, day):
            """takes age, birth month, birth day -> returns birth year"""
            if month == 0 or day == 0:
                return 0
            elif (month > today["month"]) or ((month == today["month"]) and (day > today["day"])):
                # haven't had birthday yet this year
                birth_year = today["year"] - age - 1
                return birth_year
            else:  # had birthday already this year
                return today["year"] - age  # age=2023-birth_year -> birth_year=2023-age

        def genBdayStr(season, age):
            """takes season & age -> returns string of generated birthday"""
            bmonth = genMonth(season)
            bday = genDay(bmonth)
            byear = str(genYear(age, bmonth, bday))
            bmonth = str(bmonth)
            bday = str(bday)
            if len(bmonth) < 2:
                bmonth = "0" + bmonth
            if len(bday) < 2:
                bday = "0" + bday
            if len(byear) < 2:
                byear = "000" + byear
            return f"{byear}-{bmonth}-{bday}"

        self.birthdate = genBdayStr(season_input, age_input)


    # TODO: figure out why we need separate child classes for hyena, lion, etc finish OOP vid
    # TODO: where do you apply 4 animal max cut-off?
    def genUniqueAnimalID(self):
        """generates unique id from animal object & assigns to member variable, unique_id"""
        animal_type = self.species
        if animal_type == "lion":
            Animal.NUM_OF_LIONS += 1
            self.secondpt = "0"+str(Animal.NUM_OF_LIONS)
        elif animal_type == "hyena":
            Animal.NUM_OF_HYENAS += 1
            self.secondpt = "0"+str(Animal.NUM_OF_HYENAS)
        elif animal_type == "bear":
            Animal.NUM_OF_BEARS += 1
            self.secondpt = "0" + str(Animal.NUM_OF_BEARS)
        elif animal_type == "tiger":
            Animal.NUM_OF_TIGERS += 1
            self.secondpt = "0" + str(Animal.NUM_OF_TIGERS)
        self.firstpt = self.species[0:2].title()
        unique_id = self.firstpt + self.secondpt

        self.unique_id = unique_id


    def genAnimalName(self):
        if self.species == "hyena":
            picked = random.choice(Animal.hyena_names)
            Animal.hyena_names.remove(picked)
            self.name = picked
        elif self.species == "lion":
            picked = random.choice(Animal.lion_names)
            Animal.lion_names.remove(picked)
            self.name = picked
        elif self.species == "bear":
            picked = random.choice(Animal.bear_names)
            Animal.bear_names.remove(picked)
            self.name = picked
        elif self.species == "tiger":
            picked = random.choice(Animal.tiger_names)
            Animal.tiger_names.remove(picked)
            self.name = picked
        self.infostring = f"{self.unique_id}; {self.name}; {self.age} years old; birth date {self.birthdate}; {self.color}; {self.sex}; {self.weight}; {self.originating_zoo}; arrived {today_str}"

    # Hy01; Banzai; 4 years old; birth date 2019-03-21; tan color; female; 70 pounds; from Friguia Park, Tunisia; arrived 2023-09-14

    def genZooHabitat(self):
        """should take in animal object, append them to as list if the list isn't full aka len of list is < 4"""
        """then should put those 4 lists into zoo_habitat list """
        # while len(Animal.hyena_habitat) + len(Animal.lion_habitat) + len(Animal.bear_habitat) + len(Animal.tiger_habitat) < 16:
            # Maybe add NUM_OF_ANIMALS += 1 here?? TODO
        if self.species == "hyena":
            if len(Animal.hyena_habitat) < Animal.HABITAT_CAPACITY:
                self.genBirthDay()
                self.genUniqueAnimalID()
                self.genAnimalName()
                Animal.hyena_habitat.append(self.infostring)
                # MAYBE add NUM_OF_HYENAS += 1 here??  TODO
        elif self.species == "lion":
            if len(Animal.lion_habitat) < Animal.HABITAT_CAPACITY:
                self.genBirthDay()
                self.genUniqueAnimalID()
                self.genAnimalName()
                Animal.lion_habitat.append(self.infostring)
        #         TODO
        elif self.species == "bear":
            if len(Animal.bear_habitat) < Animal.HABITAT_CAPACITY:
                self.genBirthDay()
                self.genUniqueAnimalID()
                self.genAnimalName()
                Animal.bear_habitat.append(self.infostring)
        #         TODO
        elif self.species == "tiger":
            if len(Animal.tiger_habitat) < Animal.HABITAT_CAPACITY:
                self.genBirthDay()
                self.genUniqueAnimalID()
                self.genAnimalName()
                Animal.tiger_habitat.append(self.infostring)
    #             TODO
    zoo_habitat = [hyena_habitat, lion_habitat, bear_habitat, tiger_habitat]


fileipath_animalNames = "/Users/taylornii/PycharmProjects/CIT95Programs/PythonMidterm/animalNames.txt"
fileipath_arrivingAnimals = "/Users/taylornii/PycharmProjects/CIT95Programs/PythonMidterm/arrivingAnimals.txt"
fileopath_outputFile = "/Users/taylornii/PycharmProjects/CIT95Programs/PythonMidterm/outputFile.txt"
try:
    with open(fileipath_animalNames, 'r') as animalNames:
        # Read lines from the input file
        a_lines = animalNames.readlines()
        b_lines = []
        for line in a_lines:
            line = line.strip()
            if line != "":
                b_lines.append(line)

        element_index = 0
        for element in b_lines:
            if element == "Hyena Names:":
                hyena_index = element_index + 1
            elif element == "Lion Names:":
                lion_index = element_index + 1
            elif element == "Bear Names:":
                bear_index = element_index + 1
            elif element == "Tiger Names:":
                tiger_index = element_index + 1
            element_index += 1
        Animal.hyena_names = b_lines[hyena_index].split(", ")
        Animal.lion_names = b_lines[lion_index].split(", ")
        Animal.bear_names = b_lines[bear_index].split(", ")
        Animal.tiger_names = b_lines[tiger_index].split(", ")


    with (open(fileipath_arrivingAnimals, 'r') as arrivingAnimals):
        # Read lines from the input file
        b1_lines = arrivingAnimals.readlines()
        b2_lines = []
        b3_lines = []

        for line in b1_lines:
            line = line.strip()
            b2_lines.append(line)

        for line in b2_lines:
            line = line.replace(" year old", ",").replace("male", "male,")
            line = line.replace("born in ", "").replace(", ", ";", 6)
            animalx_list = line.split(";")
            animalx = Animal(animalx_list[2])
            animalx.age = int(animalx_list[0])
            animalx.birth_season = animalx_list[3]
            animalx.color = animalx_list[4]
            animalx.weight = animalx_list[5]
            animalx.originating_zoo = animalx_list[6]
            animalx.sex = animalx_list[1]
            # age=99, birth_season="season", color="a color", weight="99 pounds", originating_zoo="from where?", birthdate="", unique_id=None, sex=""
            animalx.genZooHabitat()

        with open(fileopath_outputFile, "w") as outputFile:
            outputFile.write("Hyena Habitat:\n\n")
            for element in Animal.hyena_habitat:
                outputFile.write(element)
                outputFile.write("\n")
            outputFile.write("\nLion Habitat:\n\n")
            for element in Animal.lion_habitat:
                outputFile.write(element)
                outputFile.write("\n")
            outputFile.write("\nBear Habitat:\n\n")
            for element in Animal.bear_habitat:
                outputFile.write(element)
                outputFile.write("\n")
            outputFile.write("\nTiger Habitat:\n\n")
            for element in Animal.tiger_habitat:
                outputFile.write(element)
                outputFile.write("\n")
except Exception as e:
    print(f"An error occurred: {str(e)}")
