from pytube import YouTube
import os


def main():
    # continuing variable
    continue_var = 'Y'

    # changing directory 
    os.chdir(os.path.join('/', 'home', 'vladko', 'Documents', 'python_projects', 'YouTube Downloader 2.0', 'data'))


    # downloading loop
    while continue_var == 'Y':  
        # downloading video
        try: 
            dwl = YouTube(input('Insert a link here: '))
            stream = dwl.streams.filter(only_audio= True).first()
            output = stream.download()

            base, ext = os.path.splitext(output)
            os.rename(output, base + '.mp3' )

        except: 
            print('Not a valid link..') 


        # asking if user want to continue in the loop
        while True:
            continue_var = input('Do you want to continue dowloading? [Y/n] ').upper()
            if continue_var == 'Y' or continue_var == 'N':
                break


# func for moving files
def move_files():
    while True:
        path = input('Type path here where you want to move your files, if not just type "nope": ')
        if path == 'nope':
            break
        elif not os.path.isdir(path):
            continue

        break

    os.system(f'mv *.mp3 "{path}"')

if __name__ == '__main__':
    main()
    move_files()
