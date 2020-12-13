# Smart Doc Search

### It provides advanced searching of text in different medias like images, audio, documents etc.

## Installation

Follow these steps to run this project -

1. To download the project,

```
git clone https://github.com/udbhavdave/Major.git <local-repo-name>
```

2. Make virtual environment and activate it.

```
virtualenv env
env\Scripts\activate (windows)
source env/bin/activate (linux)
```

3. To install project dependencies,

```
pip install -r requirements.txt
```

4. To generate local database and tables in it,

```
python smartdoc\manage.py migrate
```

5. To launch server on localhost,

```
python smartdoc\manage.py runserver

```

6. Go to http://127.0.0.1:8000/

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
