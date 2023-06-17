class MiniMaxAgent:
    def __init__(self):
        # Define the locations and connections in Ethiopia
        self.ethiopia_coffee_location = {
            "Addis Ababa": {"Ambo", "Buta Jirra", "Adama"},
            "Ambo": {"Gedo", "Nekemte"},
            "Buta Jirra": {"Worabe", "Wolkite"},
            "Adama": {"Dire Dawa", "Mojo"},
            "Gedo": {"Shambu", "Fincha"},
            "Nekemte": {"Gimbi", "Limu"},
            "Worabe": {"Hosana", "Durame"},
            "Wolkite": {"Benchi Naji", "Tepi"},
            "Mojo": {"Dilla", "Kaffa"},
            "Dire Dawa": {"Chiro", "Harar"}
        }

        # Define the utility values for each terminal coffee location
        self.terminal_utilities = ["Shambu", "Fincha", "Gimbi", "Limu", "Hosana", "Durame", "Benchi Naji", "Tepi", "Kaffa", "Dilla", "Chiro", "Harar"]
        self.terminals = [4, 5, 8, 8, 6, 5, 5, 6, 7, 9, 6, 10]

        # Define the connections between coffee locations
        self.graph = {
            "Fincha": "Gedo",
            "Limu": "Nekemte",
            "Hosana": "Worabe",
            "Tepi": "Wolkite",
            "Dilla": "Mojo",
            "Harar": "Dire Dawa"
        }

        # Define additional connections for the second level of choices
        self.graph_1 = {
            "Gedo": "Ambo",
            "Worabe": "Buta Jirra",
            "Mojo": "Adama"
        }

    def minimax_search(self):
        # First level of choices
        is_max = True
        choosen_cities = []
        terminals_1 = []

        for i in range(0, len(self.terminals), 2):
            if self.terminals[i] > self.terminals[i + 1]:
                choosen_cities.append(self.terminal_utilities[i])
            else:
                choosen_cities.append(self.terminal_utilities[i + 1])
            terminals_1.append(max(self.terminals[i], self.terminals[i + 1]))

        # Second level of choices
        choosen_cities_2 = []
        terminals_2 = []
        is_max = False

        for i in range(0, len(terminals_1), 2):
            if terminals_1[i] > terminals_1[i + 1]:
                choosen_cities_2.append(self.graph[choosen_cities[i + 1]])
            else:
                choosen_cities_2.append(self.graph[choosen_cities[i]])
            terminals_2.append(min(terminals_1[i], terminals_1[i + 1]))

        # Determine the best city from the second level choices
        max_city_ind = 0
        if terminals_2[1] > terminals_2[max_city_ind]:
            max_city_ind = 1
        if terminals_2[2] > terminals_2[max_city_ind]:
            max_city_ind = 2

        # Retrieve the first chosen city and the best second city
        first_chosen_city = self.graph_1[choosen_cities_2[max_city_ind]]
        second_city = choosen_cities_2[max_city_ind]

        # Find the possible third city based on the second city's options
        third_city_options = self.ethiopia_coffee_location[second_city]
        third_city = None

        for c in third_city_options:
            if c in self.graph:
                third_city = c

        return first_chosen_city, second_city, third_city


# Usage example:
agent = MiniMaxAgent()
first_city, second_city, third_city = agent.minimax_search()
print(first_city)
print(second_city)
print(third_city)
