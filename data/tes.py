from csv import writer

link = ['https://mendeley.com/page']
data = 'urls-copy.csv'

def insert_link(data, link):
    with open(data, 'a+', newline='\n') as file:
        csv_write = writer(file)
        csv_write.writerow(link)
        file.close()

for page_num in range(1, 11):
    link[0] = link[0]+'/{}'.format(page_num)
    insert_link(data, link)
    link = ['https://mendeley.com/page']
    print('link {} inserted'.format(page_num))
