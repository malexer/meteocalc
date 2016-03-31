import os
import sys

here = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(here, '..')))


from meteocalc import dew_point, heat_index, Temp
