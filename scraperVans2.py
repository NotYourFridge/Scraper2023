from scrapingbee import ScrapingBeeClient


client = ScrapingBeeClient(
    api_key='GTDQLS41MQ34TMJ24ZB7GAW7DRJ57C6AXFZ4V05OQBE886RIBBJKGVR9GCFFQU96QKMTP6K4V4TBYKIT')

file = open('reviewsVans.txt', 'wt')
for num in range(10, 50, 10):
    print("loading...")
    print('https://display.powerreviews.com/m/106693/l/nl_NL/product/D3H_OldSkool_Ftw/reviews?paging.from='+ str(num) + '&paging.size=10&filters=&search=&sort=Newest&image_only=false&page_locale=nl_NL&_noconfig=true&apikey=f2c524cf-c0c6-4019-b3d4-5f3c5f872067')
    response = client.get('https://display.powerreviews.com/m/106693/l/nl_NL/product/D3H_OldSkool_Ftw/reviews?paging.from='+ str(num) + '&paging.size=10&filters=&search=&sort=Newest&image_only=false&page_locale=nl_NL&_noconfig=true&apikey=f2c524cf-c0c6-4019-b3d4-5f3c5f872067',
                          params={
                              "render_js": "false"
    }
    )
    file.write(response.content.decode("utf-8").encode('cp850', 'replace').decode('cp850'))
    

file.close()




# hdfs impo
# client = hdfs.insecureclient(local:u98875678)
# with open('sneaker_images_decathlon.txt', 'rb') as g:
    # data = g.read
    # client.write(folder hadoop/nameminer, data)


