# build skyscapper = input("men")
build = input("number of skyscrpper : ")

men = int(build) * int(950)
metal = int(build) * 72500
wood = int(build)*70000
cement = int(build) * 2950000

men = int(men)
cement = int(cement)
metal = int(metal)
wood = int(wood)
total = (men + cement + metal + wood)

# p_men

men = f'men = {men}'
metal = f' metal = {metal}'
wood = f'wood = {wood}'
cement = f'cement = {cement}'



print(men,metal, wood, cement)
print(total)
print(type(wood))