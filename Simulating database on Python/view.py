from trythisshit import *



def menumenu(dat):
    print('             Welcome to the Main menu!')
    print('1. Print the database')
    print('2. Change the database')
    print('3. Print all the faculties with the largest numbers of groups')
    print('4. Get out')
    select = int(input('Please, select what you wanna do: '))
    if select == 1:
        print()
        print('')
        print('Faculty №:      Number of groups      Name of faculty')
        for val in dat.faculties:
            print('{}               \v{}                    \v{}'.format(val, dat.groups[dat.faculties[val]], dat.faculties[val]))
        print()
        menumenu(dat)
    elif select == 2:
        print()
        print()
        print('1. Do you wanna ADD NEW FACULTY, bro?')
        print('2. Or maybe you want to DELETE the FACULTY?')
        print('3. Come on, let`s CHANGE the NUMBER OF GROUPS of current faculty!')
        print('4. No, bro, GET OUT of here.')
        choice = int(input('Select the action, dog!   '))
        if choice == 1:
            print()
            dat.newfac()
            print()
            menumenu(dat)
        elif choice == 2:
            print()
            print('Write the name of faculty you wanna delete')
            name = str(input())
            dat.delfac(name)
            print()
            menumenu(dat)
        elif choice == 3:
            print()
            print('Write the name of faculty')
            name = str(input())
            print('Write the new number of groups')
            newnum = int(input())
            dat.changenum(name, newnum)
            print()
            menumenu(dat)
        elif choice == 4:
            print()
            menumenu(dat)
            print()
    elif select == 3:
        print()
        print('Look, now you need to enter the number.')
        print('There will be only faculties with higher numbers of groups than current')
        number = int(input())
        print('Number of groups      Name of faculty')
        for val in dat.groups:
            if dat.groups[val] > number:
                print('{}                    {}'.format(dat.groups[val], val))
        print()
        menumenu(dat)
    elif select == 4:
        dat.exit()
        quit()

