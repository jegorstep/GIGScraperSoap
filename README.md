# Web Spider

## Requirements
install packages in file requirements.txt

```bash
beautifulsoup4==4.12.3
scrapy==2.11.1
requests==2.31.0
```

## How to use?
In the folder 'src' there are 2 files, GIGscrapy.py and GIGsoap.py. 
Both files fetch information from the GIG website's 'kasutatud-tehnika' section.
GIGscrapy uses the scrapy framework for this purpose, while GIGsoap utilizes the Beautiful Soup package. 
To generate the files, run the following files in command prompt (you must be in the 'src' folder): 

```bash
python GIGscrapy.py

python GIGsoap.py

or Run files in PyCharm.
```
Files will be generated in  'src' folder

## Configurations for output?
If you want to configure where the JSON file will be saved, 
you need to adjust the 'output_file' line in the GIGscrapy.py and GIGsoap.py files.

GIGsoap.py
```bash
    scraped_data = parse(start_url)

    output_file = 'soap-products.json' #cofigure here
    with open(output_file, 'w') as json_file:
        json.dump(scraped_data, json_file, indent=4)
```
GIGscrapy.py
```bash
    output_file = 'scrapy-products.json' #configure here
    process = CrawlerProcess(settings={
        'FEEDS': {
            output_file: {
                'format': 'json',
                'indent': 4
            }
        }
    })
```