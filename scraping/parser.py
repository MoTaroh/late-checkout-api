import re
from bs4 import BeautifulSoup


class Parser:
    def parse(self, html: str):
        soup = BeautifulSoup(html, 'html.parser')
        # プラン情報取得
        plan_name_list = soup.select(".p-searchResultItem__catchPhrase")
        checkin_out_list = soup.select(".p-checkInOut__value")
        plan_details_list = soup.select(".p-searchResultItem__planTable")
        # チェックアウト時間が指定時間より遅いものを抽出
        plans = []
        # 空白や改行などを削除
        checkin_out_list = [re.sub(r"\s", "", t.string)
                            for t in checkin_out_list]
        for index, (p_name, p_details) in enumerate(zip(plan_name_list, plan_details_list)):

            if self.is_late(checkin_out_list[index+1]):
                rooms = [(room.string, room.get("href")) for room in p_details.select(
                    "a.p-searchResultItem__planName")]
                total_prices = [re.sub(r"\s", "", price.string) for price in p_details.select(
                    ".p-searchResultItem__total")]
                room_list = [{"roomName": room[0], "roomURL":room[1], "roomPrice":price}
                             for room, price in zip(rooms, total_prices)]

                plan = {
                    "planName": re.sub(r"\s", "", p_name.string),
                    "checkInTime": checkin_out_list[index].replace('～', ''),
                    "checkOutTime": checkin_out_list[index+1].replace('～', ''),
                    "roomList": room_list
                }

                plans.append(plan)

        # チェックアウト時間が指定した時間より遅ければ、htmlから下記を取得する
        # - プラン名
        # - チェックイン時間
        # - チェックアウト時間
        # - 部屋名
        # - 料金
        print(plans)

        return plans

    def is_late(self, checkout: str) -> bool:
        return True
