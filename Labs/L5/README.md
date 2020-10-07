# Авторизація і автентифікація

В даній лабораторній порібно реалідізувати автентифікацію та авторизацію користувачів для розробленого REST API. Автентифікація є перевіркою того, що запит відбувається від іменгі конкретного користувача. Авторизація є перевіркою того чи має конкретний користувач доступ до конкретної операції над певним ресурсом.

## Хід роботиґ



## Критерії оцінювання

## Виконання лабораторної роботи


Встановити залежності
```shell script
$ echo "Flask-JWT" >> requirements.txt
$ pip install -Ur requirements.txt
```

Стартувати базу даних
```
$ make up
```

Виконати ряд запитів до системи
```
$ sudo apt-get install jq
$ source functions.sh
$ AUTH_USERNAME=admin-aec8084845b41a6952d46cbaa1c9b798659487ffd133796d95d05ba45d9096c2 AUTH_PASSWORD=super-secret EMAIL="test_1@example.com" PASSWORD=123 python-uni-create-user
$ AUTH_USERNAME=admin-aec8084845b41a6952d46cbaa1c9b798659487ffd133796d95d05ba45d9096c2 AUTH_PASSWORD=super-secret EMAIL=test_2@example.com PASSWORD=123 python-uni-create-user
$ AUTH_USERNAME=test_1@example.com AUTH_PASSWORD=123 WALLET_NAME=WalletA python-uni-create-wallet
$ AUTH_USERNAME=test_2@example.com AUTH_PASSWORD=123 WALLET_NAME=WalletB python-uni-create-wallet
$ AUTH_USERNAME=test_1@example.com AUTH_PASSWORD=123 python-uni-list-wallets
$ AUTH_USERNAME=admin-aec8084845b41a6952d46cbaa1c9b798659487ffd133796d95d05ba45d9096c2 AUTH_PASSWORD=super-secret FROM_WALLET=0 TO_WALLET=1 AMOUNT=100 python-uni-send-funds
$ AUTH_USERNAME=test_1@example.com AUTH_PASSWORD=123 python-uni-list-wallets
$ AUTH_USERNAME=test_1@example.com AUTH_PASSWORD=123 FROM_WALLET=1 TO_WALLET=2 AMOUNT=10 python-uni-send-funds
$ AUTH_USERNAME=test_1@example.com AUTH_PASSWORD=123 python-uni-list-wallets
$ AUTH_USERNAME=test_2@example.com AUTH_PASSWORD=123 python-uni-list-wallets
```

Знищити базу даних
```
$ make down
```
