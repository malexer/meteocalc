import os
import sys

here = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(here, '..')))


from meteocalc import dew_point, feels_like, heat_index, wind_chill, Temp
