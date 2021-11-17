import os
import sys

try:
  import colorama
  import sourcedefender
  import zxcpt
except ImportError:
  os.system('pip3 install requirements.txt')
