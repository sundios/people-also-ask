
# People Also Ask Google Scraper

PPA scraper is a Python script that based on a query it scrapes Google people also ask questions. 
You can see this script in action on https://www.keywordresearchtool.io/


## Installation

To install and run this script we need to install the requirements.txt and the driver. Since we are using Chrome we need to download the latest chrome driver.


### Requirements

To install requirements.txt please run the following on the terminal.

```bash
pip install requirements.txt
```

### Chrome driver

#### 1.- Step one (Check Chrome Version)

Check which chrome version are you using.

you can do it via the terminal using the following command:

```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version
```

or you an simply go into chrome and click on Chrome> About Google Chrome. you should see somehting like:

```
Google Chrome is up to date
Version 89.0.4389.90 (Official Build) (x86_64)
```

#### 2.- Step two (Download Chrome Driver)

Download the correct version of chrome driver.

Go to https://chromedriver.chromium.org/downloads

and click on you chrome version.

E.g: 'Chrome version 89, please download ChromeDriver 89.0.4389.23'


#### 3.- Step three (Chrome driver permisions)

If you are on MacOS Catalina do the following:

Navigate to path where your chromedriver file is located and run 

```bash
xattr -d com.apple.quarantine chromedriver

```

#### 4.- Step four (chromedriver path)

You can do either solution:

a.- Move chrome driver to /usr/local/bin/ 

Make sure you are on the folder chromedriver is and run

```bash
sudo mv chromedriver /usr/local/bin/
```

b.- Update chrome driver path on the python script.

On line 35 update `executable_path` with your chrome driver path

```python
executable_path='add_path_here'
```


## Usage
 
To run the script we go on the terminal and make sure we are in the correct folder. We type:


```bash
python3 paa.py
```

Once you run the script it will ask you to provide 3 inputs that are necessary.

1. **Add Query:** Query that you want to get the answers from.

**E.g**

```
netflix stock
```

2. **How many questions do you want to click?:** The more clicks you add the more question you get. Usually 1 click adds 2 or 3 questions and by default Google provides 4 questions. So if we add 5 as clicks then we would get around 15 questions.

3. **Please select your languange:** I added only 2 languages, English (en) and Spanish (es). Make sure that the language is in lowcase.

## Result

Once you run the script it will output a df with all the question that found for the query you rquested. The output should look like this:

**English E.g** 
```
                                         Questions
0                        Is Netflix a buy or sell?
1                   Why is Netflix stock dropping?
2               Does Netflix stock pay a dividend?
3                           Is Netflix overvalued?
4             What stock is best to buy right now?
5                  Is Walmart a good stock to buy?
6                          Is Netflix going broke?
7                        What stocks are up today?
8   What is the most expensive stock in the world?
9               What stock pays the best dividend?
10                        Do Amazon pay dividends?
11                Does Apple stock pay a dividend?
12                      Can you invest in Netflix?
13                  What is the future of Netflix?
```

**Spanish E.g** 
```
                                           Questions
0                    ¿Cuánto cuesta Netflix al mes?
1          ¿Cuánto cuesta Netflix al año en España?
2              ¿Cómo iniciar una sesión de Netflix?
3   ¿Cuánto cuesta una cuenta en Netflix Venezuela?
4            ¿Cuánto cuesta Netflix en México 2020?
5                       ¿Qué ofrece Netflix basico?
6            ¿Cuánto vale Netflix en Colombia 2020?
7                        ¿Cuánto vale Netflix 2020?
8                   ¿Cuánto está Netflix Perú 2020?
9                ¿Dónde pongo mi código de Netflix?
10  ¿Cómo hago para tener el mes gratis de Netflix?
11             ¿Por qué no puedo acceder a Netflix?
```


## Issues & Contributing
Pull requests are welcome. If you have any issues please open an issue to see if I can help.

