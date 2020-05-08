
# People Also Ask scraper

PPA scraper is a Python script that based on a query it scrapes Google people also ask questions. 


Note: *This is a work in Progress* 

## Installation

To install and run this script we need to install our requirements.txt. Since we are using Firefox we need to download the latest geckodriver driver.


### Requirements

To install requirements.txt please run the following on the terminal.

```bash
pip install requirements.txt
```

### Geckodriver

You can find it the latest firefox driver [here](https://github.com/mozilla/geckodriver/releases).

Once we download the driver you can save it in the same folder than the script is /people-also-ask/ and we can do two things to make sure it runs:

1. Add executable_path arg in webdriver:

```bash

with webdriver.Firefox(executable_path='/path/to/geckodriver') as driver:

```

2.(**RECOMENNDED**)The second way its to add folder that contains geckodriver using export (only folder, not geckodriver). We go to the terminal and type:

```bash

$ export PATH=$PATH:/path/to/

```


## Usage

Once we install the requirements and the driver, we can go ahead and run our script on the terminal using:


```bash
python3 paa.py
```

Once you run the script it will ask you to provide 3 inputs that are necessary.

1. Add Query: Query that you want to get the answers from.

E.g

```
netflix stock
```

2. How many questions do you want to click?: The more clicks you add the more question you get. Usually one clicks adds 2 or 3 questions and by default Google provides 4 questions. So if we add 5 as clicks then we would get around 15 questions.

3. Please select your languange: I added only 3 languages, English (en) , Spanish (es) and French (fr). Make sure that the language is in lowcaps.

## Result

Once you get allthe parameters the script will go and get all the questions for you. Then your output will consist of the question index that its being clicked, and the questions.

E.g 
```
0
Is Netflix a good stock to buy?
Why is the Netflix stock going down?
Will Netflix stock go up?
What was Netflix original stock price?


1
Is Netflix a good stock to buy?
Why is the Netflix stock going down?
Will Netflix stock go up?
What was Netflix original stock price?
Should I buy Tesla stock now?
What is the best stock to buy right now?

2
Is Netflix a good stock to buy?
Why is the Netflix stock going down?
Will Netflix stock go up?
What was Netflix original stock price?
Should I buy Tesla stock now?
What is the best stock to buy right now?
Is Disney stock a buy?
Is Netflix a buy or sell?
```

## Contributing
Pull requests are welcome. If you have any issues please open an issue to see if I can help.

