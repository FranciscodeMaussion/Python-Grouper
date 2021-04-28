# Python-Grouper
Generates Group based on a csv

## Instalation
### Python part
```
pip install -r requirements.txt
```
- [grip](https://github.com/joeyespo/grip) is used to generate github flavoured html in python.
- [pdfkit](https://github.com/JazzCore/python-pdfkit) it is used to convert from html to pdf in python.
### System wide part
You will need [wkhtmltopdf](https://github.com/wkhtmltopdf/wkhtmltopdf) to convert from html to pdf.
In debian:
```
sudo apt install wkhtmltopdf
```

## Usage
```
python Grupos.py <quantity_per_group> <csv_file> <name_exported_file>
```
