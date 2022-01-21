def city(city,county,population=''):
    if population:
        long_sen=f'{city},{county}-{population}'
    else:
        long_sen=f'{city},{county}'
    return long_sen