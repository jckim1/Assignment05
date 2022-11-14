#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
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

    if strChoice == 'x':
        break
    if strChoice == 'l': # if choice is to load, open the saved file, iterate over each row and save values to dictionary, update list with dictionary rows, then close file
        print('Load data from the file')
        lstTbl.clear()
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            drow = {'ID': lstRow[0], 'Album': lstRow[1], 'Artist': lstRow[2]}
            lstTbl.append(drow)
        objFile.close()
    elif strChoice == 'a': # inputs to get id, album name, and artist, add those to a 2d dictionary row then append to the list
        strID = input('Enter an ID: ')
        strAlbum = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        drow = {'ID': intID, 'Album': strAlbum, 'Artist': strArtist}
        lstTbl.append(drow)
    elif strChoice == 'i': # if choice is to check inventory, for loop iterates through list and prints each dictionary row
        print('ID, Album, Artist')
        for row in lstTbl:
            print(row)
    elif strChoice == 'd': # to delete album, user inputs the album name to delete then for loop ierates through list until it finds the value matching the user input then deletes that row
        delID = input('Enter the ID of the row you wish to delete: ')
        for row in lstTbl:
            for key, val in row.items():
                if val == delID:
                    del row
        print(lstTbl)
    elif strChoice == 's': # user can save the current list to the file for loop iterates through each row and converts the values to a string separated by a comma, then removes the last comma adding a hard breaking space, values are written to the file then the file is closed.
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strRow = ''
            for item in row:
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Invalid choice. Please select from one of the available options; l, a, i, d, s or x!')
