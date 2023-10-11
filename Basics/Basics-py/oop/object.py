class country:
    def __init__(state,continent,name,sq):
        state.continent = continent
        # continent = input()
        state.name = name
        # name = input()
        state.sq = sq
        # sq = input()
    def visit(state):
        print('Welcome to',state.name)
    def goTo(state):
        print('i want to visit',state.continent)

continent = input('Enter the continent')
name = input('Enter the country')
sq = print('Enter the sq feet')

myCountry = country(continent,name,sq)

print(myCountry.continent)
print(myCountry.name)
print(myCountry.sq)

myCountry.goTo()

myCountry.visit()