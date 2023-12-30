import pandas as pd 
import sys
sys.path.append('..')  # Add the parent directory to the path

from config2 import YOUTUBE_API_KEY
from googleapiclient.discovery import build


youtube = build('youtube','v3',developerKey=YOUTUBE_API_KEY)

requests = youtube.channels().list(
    part='statistics',
    forUsername='Buders'
    
    
)
response = requests.execute()
print(response)