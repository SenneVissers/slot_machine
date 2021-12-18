end = 1

#imports
import random

import xml.etree.ElementTree as ET
xmlDoc = ET.parse("Slot machine.xml")
root = xmlDoc.getroot()

#functies
#lijst functies
def lijst_data(data):
    list = []
    for usernames in root.iter('account'):
        if data == 'username':
            info = usernames.find('username')
            list.append(info.text)
        elif data == 'name':
            info = usernames.find('name')
            list.append(info.text)
        elif data == 'password':
            info = usernames.find('password')
            list.append(info.text)
        elif data == 'balans':
            info = usernames.find('balans')
            list.append(info.text)
        elif data == 'wins':
            info = usernames.find('wins')
            list.append(info.text)
        elif data == 'tegoed':
            info = usernames.find('tegoed')
            list.append(info.text)
        elif data == 'crew':
            info = usernames.get('crew')
            list.append(info)
    return list

# commands
print('Account inloggen      i')
print('Account aanmaken      a')
print('Beëndig             end')

#lege lijn
print()

while int(end) > 0:
    #hoofdinput
    wat = input('Wat wilt u doen? ')

    #wat wilt de gebruiker doen
    #account aanmaken
    if wat == 'a':
        #account element aanmaken
        account = ET.Element('account')

        #gebruikersnaam opgeven
        username = ET.SubElement(account, 'username')
        username.text = input('\tKies een gebruikersnaam: ')

        #bestaat gebruikersnaam al
        bestaand = 1
        while int(bestaand) > 0:
            if username.text in lijst_data('username'):
                #melding
                print('\tDeze gebruikersnaam bestaat al!')

                # lege lijn
                print()

                # gebruikersnaam opgeven
                username = ET.SubElement(account, 'username')
                username.text = input('\tKies een gebruikersnaam: ')
            else:
                account.set('crew', 'no')

                #voornaam opgeven
                name = ET.SubElement(account, 'name')
                name.text = input('\tWat is uw naam: ')

                #wachtwoord opgeven
                password = ET.SubElement(account, 'password')
                password.text = input('\tKies een wachtwoord: ')

                #account balans toevoegen
                balans = ET.SubElement(account, 'balans')
                balans.text = '0'

                #account wins
                wins = ET.SubElement(account, 'wins')
                wins.text = '0'

                #account onbetaalde wins
                tegoed = ET.SubElement(account, 'tegoed')
                tegoed.text = '0'

                #toevoegen aan bestand
                root.append(account)
                xmlDoc.write('Slot machine.xml')

                #lege lijn
                print()

                #bevestiging
                print("\nUw account is aangemaakt!")
                print("\nLog nu in om te spelen ;)")

                #beëindig while loop
                bestaand = 0

    #account inloggen
    elif wat == 'i':
        #vraag inlog gegevens
        inlog_naam = input('\tWat is uw gebruikersnaam: ')
        inlog_ww = input('\tWat is uw wachtwoord: ')

        #lege lijn
        print()

        #bestaat gebruikersnaam en wachtwoord combinatie
        if inlog_naam in lijst_data('username'):
            index = (lijst_data('username')).index(inlog_naam)
            if inlog_ww == lijst_data('password')[index]:
                print('\tWelkom', (lijst_data('name')[index]).capitalize())

                #lege lijn
                print()

                # commands
                print('\tDit zijn alle commandos die u kan uitvoeren:')
                print('\tCommandos opvragen   c')
                print('\tAccount setting      s')
                print('\tAccount info         i')
                print('\tSpelregels           r')
                print('\tSpel spelen          g')
                print('\tHigh scores          h')
                print('\tLog uit              l')

                #crew only commands
                if lijst_data('crew')[index] == "yes":
                    print('\tStorten             cs')
                    print('\tReset               cr')

                #lege lijn
                print()

                #variable voor while loop
                endi = 1

                #oneindig runnen tot uitlog functie gebruikt wordt
                while endi > 0:
                    #hoofdinput
                    wati = input('\tHallo ' + lijst_data('username')[index] + ', wat wilt u doen? ')

                    #lege lijn
                    print()

                    #wat wilt de gebruiker doen
                    #commandos weergeven
                    if wati == 'c':
                        print('\tDit zijn alle commandos die u kan uitvoeren:')
                        print('\tCommandos opvragen   c')
                        print('\tAccount setting      s')
                        print('\tAccount info         i')
                        print('\tSpelregels           r')
                        print('\tSpel spelen          g')
                        print('\tHigh scores          h')
                        print('\tLog uit              l')
                        # crew only commands
                        if lijst_data('crew')[index] == "yes":
                            print('\tStorten             cs')
                            print('\tReset               cr')
                        print()

                    #account settings tonen
                    elif wati == 's':
                        print('\tUw gebruikersnaam is', (lijst_data('username')[index]))
                        print('\tUw naam is', (lijst_data('name')[index]).capitalize())
                        print('\tUw wachtwoord is', (lijst_data('password')[index]))
                        print()

                    #account info tonen
                    elif wati == 'i':
                        print('\tU kan nog', lijst_data('balans')[index], 'keer spelen.')
                        print('\tU heeft al', lijst_data('wins')[index], 'keer gewonnen.')
                        print('\tU heeft nog', lijst_data('tegoed')[index], 'onbetaalde winsten.')
                        print()

                    #spelregels tonen
                    elif wati == 'r':
                        print('\tDit zijn de spelregels: ')
                        print('\tOm de jackpot van 50 euro te winnen moet je 777 rollen.')
                        print('\tMet 3x BAR krijg je 5 extra coins om mee te spelen.')
                        print('\tMet combinaties van 2 of 5 kan je niets winnen.')
                        print()

                    #spel spelen
                    elif wati == 'g':

                        #heeft de gebruiker nog spel coins
                        if lijst_data('balans')[index] != '0':
                            #balans verminderen
                            if lijst_data('balans')[index] != '-1':
                                for element in root.findall("account"):
                                    if element.find('username').text == lijst_data('username')[index]:
                                        element.find('balans').text = str(int(lijst_data('balans')[index]) - 1)
                                xmlDoc.write('Slot machine.xml')

                            l1 = [2, 5, 'BAR', 7]
                            l2 = [2, 5, 'BAR', 7]
                            l3 = [2, 5, 'BAR', 7]
                            n1 = l1[random.randint(0, 3)]
                            n2 = l2[random.randint(0, 3)]
                            n3 = l3[random.randint(0, 3)]
                            print('\t' + str(n1), end=' ')
                            print(str(n2), end=' ')
                            print(str(n3))
                            if n1 == n2 and n2 == n3 and n3 == 7:
                                print('\tU heeft de jackpot van €50 gewonnen!!!')
                                print('\tOm te blijven spelen druk g')

                                #wins verhogen
                                for element in root.findall("account"):
                                    if element.find('username').text == lijst_data('username')[index]:
                                        element.find('wins').text = str(int(lijst_data('wins')[index]) + 1)
                                        element.find('tegoed').text = str(int(lijst_data('tegoed')[index]) + 1)
                                xmlDoc.write('Slot machine.xml')

                            elif n1 == n2 and n2 == n3 and n3 == 'BAR':
                                print('\tU heeft 5 extra coins gewonnen!!!')
                                print('\tOm te blijven spelen druk g')

                                #balans verhogen
                                for element in root.findall("account"):
                                    if element.find('username').text == lijst_data('username')[index]:
                                        element.find('balans').text = str(int(lijst_data('balans')[index]) + 5)
                                xmlDoc.write('Slot machine.xml')

                            else:
                                print('\tJammer probeer nog een keer :(')
                                print('\tOm te blijven spelen druk g')
                            print()

                        #de gebruiker heeft geen spelcoins meer
                        else:
                            print('\tU heeft geen spel coins meer :(')
                            print('\tOm coins te kopen kan u de hulp vragen van een crew member!')
                            print()

                    #high scores weergeven
                    elif wati == 'h':
                        counter = 0
                        for usernames in lijst_data('username'):
                            print('\t' + lijst_data('username')[counter] + '\t\t' + lijst_data('wins')[counter])
                            counter += 1
                        print()

                    #crew functie storten
                    elif wati == 'cs':
                        username_stort = input('\tVan welke gebruiker wilt u de balans verhogen (gebruikersnaam): ')
                        balans_stort = input('\tMet hoeveel wil je het saldo van ' + username_stort + ' verhogen: ')
                        ind = lijst_data('username').index(username_stort)
                        print('Het saldo van', username_stort, 'is met', balans_stort, 'verhoogd.')
                        print()

                        # balans verhogen
                        for element in root.findall("account"):
                            if element.find('username').text == lijst_data('username')[ind]:
                                element.find('balans').text = str(int(lijst_data('balans')[ind]) + int(balans_stort))
                        xmlDoc.write('Slot machine.xml')

                    #crew functie reset
                    elif wati == 'cr':
                        username_reset = input('\tVan welke gebruiker wilt u iets resetten (gebruikersnaam): ')
                        ind = lijst_data('username').index(username_reset)
                        print('\tHet aantal onuitbetaalde winsten van', username_reset, 'staat nu op 0.')
                        print()

                        # balans verhogen
                        for element in root.findall("account"):
                            if element.find('username').text == lijst_data('username')[ind]:
                                element.find('tegoed').text = '0'
                        xmlDoc.write('Slot machine.xml')

                    #uitloggen
                    elif wati == 'l':
                        print('\tU bent nu uitgelogd!')
                        print()
                        endi = 0

            else:
                print('\tDit wachtwoord is fout!')
                print()
        else:
            print('\tDit account bestaat niet!')
            print()

    #programma beëindigen
    elif wat == 'end':
        end = 0
