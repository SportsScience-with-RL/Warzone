weapons = {"AX-50": 0, "PKM": 1, "M4": 2}
bullets = {"AX-50": 10, "PKM": 100, "M4": 30}
ammo = {"AX-50": 40, "PKM": 250, "M4": 150}
bullets_fired = {"AX-50": 1, "PKM": 10, "M4": 3}

select_weapons = input("Choose a weapon between AX-50, PKM and M4: ")
init_charger = bullets[select_weapons]
charger = bullets[select_weapons]
full_ammo = ammo[select_weapons]

print("Your weapon is the {}".format(select_weapons))
print("You have {} bullets in the charger and a total of {} bullets of ammunition".format(charger, full_ammo))

shoot = True

while shoot:
    while charger > 0:
        decision = input("Do you want to shoot or reload? ")
        if decision == "shoot":
            charger -= bullets_fired[select_weapons]
            print("{} bullets remaining in the charger".format(charger))
        elif decision == "reload":
            if full_ammo == 0:
                print("You can't reload, last bullets are in the charger")
            elif (init_charger - charger) > full_ammo:
                charger += full_ammo
                full_ammo -= full_ammo
                print("You have a reloaded charger of {} bullets and {} bullets of ammunition".format(charger, full_ammo))
            else:
                full_ammo -= (init_charger - charger)
                charger = init_charger
                print("You have a reloaded charger of {} bullets and {} bullets of ammunition".format(charger, full_ammo))

    if charger <= 0 and full_ammo <= 0:
        print("You're out of bullets! Find a way to get more ammunition")
        shoot = False
    elif charger <= 0:
        print("You have to reload!")
        if (init_charger - charger) > full_ammo:
            charger += full_ammo
            full_ammo -= full_ammo
            print("You have a reloaded charger of {} bullets and {} bullets of ammunition".format(charger, full_ammo))
        else:
            full_ammo -= (init_charger - charger)
            charger = init_charger
            print("You have a reloaded charger of {} bullets and {} bullets of ammunition".format(charger, full_ammo))
