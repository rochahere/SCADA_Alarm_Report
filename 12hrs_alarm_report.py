import pandas as pd # Creates data frames
from tabulate import tabulate # Shows pretty data frames in terminal
import shutil # Moves and renames directories and files
import glob # Finds all pathnames
import os # Portable way of using operating system dependent functionality
import sys # Stops python script
from secrets import *

# Get the newest file on folder
try:
  # DOWNLOAD_LOCATION = 'HOME/USER/DOWNLOADS/*.XLSX'
  list_of_files = glob.glob(DOWNLOAD_LOCATION)
  downloaded_file = max(list_of_files, key=os.path.getctime)
except:
  print("There is no file with that extension")
  sys.exit()


# Move and rename file location
# FINAL_LOCATION = 
new_location = FINAL_LOCATION
shutil.move(downloaded_file, new_location)

# Set report name
# report = os.path.basename(new_location)
report = new_location

# Set sheet name
sheet_name = MY_SHEET_NAME

# Import file
print(report)
df = pd.read_excel(report, sheet_name=sheet_name)

# Show column names
# print('Raw column names: ')
# print(' ')
# for col in df.columns:
#         print(col)

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')

# Show column names
# print(' ')
# print('Fixed column names:')
# print(' ')
# for col in df.columns:
#         print(col)

# Show data types
# df.dtypes

# Removes not needed columns
df_clean = df[['device','alarm_timestamp','alarm_setpoint','recipients']]

# Create DF for device alarm count
df_device = df_clean[['device', 'alarm_setpoint']]

# df_device.head()

# Group by "device"
device_count = df_device.groupby(['device','alarm_setpoint'])['alarm_setpoint'].count().reset_index(name='count').sort_values(['count'], ascending=False)

# Sort Desc
print(tabulate(device_count.head(10), headers='keys', tablefmt='psql'))