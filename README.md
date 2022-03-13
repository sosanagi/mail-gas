# mail-gas

### 共通設定
```bash
cp .env_dist .env
cp src/mail_dist.txt src/mail.txt
```
.envファイルを設定

### windows設定の場合
python3をインストール

1. chrome://settings/manageProfileへアクセスする。
2. デスクトップにショートカットを作成するをオンにする。
3. プロパティ設定、リンク先を確認する。
4. exeまでを.env CHROMEへ。
5. --profile-directoryを.env PROFILEへ。

.env_distを参考にpowerShellに環境変数を設定する。
```
cd src
python3 main.py
```

### docker設定の場合
```bash
cd docker/
docker compose up -d
docker compose exec gas-setup bash
python3 main.py
```
ctrl+URLクリック