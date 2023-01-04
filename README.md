# pngdeband
24bit PNG to 15bit PNG converter with de-banding filter

Python で書かれた PNG 画像 de-banding フィルタツールです。

24bit color RGB/RGBA の PNG ファイルを X680x0 で表示するのに適した 15bit color の PNG に変換します。
この時、単純に RGB 各 8bit の下位 3bit を落として 24bit から 15bit に変換してしまうと、バンド(マッハバンド)がすごく目立ちます。
これを防ぐために debanding (バンド除去) フィルターをかけつつ 15bit に変換し、新たな PNG ファイルとして出力します。

PNG ファイルはその仕様上 15bit/16bit のビット深度はサポートされていませんので 24bit RGB PNG として出力しますが、
使われているカラーは 15bit 分のみ、下位3bitはすべて0になっています。

---

### ffmpeg のインストール

インストールにあたっては、オープンソースの動画フィルタコマンドラインツール `ffmpeg` の導入が必要になります。
やや大きめの規模のソフトウェアになりますので注意してください。

Windowsの場合は公式サイト [https://ffmpeg.org/](https://ffmpeg.org/) に行き、Get packages & executable files を選びます。

![](images/ffmpeg1.png)

下の方のサイト(BtbN)が分かりやすいのでそちらから、

    ffmpeg-master-latest-win64-gpl-shared.zip

をダウンロードします。Windowsインストーラ形式にはなっていないので、zipファイルを自分の希望する場所に展開します。
その後で bin フォルダを環境変数 PATH に追加してください。

ググると詳細な導入説明サイトが沢山ありますので、それらも参考にしてください。

macOSの場合は

    brew install ffmpeg

だけです。

---

### pngdeband のインストール

    pip install git+https://github.com/tantanGH/pngdeband.git

[Windowsユーザ向けPython導入ガイド](https://github.com/tantanGH/distribution/blob/main/windows_python_for_x68k.md)

---

### 使い方

    pngdeband [options] <input-png-file> <output-png-file>

---

### 変換例

