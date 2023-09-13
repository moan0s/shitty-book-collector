# Shitty Book Collector

![Healthcheck Badge](https://hc.wurzelraum.org/badge/98e8acf3-6b50-44bd-b361-2ce2cb702b0c/c7Tl9PQ2/qzt-buch.svg)

A shitty CLI script to convert a `.ods` table into a `.html` table. It supports healthchecks and defining a CSS file.
That's it. Not much to see here.

# Installation

**Clone the project and move into the directory**
```bash
git clone https://github.com/moan0s/shitty-book-collector.git
cd shitty-book-collector/
```

**Optional: Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate
```

**Install dependencies**
```bash
pip install -r requirements.txt
```

# Usage

Basic usage
```bash
python main.py -i Books.ods -o books.html
```

Advanced usage
```bash
python main.py -i Books.ods -o books.html --css custom.css --healthcheck https://hc.example.org/ping/8acb905-1234-4567-7890-dac56fff
```
