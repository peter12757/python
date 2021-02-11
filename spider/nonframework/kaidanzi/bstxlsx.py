from openpyxl import load_workbook
from module import *
import json


class Xlsx():
  """
  docstring
  """
  workLock = None 
  httpOrderForm:[] = []

  def __init__(self,httpOrderForm:[]) -> None:
    self.httpOrderForm = httpOrderForm
  
  pass



 




if __name__ == "__main__":
  jsonStr = ""
  with open("./record.json","r") as f:
	  jsonStr = f.read(1000)
  print(jsonStr)
  excel = Xlsx(json.loads(jsonStr,))
  pass