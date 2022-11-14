#------------------------------------------#
# Title: CDInventory.py
# Desc: Script to manage a list of dictionaries containing album information
# Change Log: 11/13/2022, Added comments
# Jesse Kim, 11/13/2022, Created File
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
lstRow = None
drow = {} # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
strRow = ''

# Get user Input
print('CD Inventory\n')
while True:
    print('[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory\n[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('Select from the above options: ').lower()  # convert choice to lower case at time of input
    print()
# Processing Input
    if strChoice == 'x': # if user choice is x, exit program
        break
    if strChoice == 'l': # if choice is to load, open the saved file, iterate over each row and save values to dictionary, update list with dictionary rows, then close file
        lstTbl.clear()
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            drow = {'ID': lstRow[0], 'album': lstRow[1], 'artist': lstRow[2]}
            lstTbl.append(drow)
        objFile.close()
    elif strChoice == 'a': # two inputs to get album name and artist, add those to a 2d dictionary row then append to the list
        strAlbum = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        drow = {'album': strAlbum, 'artist': strArtist}
        lstTbl.append(drow)
    elif strChoice == 'i': # if choice is to check inventory, for loop iterates through list and prints each dictionary row
        print('Album, Artist')
        for row in lstTbl:
            print(row)
    elif strChoice == 'd': # to delete album, user inputs the album name to delete then for loop ierates through list until it finds the value matching the user input then deletes that row
        delalbum = input('Enter the name of the album you wish to delete: ')
        for i in range(len(lstTbl)):
            if lstTbl[i]['album'] == delalbum:
                del lstTbl[i]
        print(lstTbl)
    elif strChoice == 's': # user can save the current list to the file for loop iterates through each row and converts the values to a string separated by a comma, then removes the last comma adding a hard breaking space, values are written to the file then the file is closed.
        objFile = open(strFileName, 'a')
        for item in lstTbl:
            strRow = ''
            strRow = item['album'] + ', ' + item['artist'] + '\n'
            objFile.write(strRow)
        objFile.close()
        print('Inventory saved to file')  
    else:
        print('Invalid choice. Please select from one of the available options; l, a, i, d, s or x!')
