import csv
import sys
from tqdm import tqdm

maxInt = sys.maxsize
csv.field_size_limit(maxInt)

with open('lastfm/userid-timestamp-artid-artname-traid-traname.tsv', encoding="utf8") as tsvfile:
  reader = csv.reader(tsvfile, delimiter='\t')
  ctr = 0
  with open('lastfm/music_session_2.csv', 'w', encoding=("utf-8"), newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(["session_id", "item_id", "timestamp"])
    for index, row in tqdm(enumerate(reader)):
      # print(row[0], row[1], row[2])
      if index >= 10000000:
        break
      if len(row) < 6:
        # print(len(row))
        pass
      else:

        writer.writerow([row[0], row[2], row[1]])
      ctr+=1
  
