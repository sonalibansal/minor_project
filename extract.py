import datefinder
from commonregex import CommonRegex
import geograpy
import re


class Extractor(object):
  """docstring for ClassName"""
  path = ""
  parsed_text=""
  contents=""

  def setPath(self,p):
    self.path = p
    self.parsedContent()

  def parsedContent(self):
    openObject=open(self.path, "r")
    self.contents = openObject.read()
    self.parsed_text = CommonRegex(self.contents)
   
  def findUserName(self):
    return "Ria Pant"
    
  def findDate(self):
    date = self.parsed_text.dates
    return date[0]

  def findTime(self):
    time = self.parsed_text.times
    return time[0]

  def findAddress(self):
    address=[]      
    regexp1 = "venue[ ]?[:-][ ]?[a-zA-Z0-9,&. -]+"
    if "Venue" in self.contents:
      address =re.findall(regexp1, self.contents.lower())
      address[0] = address[0][5:]
      addressString= address[0]
      addressString.strip()
      addressString = addressString[2:]
      address[0] = addressString
    if not address:
      regexp = "[0-9]{1,3} .+, .+, [A-Z]{2} [0-9]{5}"
      #"[0-9]{1,3} .+, .+, [A-Z]{2} [0-9]{5}"
      address = re.findall(regexp, self.contents)
    if not address:
      regexp = "\d+.+(?=AL|AK|AS|AZ|AR|CA|CO|CT|DE|DC|FM|FL|GA|GU|HI|ID|IL|IN|IA|KS|KY|LA|ME|MH|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|MP|OH|OK|OR|PW|PA|PR|RI|SC|SD|TN|TX|UT|VT|VI|VA|WA|WV|WI|WY)[A-Z]{2}[, ]+\d{5}(?:-\d{4})?"
      #"[0-9]{1,3} .+, .+, [A-Z]{2} [0-9]{5}"
      address = re.findall(regexp, self.contents)
    return address[0]    