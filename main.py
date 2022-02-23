from pytube import YouTube
import os


if __name__ == '__main__':

    # continuing variable
    continue_var = 'Y'

    # changing directory 
    os.chdir(os.path.join('/', 'home', 'vladko', 'Documents', 'python_projects', 'YouTube Downloader 2.0', 'data'))

    # getting an input from user (youtube link)
    while continue_var == 'Y':  
        song_link = input('Insert a link here: ')
        try: 
            YouTube(song_link)
        except: 
            print('Not a valid link..') 


        # asking if user want to continue in the loop
        while True:
            continue_var = input('Do you want to continue dowloading? [Y/n] ').upper()
            if continue_var == 'Y' or continue_var == 'N':
                break

