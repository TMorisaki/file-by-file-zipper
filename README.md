# file-by-file-zipper
zipper.pyはファイル単位で同じディレクトリ上にzipファイルを生成します
ファイル選択についてはsetFiles.pyが行っており、以下のどちらかの方法で読み込みが可能です
・どのディレクトリorファイルを読み込むかを指定する
・setFiles_config.iniに指定したディレクトリ群,ファイル
setFiles_config.iniの設定方法は.ini内に記載されている例を参考にしてください。

zipper.py create zip files as file by file in same directory.
setFiles.py determine which files will conbersion by;
・select a directory/files with dialog
・load specified directories/files by setFile_config.ini
