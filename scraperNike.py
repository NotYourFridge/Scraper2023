from scrapingbee import ScrapingBeeClient


client = ScrapingBeeClient(
    api_key='GTDQLS41MQ34TMJ24ZB7GAW7DRJ57C6AXFZ4V05OQBE886RIBBJKGVR9GCFFQU96QKMTP6K4V4TBYKIT')

file = open('reviewsNike.txt', 'wt')
for num in range(0, 500, 100):
    print("loading...")
    print('https://cdn-ws.turnto.com/v5/sitedata/w42wYsFH9Jdgqklsite/554724/d/review/nl_NL/10/' + str(num) + '/%7B%7D/RECENT/true/false/?')
    response = client.get('https://cdn-ws.turnto.com/v5/sitedata/w42wYsFH9Jdgqklsite/554724/d/review/nl_NL/10/' + str(num) + '/%7B%7D/RECENT/true/false/?',
                          params={
                              "render_js": "false"
    }
    )
    file.write(response.content.decode("utf-8").encode('cp850', 'replace').decode('cp850'))
    

file.close()
