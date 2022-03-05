import os


#simple function to rename bulk files
def main():
    i = 0
    path = 'PATH/WITH/A/LOT/OF/FILES/'
    for file in os.listdir(path):
        my_dest = f'img{str(i)}.jpg'
        my_souce = path + file
        my_dest = path + my_dest
        os.rename(my_souce, my_dest)
        i += 1

#calling the function
if __name__ == '__main__':
    main()
