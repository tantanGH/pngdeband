# pngdeband
24bit PNG to 15bit PNG converter with de-banding filter in Python

24bit color RGB/RGBA の PNG ファイルを X680x0 で表示するのに適した 15bit color の PNG に変換します。
この時、単純に RGB 各 8bit の下位 3bit を落として 24bit から 15bit に変換してしまうと、画像の平坦かつ明暗差がある部分で band(マッハバンド)がすごく目立ちます。これを防ぐために debanding (マッハバンド除去) をしつつ 15bit に変換し、新たな PNG ファイルとして出力します。

PNG ファイルはその仕様上 15bit のビット深度はサポートされていませんので 24bit RGB PNG として出力しますが、
使われているカラーは 15bit 分のみ、下位3bitはすべて0になっています。

---

### ffmpeg のインストール (Windows)

インストールにあたっては、オープンソースの動画処理コマンドラインツール `ffmpeg` の導入が必要になります。

Windowsの場合は公式サイト [https://ffmpeg.org/](https://ffmpeg.org/) に行き、Get packages & executable files を選びます。

![](images/ffmpeg1.png)

下の方のサイト(BtbN)が分かりやすいのでそちらから、

    ffmpeg-master-latest-win64-gpl-shared.zip

をダウンロードします。Windowsインストーラ形式にはなっていないので、zipファイルを自分の希望する場所に展開します。
その後で bin フォルダを環境変数 PATH に追加してください。

ググると詳細な導入説明サイトが沢山ありますので、それらも参考にしてください。

---

### ffmpeg のインストール (MacOS)

    brew install ffmpeg

だけです。

---

### pngdeband のインストール

pip を使って導入します。

    pip install git+https://github.com/tantanGH/pngdeband.git

[Windowsユーザ向けPython導入ガイド](https://github.com/tantanGH/distribution/blob/main/windows_python_for_x68k.md)

---

### 使い方

    pngdeband [options] <input-png-file> <output-png-file>

---

### 変換例1

変換前の24bitPNGをdeband処理なしで15bit表示したもの

![](images/sample1.png)

deband処理して15bit表示したもの

![](images/sample1d.png)

---

### 変換例2

変換前の24bitPNGをdeband処理なしで15bit表示したもの

![](images/sample2.png)

deband処理して15bit表示したもの

![](images/sample2d.png)

---

### 変換例3

変換前の24bitPNGをdeband処理なしで15bit表示したもの

![](images/sample3.png)

deband処理して15bit表示したもの

![](images/sample3d.png)

--
