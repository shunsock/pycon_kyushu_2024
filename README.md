# PyCon Kyushu 2024: Pythonで作る堅牢なソフトウェア

## Project Overview
PyCon Kyushu 2024での講演「Pythonで作る堅牢なソフトウェア」のレポジトリです。
スライドとサンプルコードを含んでいます。

## Slide
{スライドのリンクを貼る}

## Prerequisites
サンプルコードを実行するためには、以下のツールが必要です。
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## サンプルコードの実行方法

### Build
コンテナをビルドするには、次のコマンドを実行します。
```shell
docker compose up -d --build
```

### Get into container
コンテナに入るには、次のコマンドを実行します。
```shell
docker compose exec app bash
```

### Initialize
コンテナ内に入ったら、Poetryを使ってプロジェクトの依存関係を初期化します。
```shell
~app/project$ poetry install
```

### Run Workflow
Pythonスクリプトを実行する前に、フォーマット、リント、その他の種類のワークフローを実行することができます。Makefileを使用して、次のタスクを処理します。

- Formatting: isort, black
- Linting: flake8
- Static Analysis: mypy
- Testing: pytest
- Reporting: coverage

To execute the workflows, run:
```shell
~app/project$ make
```
