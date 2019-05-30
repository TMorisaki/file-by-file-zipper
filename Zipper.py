from Zipper.Zipper import setFiles
import zipfile
import os
if __name__ == '__main__':
    setFiles = setFiles.setFiles()
    fileList = setFiles.select_process()
    for i in fileList:
        if not os.path.isdir(i):
            zipped = i.replace(os.path.splitext(i)[1],'') #拡張子を除外
            zipped += '.zip'
            with zipfile.ZipFile(zipped,'w', compression = zipfile.ZIP_DEFLATED) as new_zip:
                new_zip.write(i,arcname=os.path.basename(i))
