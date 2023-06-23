from scrapingbee import ScrapingBeeClient


client = ScrapingBeeClient(
    api_key='8FFCR4E3QJ6DFLMO4D55MCWHLTJK5LMC1BHAZ2AIKD7MD4NSD1BLBLDKQY3QWO4DN6NR2Q29EV6IYOCQ')

file = open('reviewsAdidas.txt', 'wt')
for num in range(0, 500, 10):
    print("loading...")
    print('https://www.adidas.nl/api/models/IUU93/reviews?bazaarVoiceLocale=nl_NL&includeLocales=nl%2A&limit=10&offset=' + str(num) + '&sort=newest')
    response = client.get('https://www.adidas.nl/api/models/IUU93/reviews?bazaarVoiceLocale=nl_NL&includeLocales=nl%2A&limit=10&offset=' + str(num) + '&sort=newest',
                          params={
                              "render_js": "false"
    }
    )
    file.write(response.content.decode("utf-8").encode('cp850', 'replace').decode('cp850'))
    

file.close()
