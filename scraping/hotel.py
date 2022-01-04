import requests


class Hotel():
    def __init__(self, hotelName: str, yadNo: int, regionName: str, stayYear: int, stayMonth: int, stayDay: int, stayCount: int, adultNum: int) -> None:
        self.hotelName = hotelName
        self.yadNo = yadNo
        self.stayYear = stayYear
        self.stayMonth = stayMonth
        self.stayDay = stayDay
        self.stayCount = stayCount
        self.adultNum = adultNum
        self.regionName = regionName
        self.url = self.create_url()

    def create_url(self) -> str:
        url = f"https://www.jalan.net/yad{yadNo}/plan/?screenId=UWW3101&yadNo={yadNo}&reSearchFlg=1&roomCrack=200000&smlCd=272005&distCd=01&stayYear={stayYear}&stayMonth={stayMonth}&stayDay={stayDay}&stayCount={stayCount}&roomCount=1&adultNum={adultNum}"
        return url

    def get_html(self) -> str:
        response = requests.get(self.url)
        html = response.text
        return html
