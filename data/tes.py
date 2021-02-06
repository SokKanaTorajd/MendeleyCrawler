from database import DBModel
import pandas as pd


# data = [
#         {
#             "url": 'https://www.mendeley.com/catalogue/189518ae-c7f3-3950-b1a9-472e538777eb',
#             "title": 'Effect of supply chain cultural competence on Thai SMEs performance with mediating role of supply chain technology',
#             "publisher": 'International Journal of Supply Chain Management (2020) 9(1) 215-224',
#             "doc_id": '20507399',
#             "authors": ['Mekhum W', ''],
#             "keywords": ['Performance', 'SMEs', 'Supply chain cultural capabilities', 'Supply chain technology'],
#             "abstract": "Performance is a key indicator for the survival of any business. Organizational culture must have strong liaison with the goals of organizations because it has direct association with organizational performance. Therefore, the core objective of this study was to investigate the influence of supply chain cultural capabilities on the performance of Thai SMEs with the mediation role of supply chain technology adoption. To achieve the objective of this study, the data was collected from the managers of SMEs by using survey questioner approach. Smart-PLS was used to test the hypotheses and analysis of data. Findings of contemporary study highlighted that supply chain cultural capabilities have significant positive influence on the performance of SMEs in Thailand. Furthermore, results indicated that supply chain technology adoption could increase the performance of organizations. Results of this research illuminated that Adaptability and consistency in organizational cultural support in the adoption of supply chain technology and supply chain technology boost up the performance of organization. This research offer new empirical indication that supply chain cultural capabilities are significant for the performance of SMEs in developing countries like Thailand. Though, this research used only cultural capabilities, the other important capabilities of supply chain such as supply chain technological capabilities, would be used in future research."
#         },
#         {
#             'url': 'https://www.mendeley.com/catalogue/9225d55b-8562-3347-b3b5-21e532dbcf82',
#             'title': 'Supply chain technology utilization in Malaysia construction industry',
#             'publisher': 'Jurnal Teknologi (2015) 77(4) 69-75',
#             'doc_id': '10.11113/jt.v77.6044',
#             'authors': ['Udin Z', 'Othman A', 'Ahmad A', ''],
#             'keywords': ['Construction', 'Malaysia', 'Rasch method', 'Supply chain management', 'Supply chain technology'],
#             'abstract': "Supply Chain Technology (SCT) utilization becomes a phenomenon in the construction industry nowadays. The uses of these technologies have shown an improvement in construction business process particularly in planning and designing processes. These improvements significantly affect the performance of Supply Chain Management (SCM) in construction industry. The construction industry is critical for national wealth creation particularly in the developing countries such Malaysia. However, about five percent of construction projects were not able to be completed due to various reasons. Therefore, there is a great interest to find out the level of utilization of SCT within the construction industry, which is believed as a main driver to improve the SCM performance and directly reflect to the construction project performance. The objective of this paper is to identify and highlight the issues and problems associated with the current SCM practices, particularly in the technology utilization among the major players in the Malaysian construction industry. To be more specifically, the type of application system that is being utilized in the Malaysian construction supply chain process will be identified."
#         }]

# details = [
#     "https://www.mendeley.com/catalogue/f85f3983-fccd-3d8e-b167-86c2dcab1b37",
#     "A model to evaluate supply chain technology implementation influence on organizational performance",
#     "Transport (2018) 33(3) 779-792",
#     "10.3846/transport.2018.5468",
#     ['Soltany Z', 'Rostamzadeh R', 'Skrickij V', ''],
#     ['IT enabled', 'Organizational performance', 'Simultaneous factor analysis', 'Structural equation model', 'Supply chain technology'],
#     "Supply Chain Management (SCM) aims to achieve organizational competitiveness. By including SCM paradigm and Information Technology (IT), companies aim to enhance their responsiveness and flexibility, and by changing their operations� strategy, they attempt to improve their competitiveness. This study focuses on the organizational variable, IT capabilities, technological structure, and possible antecedents and their impact on Supply Chain Technology (SCT) implementation. This paper proposes a model to examine the way, which SCT implementation affects IT enabled Organizational Performance (OP). The data were achieved through the questionnaires, and then they were analysed by using Smart PLS 3 program. The data collected from 118 employees in IT sector of Iran�s customs administration provide strong support to the proposed research model. The results of this research showed that SCT implementation has a mediating effect on IT enabled OP improvement. Besides, the study revealed that IT capabilities have the most and organizational variable has the least influence on implementation of SCT. Based on other organization�s situations, they can use the suggested model with a little changes."
# ]

dbmodel = DBModel()
coll_details = 'details'
coll_urls = 'urls'

# list_url = dbmodel.get_urls(database)
# for data in list_url:
#     print(data['url'])


# for d in data:
#     dbmodel.insert_detail(database, coll_details, d)

# dbmodel.insert_detail(database, coll_details, details)

# df = pd.read_csv('urls.csv')
# df = df['url'].to_list()
# print(url)
# for url in df:
#     dbmodel.insert_url(database, coll_urls, url)

# print('data inserted')

url = [
    "https://www.mendeley.com/catalogue/189518ae-c7f3-3950-b1a9-472e538777eb",
    "https://www.mendeley.com/catalogue/f85f3983-fccd-3d8e-b167-86c2dcab1b37",
    "https://www.mendeley.com/catalogue/ee2a011e-7817-31eb-9731-f9c200c5b581",
    "https://www.mendeley.com/catalogue/31947e74-7d21-3d23-9775-c266f848ad1d"]


urls = dbmodel.get_urls()
for u in urls:
    # print(u)
    data = dbmodel.check_docs(coll_details, u['url'])
    if data is False:
        print('ayo crawling')
    else:
        print('ga usah crawling')
    # print(u['url'])
    # print(check_value)
    # if check_value == u['url']:
    #     print(u['url'], 'sudah ada')
    # else:
    #     print('ayo ambil')
    
# url = "https://www.mendeley.com/catalogue/31947e74-7d21-3d23-9775-c266f848ad1d"
# url = "https://www.mendeley.com/catalogue/189518ae-c7f3-3950-b1a9-472e538777eb"
# value = dbmodel.get_data('details', url)
# print(value, type(value))

