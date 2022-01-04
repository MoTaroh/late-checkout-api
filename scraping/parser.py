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
        soup = BeautifulSoup(html, 'html.parser')
        # プラン情報取得
        plan_name_list = soup.select(".p-searchResultItem__catchPhrase")
        checkin_out_list = soup.select(".p-checkInOut__value")
        plan_details_list = soup.select(".p-searchResultItem__planTable")
        # 空白や改行などを削除
        checkin_out_list = [re.sub(r"\s", "", t.string).replace('～', '')
                            for t in checkin_out_list]
        # チェックアウト時間が指定時間より遅いものを抽出
        plans = []
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
                    "checkInTime": checkin_out_list[index],
                    "checkOutTime": checkin_out_list[index+1],
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

    def is_late(self, checkout_time: str, wish_time: str = "18:00") -> bool:
        """チェックアウト時間がレイトチェックアウトに該当するかを判定する関数

        Args:
            checkout_time (str): 取得したプランのチェックアウト時間
            wish_time (str, optional): レイトチェックアウトの基準となる時間. Defaults to "18:00".

        Returns:
            bool: レイトチェックアウトの場合True
        """

        wish_time = datetime.strptime(wish_time, "%H:%M")
        checkout_time = datetime.strptime(checkout_time, "%H:%M")
        print(checkout_time, wish_time)
        if checkout_time >= wish_time:
            return True
        else:
            return False
