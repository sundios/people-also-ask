
Need to install

```
pip install -r requirements.txt
```


download driver on --> find link 

and we can do it 2 ways:

- Add executable_path arg in webdriver:

```

with webdriver.Firefox(executable_path='/path/to/geckodriver') as driver:

```

And the second way its to add folder that contains geckodriver using export (only folder, not geckodriver):

```

$ export PATH=$PATH:/path/to/

```