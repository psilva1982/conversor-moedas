# Conversor de Moedas

[![coverage report](https://github.com/psilva1982/conversor-moedas/blob/main/backend/coverage.svg)](https://github.com/psilva1982/conversor-moedas/blob/main/backend/coverage.svg)


## How to run this app

1° clone this repository

```
git clone https://github.com/psilva1982/conversor-moedas.git
```
## The backend - 🌐 [https://dollarquote-api.herokuapp.com/api/](https://dollarquote-api.herokuapp.com/api/)
2° Setup Django App
```
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3° Configure your .env file. Do you need setup only database access
- This app uses **postgresql**
```
mv .env-sample.txt .env
```

4° Run migrations
```
python manage.py migrate
```

5° Run server
```
python manage.py runserver
```
---
## The frontend - 🌐 [https://dollar-quote.surge.sh/](https://dollar-quote.surge.sh/)
Do you **need node/npm and yarn** installed on your pc.

6° After you install node/npm and yarn proceed to install frontend dependencies
```
cd frontend
yarn install
```
7° Configure .env
```
mv .env-sample.txt .env.local
```
8° Run server
```
yarn serve
```

9° Access webapp 👉 [http://localhost:8080/](http://localhost:8080/)

Thats it!!! 🤘🤘🤘
