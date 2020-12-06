from openpyxl import load_workbook
from module import *


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
    
    excel = Xlsx()
    pass