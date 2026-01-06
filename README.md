# muf-sample-unit
MUF（Redisベースのユニット開発フレームワーク）のための、Webインターフェースを備えたサンプルユニットの実装リポジトリです。このプロジェクトは、FlaskまたはFastAPIを用いてブラウザからの入力を受け付け、Redisを介してMUF標準のecho-unitと通信し、その応答をリアルタイムに画面へ表示する一連のメッセージングサイクルを実証します

## 開発リファレンス

- [Pythonライブラリ](https://github.com/Masafuro/MUF/blob/main/doc/unit_reference_v2.md)
- [docker 及び設定情報](https://github.com/Masafuro/MUF/blob/main/doc/custom-unit_reference.md)

## MUF SDK及びコアユニット
https://github.com/Masafuro/MUF/tree/main


## ユニット開発
- submoduleとしてmufを引き込み
> git submodule add https://github.com/Masafuro/MUF.git muf

- submodule更新
> git submodule update --remote

- muf-redis立ち上げ
> docker compose up -d muf-redis

- echo-unit立ち上げ
> docker compose up -d muf-echo-unit

- monitor立ち上げ
> docker compose run --rm muf-monitor

- check-unit実行
> docker compose run --rm muf-check-unit

- echo-unit停止
> docker rm -f muf-echo-unit

- docker container 状況確認
> docker ps

## sample-unit動作確認

- 実行
ルートディレクトリから
> docker compose up
ブラウザで`localhost:8000`にアクセスする。

- 終了
ctrl + C で終了し
> docker compose down
