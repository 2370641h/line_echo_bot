import os
import sys

from flask import Flask, request, abort

from linebot.v3 import WebhookHandler

from linebot.v3.webhooks import MessageEvent, TextMessageContent, UserSource
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi, TextMessage, ReplyMessageRequest
from linebot.v3.exceptions import InvalidSignatureError

channel_access_token = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
channel_secret = os.environ["LINE_CHANNEL_SECRET"]

if channel_access_token is None or channel_secret is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN and LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)

handler = WebhookHandler(channel_secret)
configuration = Configuration(access_token=channel_access_token)

app = Flask(__name__)


# LINEボットからのリクエストを受け取るエンドポイント
@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError as e:
        abort(400, e)

    return "OK"


import random
import datetime


code_mode=0
# 　返信メッセージを生成する関数
def generate_response(from_user, text):
    global code_mode
    res = []
    res.append(TextMessage(text=f"あー{from_user}さん。。。"))
    if "こん" in text[:2]:
        res.append(TextMessage(text="こんちゃー"))
    elif"服装"in text or "コーデ" in text:
        code_mode=1
        res.append(TextMessage(text="今の季節は春、夏、秋、冬のどれですか？"))
    elif code_mode==1 and"春" in text:
        color_spring=["桜","猫柳","菜の花","若菜","藤紫","柳緑","紅梅","青藤"]
        color_normal=["黒","白","赤","緑","青","黄","オレンジ","ピンク","水","紫","灰"]
        color_season_num = len(color_spring)
        color_normal_num = len(color_normal)
        color_season_ran=random.randrange(color_season_num)
        color_normal_ran=random.randrange(color_normal_num)
        tops_spring=["レザージャケット", "ボリューム袖ブラウス", "ベスト", "ロングシャツ", "ボーダーカットソー", "キルティングコート", "スポーティアウター", "ニット"]
        bottoms_spring = ["プリーツスカート", "デニム", "ワイドパンツ", "タイトスカート", "ワンピース", "スキニー", "キュロット"]
        tops_spring_num=len(tops_spring)
        bottoms_spring_num=len(bottoms_spring)
        tops_ran=random.randrange(tops_spring_num)
        bottoms_ran=random.randrange(bottoms_spring_num)
        res.append(TextMessage(text=f"今日のおすすめコーデは{color_spring[color_season_ran]}色の{tops_spring[tops_ran]}と{color_normal[color_normal_ran]}色の{bottoms_spring[bottoms_ran]}です。ぜひ参考にせて下さい！！"))
        code_mode = 0
    elif code_mode==1 and "夏" in text:
        color_summer = ["露草", "撫子", "砂", "藍鉄", "向日葵", "鈍", "赤銅", "麴","碧緑","紺碧"]
        color_normal = ["黒", "白", "赤", "緑", "青", "黄", "オレンジ", "ピンク", "水", "紫", "灰"]
        color_season_num = len(color_summer)
        color_normal_num = len(color_normal)
        color_season_ran = random.randrange(color_season_num)
        color_normal_ran = random.randrange(color_normal_num)
        tops_summer = ["Tシャツ", "ポロシャツ", "タンクトップ", "カットソー", "ブラウス", "ぺトラム", "ワイシャツ"]
        bottoms_summer = ["プリーツスカート", "デニム", "ワイドパンツ", "タイトスカート", "ワンピース", "スキニー", "キュロット"]
        tops_summer_num = len(tops_summer)
        bottoms_summer_num = len(bottoms_summer)
        tops_ran = random.randrange(tops_summer_num)
        bottoms_ran = random.randrange(bottoms_summer_num)
        res.append(TextMessage(text=f"今日のおすすめコーデは{color_summer[color_season_ran]}色の{tops_summer[tops_ran]}と{color_normal[color_normal_ran]}色の{bottoms_summer[bottoms_ran]}です。ぜひ参考にせて下さい！！"))
        code_mode = 0
    elif code_mode==1 and "秋" in text:
        color_fall = ["赤丹", "栗梅茶", "黄朽葉", "竜胆", "栗鼠", "瞑", "紺子", "京緋","灰青","小豆鼠","左伊多津万"]
        color_normal = ["黒", "白", "赤", "緑", "青", "黄", "オレンジ", "ピンク", "水", "紫", "灰"]
        color_season_num=len(color_fall)
        color_normal_num=len(color_normal)
        color_season_ran = random.randrange(color_season_num)
        color_normal_ran = random.randrange(color_normal_num)
        tops_fall = ["Tシャツ", "ポロシャツ", "パーカー", "ベスト", "ブラウス", "トレーナー", "ワイシャツ"]
        bottoms_fall = ["フレアスカート", "デニム", "ワイドパンツ", "タイトスカート", "ワンピース", "スキニー", "キュロット","スラックス"]
        tops_fall_num = len(tops_fall)
        bottoms_fall_num = len(bottoms_fall)
        tops_ran = random.randrange(tops_fall_num)
        bottoms_ran = random.randrange(bottoms_fall_num)
        res.append(TextMessage(text=f"今日のおすすめコーデは{color_fall[color_season_ran]}色の{tops_fall[tops_ran]}と{color_normal[color_normal_ran]}色の{bottoms_fall[bottoms_ran]}です。ぜひ参考にせて下さい！！"))
        code_mode = 0
    elif code_mode==1 and "冬" in text:
        color_winter = ["銀灰", "緋銅", "涅", "石板", "留紺", "深緑", "胡粉", "海松","漆黒","紅","藍鼠"]
        color_normal = ["黒", "白", "赤", "緑", "青", "黄", "オレンジ", "ピンク", "水", "紫", "灰"]
        color_season_num=len(color_winter)
        color_normal_num=len(color_normal)
        color_season_ran = random.randrange(color_season_num)
        color_normal_ran = random.randrange(color_normal_num)
        tops_winter = ["セーター", "ニット", "トレーナー", "ベスト", "シャツ", "パーカー", "コート", "ジャケット"]
        bottoms_winter = ["ジーパン", "ワイドパンツ", "フレア", "ワンピース", "スラックス", "バギーパンツ", "ガウチョパンツ"]
        tops_winter_num = len(tops_winter)
        bottoms_winter_num = len(bottoms_winter)
        tops_ran = random.randrange(tops_winter_num)
        bottoms_ran = random.randrange(bottoms_winter_num)
        res.append(TextMessage(
            text=f"今日のおすすめコーデは{color_winter[color_season_ran]}色の{tops_winter[tops_ran]}と{color_normal[color_normal_ran]}色の{bottoms_winter[bottoms_ran]}です。ぜひ参考にせて下さい！！"))
        code_mode=0

    elif "おは" in text:
        res.append(TextMessage(text="おはこんばんわ"))
    elif "何時" in text or "なんじ" in text:
        now = datetime.datetime.now()
        res.append(TextMessage(text=f"今は{now.hour}時{now.minute}分ですよ"))
    else:
        msg_templates = ["ホゲホゲ", "そうねぇ", f"「{text}」って言ったね？"]
        msg_num = len(msg_templates)  # メッセージの数
        idx = random.randrange(msg_num)  # 0からmsg_num-1までの乱数を生成
        res.append(TextMessage(text=msg_templates[idx]))
    return res


# メッセージを受け取った時の処理
@handler.add(MessageEvent, message=TextMessageContent)
def handle_text_message(event):
    # 送られてきたメッセージを取得
    text = event.message.text

    # 返信メッセージの送信
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)

        res = []
        if isinstance(event.source, UserSource):
            # ユーザー情報が取得できた場合
            profile = line_bot_api.get_profile(event.source.user_id)
            # 返信メッセージを生成
            res = generate_response(profile.display_name, text)
        else:
            # ユーザー情報が取得できなかった場合
            # fmt: off
            # 定型文の返信メッセージ
            res = [
                TextMessage(text="ユーザー情報を取得できませんでした。"),
                TextMessage(text=f"メッセージ：{text}")
            ]
            # fmt: on

        # メッセージを送信
        line_bot_api.reply_message_with_http_info(ReplyMessageRequest(reply_token=event.reply_token, messages=res))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
