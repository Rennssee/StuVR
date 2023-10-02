def game(terra, power):
    for enrg_list in terra:  # створення списку enrg_list та перебір у списку terra
        for energy in enrg_list:  #
            if energy <= power:
                power += energy
            else:
                break
    return power
