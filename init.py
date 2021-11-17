import os
import sys

try:
  import sourcedefender
  import zxcpt
  import colorama
except ImportError:
  os.system('pip3 install requirements.txt')
