import datefinder
from commonregex import CommonRegex
import geograpy
import re
import nltk
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
import pymysql

test_doc = 'travel-nontravel/tr2.txt'
f=open(test_doc, "r")
contents =f.read()
print contents
parsed_text = CommonRegex(contents)
print(parsed_text.times)
time = parsed_text.times
print(time[0])
date = parsed_text.dates
print(date[0])
print(parsed_text.street_addresses)
print(parsed_text.btc_addresses)
      #places = geograpy.get_place_context(text=contents)
      #print(places.region)
      #print(places.cities)
      #regexp = "[0-9]{1,3} .+, .+, [A-Z]{2} [0-9]{5}"
      #address = re.findall(regexp,contents)
      #print(address)
      #print parse_address(contents)
address=[]      
regexp1 = "venue[ ]?[:-][ ]?[a-zA-Z0-9,&. -]+"
if "venue" in contents:
	address =re.findall(regexp1, contents.lower())
	address[0] = address[0][5:]
	address[0].strip()
	address[0] = s[1:]
	address[0].strip();
if not address:
	regexp = "[0-9]{1,3} .+, .+, [A-Z]{2} [0-9]{5}"
	#"[0-9]{1,3} .+, .+, [A-Z]{2} [0-9]{5}"
	address = re.findall(regexp, contents)
if not address:
	regexp = "\d+.+(?=AL|AK|AS|AZ|AR|CA|CO|CT|DE|DC|FM|FL|GA|GU|HI|ID|IL|IN|IA|KS|KY|LA|ME|MH|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|MP|OH|OK|OR|PW|PA|PR|RI|SC|SD|TN|TX|UT|VT|VI|VA|WA|WV|WI|WY)[A-Z]{2}[, ]+\d{5}(?:-\d{4})?"
	#"[0-9]{1,3} .+, .+, [A-Z]{2} [0-9]{5}"
	address = re.findall(regexp, contents)

print "\n"		
print address
con = pymysql.connect(host='localhost',database='minorproject', user='root',charset='utf8mb4')
cur = con.cursor()
sql_insert = "INSERT INTO extract(date,address) values (%s,%s)"
cur.execute(sql_insert,(date[0],address[0]))
con.commit()

###
#312 N whatever st., New York NY 10001
#115A Address Street, Suite 100, Google KS, 66601
#42 NE Another Address, Some City with 9 digit zip, AK 55555-2143
###
