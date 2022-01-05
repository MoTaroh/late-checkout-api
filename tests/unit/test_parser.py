import pytest
from functions.scraping.parser import Parser


class TestParser:
    def test(self):
        parser = Parser()
        html = """
        <html>
            <head>
              <title>Test</title>
            </head>
            <body>
              <li class="p-planCassette p-searchResultItem js-searchResultItem" data-plancode="03332952">
                                <div class="p-planCassette__header p-searchResultItem__header">
                                    <p class="p-searchResultItem__catchPhrase">
                                        【じゃらん限定35％OFF！】カップル＆女子旅におすすめ！クチコミ4.6以上の朝食バイキング付＜13時アウト＞
                                    </p>
                                    <ul class="p-searchResultItem__labels">
                                        <li class="c-label c-label--blue p-searchResultItem__label">オンラインカード決済可</li>
                                    </ul>
                                </div>
                                <div class="p-planCassette__body p-searchResultItem__body">
                                    <div class="p-planCassette__row">
                                        <div class="p-planCassette__picture">
                                            <a
                                                href="/uw/uwp3200/uww3201init.do?stayYear=2022&amp;stayMonth=1&amp;stayDay=8&amp;stayCount=1&amp;roomCount=1&amp;adultNum=2&amp;distCd=01&amp;yadNo=328778&amp;smlCd=272002&amp;roomCrack=200000&screenId=UWW3101&planCd=03332952&roomTypeCd=0454180&planListNumPlan=23__0&groupBookingFlg="><img
                                                    src="https://cdn.jalan.jp/jalan/images/pictM/Y8/Y328778/Y328778519.jpg"
                                                    width="134" height="101" class="pht-lin01"></a>
                                        </div>
                                        <div class="p-planCassette__summary">
                                            <div>
                                                <dl class="p-planPeriod">
                                                    <dt class="p-planPeriod__head">【予約受付期間】</dt>
                                                    <dd class="p-planPeriod__value">2021年12月15日～2022年01月14日</dd>
                                                </dl>
                                            </div>
                                            <div>
                                                <dl class="p-mealType">
                                                    <dt class="p-mealType__head">食事：</dt>
                                                    <dd class="c-label c-label--meal p-mealType__value">朝のみ</dd>
                                                </dl>
                                                <dl class="p-checkInOut">
                                                    <dt class="p-checkInOut__head">チェックイン</dt>
                                                    <dd class="p-checkInOut__value">
                                                        15:00～
                                                    </dd>
                                                </dl>
                                                <dl class="p-checkInOut u-ml-5">
                                                    <dt class="p-checkInOut__head">チェックアウト</dt>
                                                    <dd class="p-checkInOut__value">
                                                        ～18:00
                                                    </dd>
                                                </dl>
                                            </div>
                                            <p class="p-searchResultItem__description">手作り和惣菜からスムージーまで、健康的で美味しい朝食をお届けします
                                            </p>
                                            <p
                                                class="p-searchResultItem__planView u-mt-5 js-searchResultItem__planView">
                                            </p>
                                        </div>
                                    </div>
                                    <table
                                        class="p-planTable p-searchResultItem__planTable p-searchResultItem__planTable--withPoints">
                                        <tbody>
                                            <tr>
                                                <th
                                                    class="p-searchResultItem__headCell p-searchResultItem__headCell--planName">
                                                    <span class="p-searchResultItem__heading">部屋タイプ・詳細</span>
                                                </th>
                                                <th
                                                    class="p-searchResultItem__headCell p-searchResultItem__headCell--points">
                                                    <span class="p-searchResultItem__pointAndScore">
                                                        <span class="u-d-b">加算予定ポイント</span>

                                                        <span class="u-d-b">
                                                            加算予定スコア<span class="p-tooltip">
                                                                <span
                                                                    class="c-icon c-icon--questionGra p-tooltip__trigger p-searchResultItem__scoreQuestionIcon"
                                                                    onmouseover="sc_customLink('score_explain_hover', false, {eVar56: s.pageName}); return true;">
                                                                    <span class="p-tooltip__balloonOuter b-posBr">
                                                                        <span
                                                                            class="p-tooltip__balloon p-searchResultItem__scoreBalloon">
                                                                            スコアとは、じゃらんステージプログラムのステージ判定に用いる指標です。(国内宿・ホテル予約で1円につき1スコアたまります)<br>
                                                                            スコアをためるとステージがアップし、お得な特典が受けられるようになります。<br>
                                                                            <a href="https://www.jalan.net/theme/jalan_stage_program/index.html?g=900"
                                                                                class="u-d-b u-mt-3 u-ta-r"
                                                                                target="_blank">じゃらんステージプログラムの説明をみる</a>
                                                                        </span>
                                                                    </span>
                                                                </span>
                                                            </span>
                                                        </span>

                                                    </span>
                                                </th>
                                                <th
                                                    class="p-searchResultItem__headCell p-searchResultItem__headCell--numberOfPeople">
                                                    大人1名<span class="p-searchResultItem__headCellBrackets">(税込)</span>
                                                </th>
                                                <th
                                                    class="p-searchResultItem__headCell p-searchResultItem__headCell--total">
                                                    合計<span class="p-searchResultItem__headCellBrackets">(税込)</span>
                                                </th>
                                            </tr>
                                            <tr class="js-searchYadoRoomPlanCd" id="yd328778pc03332952rc0365180">
                                                <td class="p-searchResultItem__planNameCell">
                                                    <div class="p-searchResultItem__planNameAndHorizontalLabels">
                                                        <a class="p-searchResultItem__planName"
                                                            href="/uw/uwp3200/uww3201init.do?stayYear=2022&amp;stayMonth=1&amp;stayDay=8&amp;stayCount=1&amp;roomCount=1&amp;adultNum=2&amp;distCd=01&amp;yadNo=328778&amp;smlCd=272002&amp;roomCrack=200000&screenId=UWW3101&planCd=03332952&roomTypeCd=0365180&planListNumPlan=23_0_1&groupBookingFlg=">禁煙クイーン［17平米/ベッド幅160cm］</a>
                                                    </div>
                                                    <div class="p-searchResultItem__planName">
                                                        <ul class="p-searchResultItem__verticalLabels">
                                                            <li
                                                                class="c-label c-label--room p-searchResultItem__verticalLabel p-searchResultItem__verticalLabel--roomChar5">
                                                                ダブル</li>
                                                        </ul>
                                                    </div>
                                                </td>
                                                <td class="p-searchResultItem__perPersonCell">
                                                    <span class="p-searchResultItem__perPerson">
                                                        5,780円
                                                    </span>
                                                </td>
                                                <td class="p-searchResultItem__totalCell">
                                                    <span class="p-searchResultItem__total">
                                                        11,560円
                                                    </span>
                                                </td>
                                            </tr>
                                            <tr class="js-searchYadoRoomPlanCd" id="yd328778pc03332952rc0407962">
                                                <td rowspan="2" class="p-searchResultItem__planNameCell">
                                                    <div class="p-searchResultItem__planNameAndHorizontalLabels">
                                                        <a class="p-searchResultItem__planName"
                                                            href="/uw/uwp3200/uww3201init.do?stayYear=2022&amp;stayMonth=1&amp;stayDay=8&amp;stayCount=1&amp;roomCount=1&amp;adultNum=2&amp;distCd=01&amp;yadNo=328778&amp;smlCd=272002&amp;roomCrack=200000&screenId=UWW3101&planCd=03332952&roomTypeCd=0407962&planListNumPlan=23_0_2&groupBookingFlg=">禁煙ツイン［17平米/ベッド幅90cm］</a>
                                                    </div>
                                                    <div class="p-searchResultItem__planName">
                                                        <ul class="p-searchResultItem__verticalLabels">
                                                            <li
                                                                class="c-label c-label--room p-searchResultItem__verticalLabel p-searchResultItem__verticalLabel--roomChar5">
                                                                ツイン</li>
                                                        </ul>
                                                    </div>
                                                </td>
                                                <td class="p-searchResultItem__perPersonCell">
                                                    <span class="p-searchResultItem__perPerson">
                                                        5,780円
                                                    </span>
                                                </td>
                                                <td class="p-searchResultItem__totalCell">
                                                    <span class="p-searchResultItem__total">
                                                        11,560円
                                                    </span>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </li>
            </body>
        </html>
        """
        result = parser.parse(html)

        expected = [
            {
                "planName": "【じゃらん限定35％OFF！】カップル＆女子旅におすすめ！クチコミ4.6以上の朝食バイキング付＜13時アウト＞",
                "checkInTime": "15:00",
                "checkOutTime": "18:00",
                "roomList": [
                    {
                        "roomName": "禁煙クイーン［17平米/ベッド幅160cm］",
                        "roomURL": "/uw/uwp3200/uww3201init.do?stayYear=2022&amp;stayMonth=1&amp;stayDay=8&amp;stayCount=1&amp;roomCount=1&amp;adultNum=2&amp;distCd=01&amp;yadNo=328778&amp;smlCd=272002&amp;roomCrack=200000&screenId=UWW3101&planCd=03332952&roomTypeCd=0365180&planListNumPlan=23_0_1&groupBookingFlg=",
                        "roomPrice": "11,560円",
                    },
                    {
                        "roomName": "禁煙ツイン［17平米/ベッド幅90cm］",
                        "roomURL": "/uw/uwp3200/uww3201init.do?stayYear=2022&amp;stayMonth=1&amp;stayDay=8&amp;stayCount=1&amp;roomCount=1&amp;adultNum=2&amp;distCd=01&amp;yadNo=328778&amp;smlCd=272002&amp;roomCrack=200000&screenId=UWW3101&planCd=03332952&roomTypeCd=0407962&planListNumPlan=23_0_2&groupBookingFlg=",
                        "roomPrice": "11,560円",
                    },
                ],
            }
        ]
        assert len(result) == 1
        assert result[0]["planName"] == "【じゃらん限定35％OFF！】カップル＆女子旅におすすめ！クチコミ4.6以上の朝食バイキング付＜13時アウト＞"
        assert result[0]["checkInTime"] == "15:00"
        assert result[0]["checkOutTime"] == "18:00"
        assert len(result[0]["roomList"]) == len(expected[0]["roomList"])
