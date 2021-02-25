# city country

def city_country(city_name, country_name):
    city_country_name = city_name + ' '+country_name
    return city_country_name.title()

print(city_country('beijing','china'))


def city_country(city_name, country_name, population=''):
    city_country_name = city_name + ' ' + country_name + ' -population ' + population
    if population:
        return city_country_name.title()
    else:
        city_country_name = city_name + ' ' + country_name
        return city_country_name.title()

print(city_country('beijing','china','100000'))



