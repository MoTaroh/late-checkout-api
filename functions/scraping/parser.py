import re
from datetime import datetime
from bs4 import BeautifulSoup


class Parser:
    def parse(self, html: str):
        """指定されたHTMLをパースし、指定された時間以降まで滞在可能なプラン一覧を取得する

        Args:
            html (str): スクレイピングを行うURL

        Returns:
            list: レイトチェックアウト可能なプラン一覧
        """
        soup = BeautifulSoup(html, "html.parser")
        # プラン情報取得
        plan_name_list = soup.select(".p-searchResultItem__catchPhrase")
        checkin_out_list = soup.select(".p-checkInOut__value")
        plan_details_list = soup.select(".p-searchResultItem__planTable")
        # 空白や改行などを削除
        checkin_out_list = [re.sub(r"\s", "", t.string).replace("～", "").replace("〜", "") for t in checkin_out_list]
        # チェックアウト時間が指定時間より遅いものを抽出
        plans = []
        index = 0
        for p_name, p_details in zip(plan_name_list, plan_details_list):

            if self.is_late(checkin_out_list[index + 1]):
                print("Get late checkout plan: ", re.sub(r"\s", "", p_name.string))
                rooms = [
                    (room.string, room.get("href")) for room in p_details.select("a.p-searchResultItem__planName")
                ]
                total_prices = [
                    re.sub(r"\s", "", price.string) for price in p_details.select(".p-searchResultItem__total")
                ]
                room_list = [
                    {"roomName": room[0], "roomURL": room[1], "roomPrice": price}
                    for room, price in zip(rooms, total_prices)
                ]

                plan = {
                    "planName": re.sub(r"\s", "", p_name.string),
                    "checkInTime": checkin_out_list[index],
                    "checkOutTime": checkin_out_list[index + 1],
                    "roomList": room_list,
                }

                plans.append(plan)
            index += 2

        return plans

    def is_late(self, checkout_time: str, wish_time: str = "18:00") -> bool:
        """チェックアウト時間がレイトチェックアウトに該当するかを判定する関数

        Args:
            checkout_time (str): 取得したプランのチェックアウト時間
            wish_time (str, optional): レイトチェックアウトの基準となる時間. Defaults to "18:00".

        Returns:
            bool: レイトチェックアウトの場合True
        """

        wish_time = datetime.strptime(wish_time, "%H:%M")
        try:
            checkout_time = datetime.strptime(checkout_time, "%H:%M")
        except ValueError as e:
            print(e)
            print("Could not parse time", checkout_time)
            return False

        if checkout_time >= wish_time:
            return True
        else:
            return False
