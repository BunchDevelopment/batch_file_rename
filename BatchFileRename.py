import os
def main () :
    def rename_file(files, path):
        rename_type = input('How do you want them renamed? (prefix, suffix, full, quit) \n')
        if(rename_type.lower() == 'prefix'):
                prefix = input('Prefix: \n')
                for file in files:
                    os.rename(path + file, path + prefix + file)

        elif(rename_type.lower() == 'suffix'):
            suffix = input("Suffix: \n")
            for file in files:
                split_file = os.path.splitext(file)
                os.rename(path + file, path + split_file[0] + suffix + split_file[1])

        elif(rename_type.lower() == 'full'):
            new_name = input("File Name: \n")
            for ind, file in enumerate(files):
                split_file = os.path.splitext(file)
                os.rename(path + file, path + new_name + str(ind) + split_file[1])

        elif(rename_type.lower() == 'quit'):
            print('Thanks fam!')

        else :
            print('Not a recognized type, try: prefix, suffix, full \n')
            rename_file(files, path)

    try: 
        path = input('Give a path to the directory that you want to rename files: \n')
        if(path.endswith('\\') or path.endswith('/')):
            files = os.listdir(path)
            string_files = ' '.join(files)
            verify_files = input('Are these the files you want renamed? \n ' + string_files + '\n')
            if('y' in verify_files.lower()) :
                rename_file(files, path)
                print('Successfully renamed all your files!\n')
            else :
                print('Restart the script to try again.\n')
        
        else :
            print('Your path must end with \\ or /')
            main()
        

    except Exception as e:
        print('ERROR!: ', e)

if __name__ == '__main__':
    main()