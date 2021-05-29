import math
print('\n' + '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('\n' + 'CAESAR CIPHER GENERATION TOOL - IGSR - 1404709 - Spring 2021')
print('\n' + '        Prepared by ahmedhefny@************                 ')
print('\n' + '                 Version 2.0                                ')
print('\n' + '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
menu_string = '\n' + 'Please select the required operation:' + '\n' + \
                'MENU' + '\n' + \
                '----------------------------------------' + '\n' + \
                '1 Encrypt Plain Text with a Key' + '\n' + \
                '2 Decrypt Cipher Text with a key' + '\n' + \
                '3 Bruteforce CipherText by Calculating Correlation Coefficient'+ '\n' + \
                '4 Exit' + '\n'                                                             #### tool menu
valid_options = ['1','2','3','4']                                                           #### (we have four operations with our tool)
KeyMAX=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26'] ## Max Shifts is 26 (total letters in english)
ALPHA=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] ### will be used to calculate Y in Function 3
while True:
    while True:                                                                             ########### Ensure interaction with Menu
        var = input('\n ...press enter to continue...')
        if not(var):
            print(menu_string)
            menu_input = input('Enter Menu Choice: ')
            break
        else:
            print('Press enter to continue')
    if menu_input in valid_options:
        if menu_input == '1':                                                         ######## Triger Encryption Module
            PlainText=input('Enter The Plain Text:')                                  ###### Enter Plaintext value
            Key = (input('Enter the Shifting value (1-26):'))                         ##### Enter key value, you can type anything, but input checking will be at the next step
            if Key in KeyMAX:                                                         ##### input validation, if true do the encryption
                Encryption = [chr((ord(i) + int(Key))) for i in PlainText]            #### Perform encryption using functions chr() & ord(), this two functions depends on ASCII table, this happens letter by letter, by adding the key value as shifting
                CipheredText=''.join(map(str,Encryption))                             #### the ciphered text is placed seperated, the join function allow to combine text in readable format
                print('Ciphered Text with key',Key,'is :',CipheredText)               #### print out the cipher text
            else:
                print('Key Value must be between 1 to 26, Please restart')            #### if you entered key that not in range of KeyMAX, this message will appear.
        if menu_input == '2':                                                         ##### Triger decryption module
            CipheredText=input('Enter The Ciphered text:')                            ##### enter ciphered text
            Key = (input('Enter the Shifting value (1-26):'))                         ##### enter key value, same as line 33, the validation check occur.
            if Key in KeyMAX:                                                         ##### input validation, if true do the decryption
                Decryption = [chr((ord(i) - int(Key))) for i in CipheredText]         ##### Perform decryption, in this case we subtract using the given Key value.
                DecryptedText=''.join(map(str,Decryption))                            ##### the deciphered text is placed seperated, the join function allow to combine text in readable format
                print('Plain Text with key',Key,'is :',DecryptedText)                 ##### print out the plain text
            else:
                print('Key Value must be between 1 to 26, Please restart')            ##### print out the cipher text
        if menu_input == '3':
            SigmaX = 0
            XSQUARE = 0
            SigmaXSQUARE = 0
            X = [7.487792, 1.295442, 3.544945, 3.621812, 13.99891, 2.183939, 1.73856, 4.225448, 6.653554, 0.269036,
                  0.465726, 3.569814, 3.39121, 6.741725, 7.372491, 2.428106, 0.262254, 6.140351, 6.945198, 9.852595,
                  3.004612, 1.157533, 1.691083, 0.278079, 1.643606, 0.036173]
            for VALUE in range(0, len(X)):
                SigmaX = SigmaX + X[VALUE]
                XSQUARE = X[VALUE] * X[VALUE]
                SigmaXSQUARE = SigmaXSQUARE+XSQUARE
            CCTABLE=[]
            CipheredText=input('Enter The Ciphered text:')
            for x in KeyMAX:
                BruteForce = [chr((ord(i) - int(x))) for i in CipheredText]
                PossiblePlain=''.join(map(str, BruteForce))
                Y = []
                for letter in ALPHA:
                    R = BruteForce.count(letter)
                    Y.append(int(R))
                SigmaY=0
                YSQUARE=0
                SigmaYSQUARE=0
                XY=0
                for i in range(0, len(Y)):
                    SigmaY = SigmaY + Y[i]
                    YSQUARE = Y[i] * Y[i]
                    SigmaYSQUARE = SigmaYSQUARE + YSQUARE
                    XY=[X*Y for X,Y in zip(X,Y)]
                SigmaXY=0
                for i in range(0,len(XY)):
                    SigmaXY=SigmaXY+XY[i]
                N = 26
                R=(N*SigmaXY-SigmaX*SigmaY)/(math.sqrt(N*SigmaXSQUARE-math.pow(SigmaX,2))*math.sqrt(N*SigmaYSQUARE-math.pow(SigmaY,2)))
                # print(R)
                CCTABLE.append(R)
            HIGHESTCC = max(CCTABLE)
            KEYINDEX = CCTABLE.index(HIGHESTCC)
            KEYVALUE = KEYINDEX+1
            print('Highest correlation value is',HIGHESTCC,"is associated with key value =",KEYVALUE)
            Decryption = [chr((ord(i) - int(KEYVALUE))) for i in CipheredText]
            DecryptedText = ''.join(map(str, Decryption))
            print('--------------------------------------------------')
            print('Decrypted Text is:')
            print(DecryptedText)
            print('--------------------------------------------------')
        if menu_input == '4':
            print('\n' + 'Terminating the tool, Please close this window!' + '\n')
            break
    else:
        print('\n' + 'INVALID MENU OPTION: Please try again' + '\n')
