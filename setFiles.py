#設定されたor選択したフォルダ/ファイルの配列を返すプログラム
#これと処理系のプログラムを組み合わせて使います
#setFilesのインスタンスを生成したあとは以下のように処理を追加できます。
#1. setFiles.select_process() : 処理方法を選択して該当するファイルの全てのフルパスをリストで返す
#2. setFiles.getDir() : ダイアログからフォルダを選択して、その中にあるファイルのフルパスをリストで返す
#3. setFiles.getFiles() : ダイアログから複数ファイルを選択して、その中にあるファイルのフルパスをリストで返す
#4. setFiles.spDir() : setFiles_configファイルに指定されたディレクトリの中にある全てのファイルのフルパスをリストで返す
#5. setFiles.spFiles() : setFiles_configファイルに指定されたファイルのフルパスをリストで返す
from tkinter import filedialog
import tkinter
import glob
import configparser
import os
import sys

class setFiles(tkinter.Frame):
    #iniファイルの読み込みと下準備
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('setFiles_config.ini','utf-8')
        self.getFilesConfig = 'getFilesList'
        #filetypeは2次元針列で受け取る必要があるためiniファイルの内容を配列に分解
        self.tpText = self.config[self.getFilesConfig]['type'].split(';')
        self.tp =[]
        for i in self.tpText:
            self.tp.append(i.split(','))
        #それ以外は1次元配列に分解するだけでOK
        self.spConDirs = self.config[self.getFilesConfig]['spDirs'].split(';')
        self.spConFiles = self.config[self.getFilesConfig]['spFiles'].split(';')
        self.preDir = self.config[self.getFilesConfig]['preDir']
        self.fileList = []
        self.setVar = int(self.config[self.getFilesConfig]['setVar'])

    def select_process(self):
        self.create_widgets()
        return self.fileList

    #簡易なGUI画面の作成
    def create_widgets(self):
        self.master = tkinter.Tk()
        self.master.geometry('300x200')
        self.tkVar = tkinter.IntVar()
        self.tkVar.set(self.setVar)
        self.master.title('処理方法選択')
        self.tk_text = ['フォルダ選択','ファイル選択','フォルダ設定読込','ファイル設定読込']
        for i in range(len(self.tk_text)):
            self.rdo = tkinter.Radiobutton(self.master, value=i, variable =self.tkVar, text=self.tk_text[i])
            self.rdo.place(x=70, y=40+30*i)
        self.btn = tkinter.Button(self.master, text='決定', command= self.btn_click)
        self.btn.place(x=100, y=170)
        self.master.mainloop()

        if self.tk_text[self.num] == 'フォルダ選択':
            self.getDir()
        elif self.tk_text[self.num] == 'ファイル選択':
            self.getFiles()
        elif self.tk_text[self.num] == 'フォルダ設定読込':
            self.spDir()
        else:
            self.spFiles()

    def btn_click(self):
        self.num = self.tkVar.get()
        self.master.destroy()

    def getDir(self):
        self.dirName = filedialog.askdirectory(initialdir = self.preDir)
        self.fileList.append(sorted(glob.glob(self.dirName + '/*')))
        return self.fileList
    def getFiles(self):
        self.fileList.append(filedialog.askopenfilenames(filetypes = self.tp , initialdir = self.preDir ))
        return self.fileList
    def spDir(self):
        for i in self.spConDirs:
            if os.path.exists(i):
                self.fileList.extend(sorted(glob.glob(i + '/*')))
            else:
                print('!!ERROR!!' + i +' is not exist. Please check spDirs of setFiles_config_ini')
                sys.exit(1)
        return self.fileList
    def spFiles(self):
        for i in self.spConFiles:
            if os.path.exists(i):
                self.fileList.append(i)
            else:
                print('!!ERROR!!' + i +' is not exist. Please check spFiles of setFiles_config_ini')
                sys.exit(1)
        return self.fileList

if __name__ == '__main__':
    setFiles = setFiles()
    fileList = setFiles.select_process()
    print('テスト結果:')
    print(fileList)