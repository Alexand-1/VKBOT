import requests
from bs4 import BeautifulSoup

class Currency:
    DOLLAR_Rub = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E+&sca_esv=563438282&sxsrf=AB5stBgeFBRWeStbeGRosiGsp8BPsnPSEw%3A1694107666291&ei=Egj6ZPS0Eb-Oi-gPvaKByAo&ved=0ahUKEwj0haTtgpmBAxU_xwIHHT1RAKkQ4dUDCA8&uact=5&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E+&gs_lp=Egxnd3Mtd2l6LXNlcnAiJtC60YPRgNGBINC00L7Qu9C70LDRgNCwINC6INGA0YPQsdC70Y4gMggQABiABBixAzILEAAYgAQYsQMYgwEyCBAAGIAEGLEDMgUQABiABDILEAAYgAQYsQMYgwEyCxAAGIAEGLEDGIMBMgUQABiABDILEAAYgAQYsQMYgwEyBRAAGIAEMgUQABiABEj-I1AAWN4hcAN4AZABAJgBtQGgAccSqgEEMTQuObgBA8gBAPgBAagCFMICBxAjGOoCGCfCAhYQLhgDGI8BGOUCGOoCGLQCGIwD2AEBwgIWEAAYAxiPARjlAhjqAhi0AhiMA9gBAcICBBAjGCfCAgsQABiKBRgKGAEYQ8ICCxAuGIAEGLEDGIMBwgIHECMYigUYJ8ICBxAAGIoFGEPCAhEQLhiABBixAxiDARjHARjRA8ICDRAAGIoFGLEDGIMBGEPCAhAQABiABBgUGIcCGLEDGIMBwgIKEAAYigUYsQMYQ8ICEBAAGIAEGLEDGIMBGEYYggLiAwQYACBBiAYBugYGCAEQARgL&sclient=gws-wiz-serp'
    EURO_Rub = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sca_esv=563438282&sxsrf=AB5stBireFbISXrSv13cmOHIR1bAvnsWvw%3A1694108058878&ei=mgn6ZIqfNeaNi-gPkpml2Ao&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lp=Egxnd3Mtd2l6LXNlcnAiHtC60YPRgNGBINC10LLRgNC-0Log0YDRg9Cx0LvRjioCCAAyBhAAGAcYHjIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHjIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHjIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHkjgHlDdC1i9FHADeAGQAQCYAW-gAYsDqgEDMi4yuAEByAEA-AEBwgIKEAAYRxjWBBiwA8ICChAAGIoFGLADGEPCAggQABgHGB4YCuIDBBgAIEGIBgGQBgo&sclient=gws-wiz-serp'
    POUND_Rub = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D1%84%D1%84%D1%83%D0%BD%D0%B4%D0%B0+%D1%81%D1%82%D0%B5%D1%80%D0%BB%D0%B8%D0%BD%D0%B3%D0%BE%D0%B2%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sca_esv=563438282&sxsrf=AB5stBg_sBVZYQK1RNqi-w9GXJJn-MgeCw%3A1694108077160&ei=rQn6ZNGcCZOYi-gPgqiK4A8&ved=0ahUKEwiRp5mxhJmBAxUTzAIHHQKUAvwQ4dUDCA8&uact=5&oq=%D0%BA%D1%83%D1%80%D1%81+%D1%84%D1%84%D1%83%D0%BD%D0%B4%D0%B0+%D1%81%D1%82%D0%B5%D1%80%D0%BB%D0%B8%D0%BD%D0%B3%D0%BE%D0%B2%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lp=Egxnd3Mtd2l6LXNlcnAiN9C60YPRgNGBINGE0YTRg9C90LTQsCDRgdGC0LXRgNC70LjQvdCz0L7QstC6INGA0YPQsdC70Y4yBxAAGA0YgAQyBxAAGA0YgAQyBxAAGA0YgAQyBxAAGA0YgAQyBxAAGA0YgAQyCBAAGAUYHhgNMggQABgFGB4YDTIIEAAYCBgeGA0yCBAAGAgYHhgNMggQABgIGB4YDUjiH1CQBljSHnACeAGQAQGYAc0BoAGVEKoBBjMuMTMuMbgBA8gBAPgBAcICChAAGEcY1gQYsAPCAg0QABhHGNYEGMkDGLADwgILEAAYigUYkgMYsAPCAgoQABiKBRiwAxhDwgINEAAYDRiABBixAxiDAcICBhAAGAcYHsICEhAAGA0YgAQYsQMYgwEYRhiCAsICChAhGKABGMMEGArCAgQQIRgKwgIMEAAYDRiABBhGGIIC4gMEGAAgQYgGAZAGCg&sclient=gws-wiz-serp'
    YEN_Rub = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B9%D0%B5%D0%BD%D1%8B+%D0%BA++%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sca_esv=563438282&sxsrf=AB5stBh_IgpaTU0EgsiAdTUwIJwXBLh-kQ%3A1694108109498&ei=zQn6ZLeJHs7tkgWniKu4Cw&ved=0ahUKEwj3o8_AhJmBAxXOtqQKHSfECrcQ4dUDCA8&uact=5&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B9%D0%B5%D0%BD%D1%8B+%D0%BA++%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lp=Egxnd3Mtd2l6LXNlcnAiINC60YPRgNGBINC50LXQvdGLINC6ICDRgNGD0LHQu9GOMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBhAAGAcYHjIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgARItBlQ5gZYkBhwAngBkAEAmAFsoAHKBqoBAzcuMrgBA8gBAPgBAcICChAAGEcY1gQYsAPCAg0QABhHGNYEGMkDGLADwgILEAAYigUYkgMYsAPCAg0QABgNGIAEGLEDGIMBwgIHEAAYDRiABOIDBBgAIEGIBgGQBgk&sclient=gws-wiz-serp'
    FRANC_Rub = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D1%84%D1%80%D0%B0%D0%BD%D0%BA%D0%B0%D0%BA++%D1%80%D1%83%D0%B1%D0%BB%D1%8E&sca_esv=563438282&sxsrf=AB5stBgZdZtXcOr-8XhN6KOBmurWCJWjBA%3A1694108126248&ei=3gn6ZKflDoyji-gPgZGOuA0&ved=0ahUKEwinzM3IhJmBAxWM0QIHHYGIA9cQ4dUDCA8&uact=5&oq=%D0%BA%D1%83%D1%80%D1%81+%D1%84%D1%80%D0%B0%D0%BD%D0%BA%D0%B0%D0%BA++%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lp=Egxnd3Mtd2l6LXNlcnAiI9C60YPRgNGBINGE0YDQsNC90LrQsNC6ICDRgNGD0LHQu9GOMgYQABgHGB4yBhAAGAcYHjIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHjIGEAAYBxgeMgYQABgHGB4yBhAAGAcYHjIGEAAYBxgeMgYQABgHGB5IsApQuARYrglwAngBkAEAmAFwoAHaBKoBAzQuMrgBA8gBAPgBAcICChAAGEcY1gQYsAPCAgoQABiKBRiwAxhDwgINEAAYDRiABBixAxiDAcICBxAAGA0YgATiAwQYACBBiAYBkAYK&sclient=gws-wiz-serp'

    headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

#    def __init__(self):
 #       print("Currency object created")

    def get_currency_price(self, currency_url):
        try:
            full_page = requests.get(currency_url, headers=self.headers)
            full_page.raise_for_status()  # Проверяем, что запрос прошел успешно
            soup = BeautifulSoup(full_page.content, 'html.parser')
            convert = soup.findAll('span', {'class': 'DFlfde', 'class': 'SwHCTb', 'data-precision': 2})
            return convert[0].text
        except Exception as e:
            print(f"An error occurred: {e}")
            return "N/A"

    def get_all_currency_prices(self):
        dollar_price = self.get_currency_price(self.DOLLAR_Rub)
        euro_price = self.get_currency_price(self.EURO_Rub)
        pound_price = self.get_currency_price(self.POUND_Rub)
        yen_price = self.get_currency_price(self.YEN_Rub)
        franc_price = self.get_currency_price(self.FRANC_Rub)
        return {
            'Доллар США': dollar_price,
            'Евро': euro_price,
            'Фунт стерлингов': pound_price,
            'Иена': yen_price,
            'Швейцарский франк': franc_price,
        }

    def check_currency(self):
        currency_prices = self.get_all_currency_prices()
        for currency, price in currency_prices.items():
            print(f'{currency}: {price}')


if __name__ == "__main__":
    currency = Currency()
    currency.check_currency()