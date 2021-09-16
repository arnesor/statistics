# Statistics
Jupyter notebooks for statistics from Norway.

## Notebooks 
### Covid
A notebook showing a zoomable coloured municipality map of Norway with Covid-19 cases.


## Installing requirements
If you are on Windows and not using Anaconda, you need to run the following commands before installing packages from
requirements.txt:
```shell
pip install wheel pipwin
pipwin install gdal
pipwin install fiona
```
Install dependencies from requirements.txt:
```shell
pip install -r requirements.txt
```

This is a dummy change for demonstration purposes.
You can also use the pipenv tool, like this:
```shell
pipenv install -r requirements.txt
```


## Running tests
Install dependencies (from root directory):
```shell
pip install -e .[tests]
```

Run all test (from root directory):
```shell
pytest
```
