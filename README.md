# heteroconger_codama
![こだまちゃん]()  

## Desciption
チンアナゴをモチーフにしたコミュニケーションロボット。こだまちゃん。  
ユーザーの生活習慣に改善点を見つけると、こだまちゃんの体調が悪くなってユーザーに伝えます。  
犬のために一緒に散歩したり、ルンバのために部屋の片付けをするように、こだまちゃんの元気のために健康を意識できるようなコンセプトで作成しました。  
本作品はユカイ工学のインターン(2020/3/9-13)にて製作したものです。  
ユカイ工学から販売されている[Codama](https://codama.ux-xu.com/)を使用しています。  

## Demo
会話不足、運動不足、睡眠不足の3つのシナリオを想定し、会話デモを実装しました。

- Demo1: ユーザーが話しかけていなくて拗ねている時  
URL: https://youtu.be/zR2s3bXyQ2Q 
- Demo2:ユーザーが運動不足のとき、ラジオ体操流す  
URL: https://youtu.be/Ad_qbySO8Vo
- Demo3: こだまちゃんが眠いとき  
URL: https://youtu.be/dl3Lls3Y3Gs


## Requirements
- Raspberry Pi3 model B+
- [Codama](https://codama.ux-xu.com/)
- サーボモータ x3
- スピーカーまたはイヤホン

## Installation
下記コマンドで好きなディレクトリにクローンします  
```
$ git clone https://github.com/coffiego/heteroconger_codama.git  
```  

## Setup
- Codamaのセットアップ(wakeup wordの登録まで)  
codamaの[wiki](https://github.com/YUKAI/codama-doc-r2/wiki/Codama-Setup)を参考にして行ってください。
- docomo 音声認識 [API登録](https://dev.smt.docomo.ne.jp/?p=docs.api.page&api_name=speech_recognition&p_name=api_usage_scenario)  
	- こちらで取得したAPI keyをrecord2text.pyのAPIKEY="your API key"に入力する
	- record2text.pyの"yourpath/output.wav"をリポジトリをクローンしたpathに変更
- openJtalkの[セットアップ](https://qiita.com/coffiego/items/4fc3b0be78fcded3eef0)を行う
- wakeup2record2text2rep.py(mainのcode)の中でimportされているライブラリーをラズパイにインストール

## Usage
下記コマンドを実行し、Codamaの音声検出範囲を広げます。  
```
$ cd ~/heteroconger_codama
$ ./codama_reboot.sh
```
会話デモは以下のコマンドで実行できます。  
```
$ python3 demofile.py
```
demofile.pyをdemo1.py, demo2.py, demo3.pyなどのように変えてください。
<br>
- demo2.pyで音楽ファイルについて  
ラジオ体操を流していますがこのrepositoryには載せていません。  
自分の好きな音楽ファイルを用意し、  
80行目のファイル名を書き変えてください。
```
pygame.mixer.music.load("your_music_filename.mp3")
```

- Codamaの赤いLEDが点滅せずに点灯し続ける場合はハングアップ状態になっています。その際は下記コマンドを実行し、Codamaのrebootを行ってください。

```
$ ./codama_reboot.sh
```

## Collaborators
- [coffiego](https://github.com/coffiego)
- [Kuwamai](https://github.com/Kuwamai)

## License
This repository is licensed under the MIT license, see [LICENSE](./LICENSE).
