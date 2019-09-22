# Bitly url shorterer

[This script allow create short url and count clicks on bitly-links. Script uses service https://bitly.com/]

### How does it work
If you'll input a not-bitly-url script puts bitly-link in stdout.
If you'll input a bitly-link script counts how many times it was clicked.

### How to install

Python3 should be already installed

Then use 'pip' to install dependencies:

```
pip install -r requirements.txt
```

### How to run


``
python bitly.py https:/yandex.ru 
``

And script prints...

``
bit.ly/2kIxEio
`` 

Or if your URL is not correct ...

``
Wrong URL!
``

Also you can put your bitly-link, ad script says how many times someone clicks on it

``
python bitly.py bit.ly/3541ways
``

Add script prints ...

``
163
``



### Project Goals

This sript is written for educational purposes on online-course dvmn.org

