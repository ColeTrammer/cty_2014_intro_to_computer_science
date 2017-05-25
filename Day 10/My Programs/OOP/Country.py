class Country:
    """  Allowing a new instance of the Country class """
    def __init__(self, name, population, size, education, average_temp):
        self.name = name
        self.population = population
        self.size = size
        self.education = education
        self.average_temp = average_temp

    """  The method to print the Country object """
    def __str__(self):
        result = ""
        result += "Country:\n"
        result += "The name of the country is " + self.name + ".\n"
        result += "The population of the country is " + str(self.population) + ".\n"
        result += "The size of the country is " + str(self.size) + " square miles.\n"
        result += "The education of the country is " + str(self.education) + " percent.\n"
        result += "The average temperature of the country is " + str(self.average_temp) + ".\n"
        return result

    """
    @a country1 to war
    @b country2 to war

    prints the winner of the war
    """
    def war(a, b):
        if a.population > b.population:
            print "Country 1 wins!"
        elif a.population < b.population:
            print "Country 2 wins!"
        else:
            if a.education > b.education:
                print "Country 1 wins!"
            elif a.education < b.education:
                print "Country 2 wins!"
            else:
                print "Tie!"

    """
    @sz  increase Country by size
    """
    def conquest(self, sz):
        self.size += sz

    """
    @tmep increase Country by temp
    """
    def global_warming(self, temp):
        self.average_temp += temp

    """
    @a  country 1 to race
    @b  country 2 to race

    races to the stars by finding the highest intelligence
    """
    def race_to_stars(a, b):
        if a.education > b.education:
            print "Country1 reaches the stars!"
        elif a.education < b.education:
            print "Country2 reaches the stars!"
        else:
            print "They worked together"

    """
    @generations  the number of times to increase the population

    increase the pop * 2
    """
    def pop_growth(self, generations):
        for i in range(generations):
            self.population *= 2


def main():
    a = Country("USA", 1, 145, 99, 101)
    b = Country("China", 1, 154, 67, 56)
    Country.war(a, b)
    a.conquest(1234)
    b.global_warming(101)
    Country.race_to_stars(a, b)
    a.pop_growth(45)
    print a
    print b


if __name__ == "__main__":
    main()