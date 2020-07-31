from abc import ABC
from typing import Any, Text, Dict, List
import os
import datetime
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from bs4 import BeautifulSoup
import urllib.request
from datetime import date, timedelta, datetime


class ActionChitChat(Action):

    def name(self) -> Text:
        return "action_chitchat"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        intent = tracker.latest_message["intent"].get("name")
        if intent in [
            "ask_age", "ask_attributes", "ask_birthday", "ask_born_place", "ask_diet", "ask_dont_like",
            "ask_family", "ask_felling", "ask_gender", "ask_hate", "ask_health", "ask_help",
            "ask_hobby", "ask_IQ", "ask_job", "ask_live_place", "ask_look_like", "ask_love",
            "ask_love_how", "ask_love_together", "ask_love_when", "ask_love_who", "ask_name", "ask_purpose",
            "blame", "bye", "call", "compliment", "greeting", "say_love", "thanks", "ask_handsome",
            "ask_love_why", "feel_boring", "feel_hungry", "feel_sleep", "feel_tired", "ask_doing", "ask_sing",
            "feeling_thirsty", "feeling_alonely", "feeling_sick", "ask_good_game", "ask_hang_out",
            "feeling_fall_in_love"
        ]:
            dispatcher.utter_message(template="utter_" + intent)

        return []


class ActionAskDatetime(Action):

    def name(self) -> Text:
        return "action_ask_datetime"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        intent = tracker.latest_message["intent"].get("name")
        date_time = datetime.datetime.now()
        if intent == "ask_day":
            mapping_day = ["chủ nhật", "thứ hai", "thứ ba", "thứ tư", "thứ năm", "thứ sáu", "thứ bảy"]
            weekday_id = int(date_time.strftime("%w"))
            weekday_name = mapping_day[weekday_id]
            dispatcher.utter_message(template="utter_ask_day", day=weekday_name)
        elif intent == "ask_date":
            date = date_time.strftime("%d/%m")
            dispatcher.utter_message(template="utter_ask_date", date=date)
        elif intent == "ask_time":
            time = date_time.strftime("%H:%M:%S")
            dispatcher.utter_message(template="utter_ask_time", time=time)
        elif intent == "ask_year":
            year = date_time.strftime("%Y")
            dispatcher.utter_message(template="utter_ask_year", year=year)
        elif intent == "ask_month":
            month = date_time.strftime("%m")
            dispatcher.utter_message(template="utter_ask_month", month=month)
        return []


class ActionFallback(Action):

    def name(self) -> Text:
        return "action_fallback"

    def run(
            self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        dispatcher.utter_message(template="utter_fallback")
        return []


class ActionGoScreen(Action):

    def name(self) -> Text:
        return "action_go_screen"

    def run(
            self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        entities = tracker.latest_message["entities"]
        if entities:
            entity = tracker.latest_message["entities"][0]['value']
            dispatcher.utter_message(template="utter_go_screen", screen_id=entity)
        else:
            dispatcher.utter_message(template="utter_rephrase_screen")
        return []


class ActionFaqUseful(Action):

    def name(self) -> Text:
        return "action_faq_useful"

    def run(
            self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        entities = tracker.latest_message["entities"]
        if entities:
            entity = tracker.latest_message["entities"][0]['value']
            if entity == "item_token_vip":
                dispatcher.utter_message(template="utter_faq_useful_vip")
            elif entity == "item_token_normal":
                dispatcher.utter_message(template="utter_faq_useful_normal")
            else:
                dispatcher.utter_message(template="utter_rephrase_item_type")
                return []
        else:
            dispatcher.utter_message(template="utter_rephrase_item_type")
            return []
        return []


class ActionFaqHow(Action):

    def name(self) -> Text:
        return "action_faq_how"

    def run(
            self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        entities = tracker.latest_message["entities"]
        if entities:
            entity = tracker.latest_message["entities"][0]['value']
            if entity == "item_token_vip":
                dispatcher.utter_message(template="utter_faq_how_vip")
            elif entity == "item_token_normal":
                dispatcher.utter_message(template="utter_faq_how_normal")
            else:
                dispatcher.utter_message(template="utter_rephrase_item_type")
                return []
        else:
            dispatcher.utter_message(template="utter_rephrase_item_type")
            return []
        return []


class ActionFaqGameNumber(Action):

    def name(self) -> Text:
        return "action_faq_game_number"

    def run(
            self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        game_number = 7
        dispatcher.utter_message(template="utter_faq_game_number", game_number=game_number)
        return []


class ActionAskWeather(Action):

    def name(self) -> Text:
        return "action_ask_weather"

    def run(
            self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message["entities"]
        city = {'name': 'HaNoi', 'lat': '21.02', 'lon': '105.84'}
        if entities:
            time = entities[0]['value']
            if time in ['hôm nay', 'nay']:
                req = requests.get(
                    f"https://api.openweathermap.org/data/2.5/weather?q={city['name']}&lang=vi&appid=66725f249dfba97ca43ef06feab73168")
                weathers = req.json().get('weather')
                temperature = req.json().get('main').get('temp') - 273.15
            elif time in ['ngày mai', 'mai']:
                req = requests.get(
                    f"https://api.openweathermap.org/data/2.5/onecall?lat={city['lat']}&lon={city['lon']}&exclude=hourly&appid=66725f249dfba97ca43ef06feab73168&lang=vi")
                weathers = req.json().get('daily')[1].get('weather')
                temperature = req.json().get('daily')[1].get('temp').get('day') - 273.15
            elif time in ['ngày kia', 'kia']:
                req = requests.get(
                    f"https://api.openweathermap.org/data/2.5/onecall?lat={city['lat']}&lon={city['lon']}&exclude=hourly&appid=66725f249dfba97ca43ef06feab73168&lang=vi")
                weathers = req.json().get('daily')[2].get('weather')
                temperature = req.json().get('daily')[2].get('temp').get('day') - 273.15
            else:
                dispatcher.utter_message(template="utter_weather_dont_know")
                return []

            weather_description = []
            for weather in weathers:
                weather_description.append(weather.get('description'))
            weather_description = ', '.join(weather_description)

            dispatcher.utter_message(template="utter_ask_weather", time=time,
                                     description=weather_description, temperature=int(temperature))
        return []


class ActionNotifyBegin(Action):

    def name(self) -> Text:
        return "action_notify_begin"

    def run(
            self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        city = {'name': 'HaNoi', 'lat': '21.02', 'lon': '105.84'}
        req = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city['name']}&lang=vi&appid=66725f249dfba97ca43ef06feab73168")
        weathers = req.json().get('weather')
        temperature = req.json().get('main').get('temp') - 273.15
        weather_description = []
        weather_id = []
        for weather in weathers:
            weather_id.append(weather.get('icon'))
            weather_description.append(weather.get('description'))
        weather_id = ', '.join(weather_id)
        weather_description = ', '.join(weather_description)

        dispatcher.utter_message(template="utter_notify_begin", weather_id=weather_id,
                                 temperature=int(temperature), description=weather_description)
        return []


class ActionQuickChat(Action):

    def name(self) -> Text:
        return "action_quick_chat"

    def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_quick_chat")

        return []


class GetVoice(Action):

    def name(self) -> Text:
        return "action_get_voice"

    def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        service = ['fpt', 'default']
        voice = ["lannhi", "leminh", "myan", "thuminh", "giahuy", "linhsan"]
        key = os.environ.get('FPT_AI_KEY')
        dispatcher.utter_message(template="utter_get_voice", service=service[0], voice=voice[3], key=key)
        return []


def get_lottery_results(date: str):
    all_results = dict()
    document = urllib.request.urlopen(
        'https://xoso.com.vn/kqxs-{day}-{month}-{year}.html'.format(day=date[8:10], month=date[5:7],
                                                                    year=date[0:4])).read().decode('utf-8')
    content = BeautifulSoup(document, features='html.parser')
    divs = content.findAll("div", {"class": "section-content"})

    def more_results(ss):
        results = ""
        for s in ss:
            results = results + s.get_text() + " "
        return results

    def get_results(game, price):
        spans = game.findAll("span", {"class": price})
        results = ''
        for span in spans:
            results += span.get_text()
        return results

    def get_region_results(region, games, spans):
        if len(games) == 2:
            all_results[region] = dict()
            all_results[region][games[0]] = dict()
            all_results[region][games[1]] = dict()

            all_results[region][games[0]]["prize8"] = spans[0].get_text()
            all_results[region][games[1]]["prize8"] = spans[1].get_text()

            all_results[region][games[0]]["prize7"] = spans[2].get_text()
            all_results[region][games[1]]["prize7"] = spans[3].get_text()

            all_results[region][games[0]]["prize6"] = more_results(spans[4:7])
            all_results[region][games[1]]["prize6"] = more_results(spans[7:10])

            all_results[region][games[0]]["prize5"] = spans[10].get_text()
            all_results[region][games[1]]["prize5"] = spans[11].get_text()

            all_results[region][games[0]]["prize4"] = more_results(spans[12:19])
            all_results[region][games[1]]["prize4"] = more_results(spans[19:26])

            all_results[region][games[0]]["prize3"] = more_results(spans[26:28])
            all_results[region][games[1]]["prize3"] = more_results(spans[28:30])

            all_results[region][games[0]]["prize2"] = spans[30].get_text()
            all_results[region][games[1]]["prize2"] = spans[31].get_text()

            all_results[region][games[0]]["prize1"] = spans[32].get_text()
            all_results[region][games[1]]["prize1"] = spans[33].get_text()

            all_results[region][games[0]]["special-prize"] = spans[34].get_text()
            all_results[region][games[1]]["special-prize"] = spans[35].get_text()

        if len(games) == 3:
            all_results[region] = dict()
            all_results[region][games[0]] = dict()
            all_results[region][games[1]] = dict()
            all_results[region][games[2]] = dict()

            all_results[region][games[0]]["prize8"] = spans[0].get_text()
            all_results[region][games[1]]["prize8"] = spans[1].get_text()
            all_results[region][games[2]]["prize8"] = spans[2].get_text()

            all_results[region][games[0]]["prize7"] = spans[3].get_text()
            all_results[region][games[1]]["prize7"] = spans[4].get_text()
            all_results[region][games[2]]["prize7"] = spans[5].get_text()

            all_results[region][games[0]]["prize6"] = more_results(spans[6:9])
            all_results[region][games[1]]["prize6"] = more_results(spans[9:12])
            all_results[region][games[2]]["prize6"] = more_results(spans[12:15])

            all_results[region][games[0]]["prize5"] = spans[15].get_text()
            all_results[region][games[1]]["prize5"] = spans[16].get_text()
            all_results[region][games[2]]["prize5"] = spans[17].get_text()

            all_results[region][games[0]]["prize4"] = more_results(spans[18:25])
            all_results[region][games[1]]["prize4"] = more_results(spans[25:32])
            all_results[region][games[2]]["prize4"] = more_results(spans[32:39])

            all_results[region][games[0]]["prize3"] = more_results(spans[39:41])
            all_results[region][games[1]]["prize3"] = more_results(spans[41:43])
            all_results[region][games[2]]["prize3"] = more_results(spans[43:45])

            all_results[region][games[0]]["prize2"] = spans[45].get_text()
            all_results[region][games[1]]["prize2"] = spans[46].get_text()
            all_results[region][games[2]]["prize2"] = spans[47].get_text()

            all_results[region][games[0]]["prize1"] = spans[48].get_text()
            all_results[region][games[1]]["prize1"] = spans[49].get_text()
            all_results[region][games[2]]["prize1"] = spans[50].get_text()

            all_results[region][games[0]]["special-prize"] = spans[51].get_text()
            all_results[region][games[1]]["special-prize"] = spans[52].get_text()
            all_results[region][games[2]]["special-prize"] = spans[53].get_text()

        if len(games) == 4:
            all_results[region] = dict()
            all_results[region][games[0]] = dict()
            all_results[region][games[1]] = dict()
            all_results[region][games[2]] = dict()
            all_results[region][games[3]] = dict()

            all_results[region][games[0]]["prize8"] = spans[0].get_text()
            all_results[region][games[1]]["prize8"] = spans[1].get_text()
            all_results[region][games[2]]["prize8"] = spans[2].get_text()
            all_results[region][games[3]]["prize8"] = spans[3].get_text()

            all_results[region][games[0]]["prize7"] = spans[4].get_text()
            all_results[region][games[1]]["prize7"] = spans[5].get_text()
            all_results[region][games[2]]["prize7"] = spans[6].get_text()
            all_results[region][games[3]]["prize7"] = spans[7].get_text()

            all_results[region][games[0]]["prize6"] = more_results(spans[8:11])
            all_results[region][games[1]]["prize6"] = more_results(spans[11:14])
            all_results[region][games[2]]["prize6"] = more_results(spans[14:17])
            all_results[region][games[3]]["prize6"] = more_results(spans[17:20])

            all_results[region][games[0]]["prize5"] = spans[20].get_text()
            all_results[region][games[1]]["prize5"] = spans[21].get_text()
            all_results[region][games[2]]["prize5"] = spans[22].get_text()
            all_results[region][games[3]]["prize5"] = spans[23].get_text()

            all_results[region][games[0]]["prize4"] = more_results(spans[24:31])
            all_results[region][games[1]]["prize4"] = more_results(spans[31:38])
            all_results[region][games[2]]["prize4"] = more_results(spans[38:45])
            all_results[region][games[2]]["prize4"] = more_results(spans[45:52])

            all_results[region][games[0]]["prize3"] = more_results(spans[52:54])
            all_results[region][games[1]]["prize3"] = more_results(spans[54:56])
            all_results[region][games[2]]["prize3"] = more_results(spans[56:58])
            all_results[region][games[3]]["prize3"] = more_results(spans[58:60])

            all_results[region][games[0]]["prize2"] = spans[60].get_text()
            all_results[region][games[1]]["prize2"] = spans[61].get_text()
            all_results[region][games[2]]["prize2"] = spans[62].get_text()
            all_results[region][games[3]]["prize2"] = spans[63].get_text()

            all_results[region][games[0]]["prize1"] = spans[64].get_text()
            all_results[region][games[1]]["prize1"] = spans[65].get_text()
            all_results[region][games[2]]["prize1"] = spans[66].get_text()
            all_results[region][games[3]]["prize1"] = spans[67].get_text()

            all_results[region][games[0]]["special-prize"] = spans[68].get_text()
            all_results[region][games[1]]["special-prize"] = spans[69].get_text()
            all_results[region][games[2]]["special-prize"] = spans[70].get_text()
            all_results[region][games[3]]["special-prize"] = spans[71].get_text()

    # get MB lottery results
    mien_bac = divs[0]
    prizes = ['special-prize', 'prize1', 'prize2', 'prize3', 'prize4', 'prize5', 'prize6', 'prize7']
    mb_results = dict()
    #     print(mien_bac)
    for prize in prizes:
        mb_results[prize] = get_results(game=mien_bac, price=prize)
    all_results["mien_bac"] = mb_results

    # get MT lottery results
    mien_trung = divs[3]
    mt_games = [a["title"] for a in mien_trung.table.thead.findAll("a")]
    mt_spans = mien_trung.findAll("span", {"class": "xs_prize1"})
    get_region_results(region="mien_trung", games=mt_games, spans=mt_spans)

    # get MN lottery_results
    mien_nam = divs[2]

    mn_games = [a["title"] for a in mien_nam.table.thead.findAll("a")]
    mn_spans = mien_nam.findAll("span", {"class": "xs_prize1"})
    get_region_results(region="mien_nam", games=mn_games, spans=mn_spans)

    return all_results


def check_have_result(region):
    now = datetime.now()
    if region == "mien_bac":
        if now.hour < 18 or (now.hour == 18 and now.minute < 40):
            return False
        else:
            return True
    elif region == "mien_trung":
        if now.hour < 17 or (now.hour == 17 and now.minute < 40):
            return False
        else:
            return True
    elif region == "mien_nam":
        if now.hour < 16 or (now.hour == 1 and now.minute < 40):
            return False
        else:
            return True


class LotteryResults(Action, ABC):
    def name(self) -> Text:
        return "action_ask_lottery_result"

    def run(
            self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message["entities"]
        results = dict()
        if entities[0]["entity"] == "time":
            region = entities[1]["value"]
            if entities[0]["value"] == "hôm qua":
                day = str(date.today() - timedelta(days=1))
                results = get_lottery_results(date=day)[region]
                dispatcher.utter_message(template="utter_lottery_results", special_prize=results['special-prize'],
                                         prize1=results['prize1'], prize2=results['prize2'],
                                         prize3=results['prize1'], prize4=results['prize4'],
                                         prize5=results['prize5'], prize6=results['prize6'],
                                         prize7=results['prize7'], date=day)
            elif entities[0]["value"] == "hôm nay":
                day = str(date.today())
                if check_have_result(region):
                    utter

        else:
            region = entities[0]["value"]
            if entities[1]["value"] == "hôm qua":
                day = str(date.today() - timedelta(days=1))
                results = get_lottery_results(date=day)[region]
                dispatcher.utter_message(template="utter_lottery_results", special_prize=results['special-prize'],
                                         prize1=results['prize1'], prize2=results['prize2'],
                                         prize3=results['prize1'], prize4=results['prize4'],
                                         prize5=results['prize5'], prize6=results['prize6'],
                                         prize7=results['prize7'], date=day)
            elif entities[1]["value"] == "hôm nay":
                day = str(date.today())

        return []


class TakeScreenshot(Action):
    def name(self) -> Text:
        return "action_take_screenshot"

    def run(
            self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_take_screenshot")
        return []
