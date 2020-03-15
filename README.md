# Desciption
チンアナゴをモチーフにしたロボット。こだまちゃん。  
こちらはユカイ工学でインターンした時に製作したものです。  
ユカイ工学が出している[codama](https://codama.ux-xu.com/)を使っています。  
![こだまちゃん]()  

# Demo
- Demo1: ユーザーが話しかけていなくて拗ねている時  
URL: 
- Demo2:ユーザーが運動不足のとき、ラジオ体操流す  
URL:
- Demo3: こだまちゃんが眠いとき  
URL: 

# Requirements
- Raspberry Pi3 model B+
- [Codama](https://codama.ux-xu.com/)
- サーボモータ3つ
- スピーカー(なんでも)

# Installation
下記コマンドで好きなディレクトリにクローンします  
```
$ git clone https://github.com/coffiego/heteroconger_codama.git  
```  

# Setup
- Codamaのセットアップ(wakeup wordの登録まで)  
codamaの[wiki](https://github.com/YUKAI/codama-doc-r0/wiki/Codama-Setup)を参考にして行ってください。
- docomo 音声認識 [API登録](https://dev.smt.docomo.ne.jp/?p=docs.api.page&api_name=speech_recognition&p_name=api_usage_scenario)  
	- こちらで取得したAPI keyをrecord2text.pyのAPIKEY="your API key"に入力する
	- record2text.pyのoutput.wavの"yourpath/output.wav"に現在のディレクトリのpathに変更
- openJtalkの[セットアップ](https://qiita.com/coffiego/items/4fc3b0be78fcded3eef0)を行う
- wakeup2record2text2rep.py(mainのcode)の中でimportされているライブラリーをラズパイにインストール

# Usage
デモは以下のコマンドで実行できます。  
```
$ cd ~/heteroconger_codama
$ python3 demofile.py
```
demofile.pyをdemo1.py, demo2.py, demo3.pyなどのように変えてください。

# Collaborators
- [Kuwamai](https://github.com/Kuwamai)

# License
This repository is licensed under the MIT license.
