import os

import pandas as pd


def c_to_x(file):
    cfile = file+'.csv'
    if not os.path.exists(cfile):
        return f'{cfile} not found' + '\n'
    else:
        df = pd.read_csv(cfile)
        xfile = file+'.xlsx'
        df.to_excel(xfile, index=False)
        return 'convert was successfully'+'\n'


def x_to_c(file):
    xfile = file+'.xlsx'
    if not os.path.exists(xfile):
        return f'{xfile} not found' + '\n'
    else:
        df = pd.read_excel(xfile)
        cfile = file+'.csv'
        df.to_csv(cfile, index=False)
        return 'convert was successfully'+'\n'


def detecting():
    inp = input('Do you have excel file? ')
    print('')
    if inp.lower() == 'y' or inp.lower() == 'yes' or inp.lower() == 'excel' or inp.lower() == 'xlsx' or inp.lower() == 'yeah' or inp.lower() == 'yep' or inp.lower() == 'yea' or inp.lower() == 'ye' or inp.lower() == 'yup' or inp.lower() == 'yepper' or inp.lower() == 'yupper' or inp.lower() == 'yupper' or inp.lower() == 'ok' or inp.lower() == 'okay' or inp.lower() == 'sure' or inp.lower() == 'certainly' or inp.lower() == 'absolutely' or inp.lower() == 'definitely' or inp.lower() == 'of course' or inp.lower() == 'affirmative' or inp.lower() == 'roger' or inp.lower() == 'aye' or inp.lower() == 'aye aye' or inp.lower() == 'aye aye captain' or inp.lower() == 'aye aye sir' or inp.lower() == 'aye aye matey' or inp.lower() == 'aye aye sailor' or inp.lower() == 'aye aye shipmate' or inp.lower() == 'aye aye crew' or inp.lower() == 'aye aye team' or inp.lower() == 'aye aye squad' or inp.lower() == 'aye aye unit' or inp.lower() == 'aye aye division' or inp.lower() == 'aye aye battalion' or inp.lower() == 'aye aye regiment' or inp.lower() == 'aye aye brigade' or inp.lower() == 'aye aye company' or inp.lower() == 'aye aye platoon' or inp.lower() == 'aye aye section' or inp.lower() == 'aye aye squadron' or inp.lower() == 'aye aye troop' or inp.lower() == 'aye aye detachment' or inp.lower() == 'aye aye contingent' or inp.lower() == 'aye aye force' or  inp.lower() == 'aye aye unit' or inp.lower() == 'aye aye team' or inp.lower() == 'aye aye squad' or inp.lower() == 'aye aye division' or inp.lower() == 'aye aye battalion' or inp.lower() == 'aye aye regiment' or inp.lower() == 'aye aye brigade' or inp.lower() == 'aye aye company' or inp.lower() == 'aye aye platoon' or inp.lower() == 'aye aye section' or inp.lower() == 'aye aye squadron' or inp.lower() == 'aye aye troop' or inp.lower() == 'aye aye detachment' or inp.lower() == 'aye aye contingent' or inp.lower() == 'aye aye force':
        file = input('Enter xlsx file path: ')
        print('')
        return x_to_c(file)
    else:
        file = input('Enter csv file path: ')
        print('')
        return c_to_x(file)


def main():
    while True:
        print(detecting())
        inpt = input('Press enter to exit... (C to Continue) ')
        if inpt.lower() != 'c':
            print('by...')
            raise SystemExit


if __name__ == '__main__':
    main()