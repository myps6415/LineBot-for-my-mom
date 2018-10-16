from line_bot_api import *
from crawler.city_weather_card import *

def hualien_event(event):
    line_bot_api.reply_message(
        event.reply_token,
        ImageSendMessage(
            original_content_url= hualien_crawler(),
            preview_image_url= hualien_crawler()))

def taipei_event(event):
    line_bot_api.reply_message(
        event.reply_token,
        ImageSendMessage(
            original_content_url= taipei_crawler(),
            preview_image_url= taipei_crawler()))

def newtaipei_event(event):
    line_bot_api.reply_message(
        event.reply_token,
        ImageSendMessage(
            original_content_url= newtaipei_crawler(),
            preview_image_url= newtaipei_crawler()))

def taoyuan_event(event):
    line_bot_api.reply_message(
        event.reply_token,
        ImageSendMessage(
            original_content_url= taoyuan_crawler(),
            preview_image_url= taoyuan_crawler()))

def kaohsiung_event(event):
    line_bot_api.reply_message(
        event.reply_token,
        ImageSendMessage(
            original_content_url= kaohsiung_crawler(),
            preview_image_url= kaohsiung_crawler()))

def hsinchu_event(event):
    line_bot_api.reply_message(
        event.reply_token,
        ImageSendMessage(
            original_content_url= hsinchu_crawler(),
            preview_image_url= hsinchu_crawler()))

def taichung_event(event):
    line_bot_api.reply_message(
        event.reply_token,
        ImageSendMessage(
            original_content_url= taichung_crawler(),
            preview_image_url= taichung_crawler()))

def chiayi_event(event):
    line_bot_api.reply_message(
        event.reply_token,
        ImageSendMessage(
            original_content_url= chiayi_crawler(),
            preview_image_url= chiayi_crawler()))

def author_event(event):
    line_bot_api.reply_message(
        event.reply_token,
        [TextSendMessage(text= '大帥哥'),
         ImageSendMessage(
             original_content_url= 'https://miro.medium.com/max/2400/1*MJ85coWu1hMGeOib4gPUpA@2x.jpeg',
             preview_image_url= 'https://miro.medium.com/max/2400/1*MJ85coWu1hMGeOib4gPUpA@2x.jpeg'
         )]
    )

def else_event(event):
    line_bot_api.reply_message(
        event.reply_token,
        [TextSendMessage(text= '親愛的用戶您好，本機器人目前僅支援輸入：'),
        TextSendMessage(text= '花蓮、台北、新北、桃園、高雄、新竹、台中、嘉義、作者')]
    )