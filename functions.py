import pandas as pd
import csv


def insert_link(file, link):
    with open(file, 'a+', newline='\n') as f:
        csv_write = csv.writer(f)
        csv_write.writerow(link)
        print('link inserted')
        f.close()


def insert_detail(file, detail):
    with open(file, 'a+', newline='\n', encoding="utf-8") as f:
        csv_write = csv.writer(f)
        csv_write.writerow(detail)
        print('detail inserted')
        f.close()

