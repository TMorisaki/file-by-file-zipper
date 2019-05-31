import setFiles
import zipfile
import os
import sys
if __name__ == '__main__':
    setFiles = setFiles.setFiles()
    fileList = setFiles.select_process()
    if len(fileList)==0:
        print('There are no file. Please check setFies.ini')
        sys.exit(1)
    for i in fileList:
        if not os.path.isdir(i):
            zipped = i.replace(os.path.splitext(i)[1],'') #拡張子を除外
            zipped += '.zip'
            with zipfile.ZipFile(zipped,'w', compression = zipfile.ZIP_DEFLATED) as new_zip:
                new_zip.write(i,arcname=os.path.basename(i))
                print('create zip file: ' + zipped)
        else:
            print('!!Skip!! I can NOT conversion the directory: ' + i)
