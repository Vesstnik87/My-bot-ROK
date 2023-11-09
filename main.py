import telebot
import pyautogui
import keyboard
import os


bot = telebot.TeleBot('6491642674:AAGPDmY4YAnpovkxy_q6-vhQ6R4KqaJk3TE')


@bot.message_handler(commands=['startgame'])
def startGame(message):
    bot.send_message(message.chat.id, 'Проверяю готовность к запуску эмулятора')
    pyautogui.sleep(1)
    path_proverka = 'static/proverka.JPG'
    proverka = pyautogui.locateOnScreen(path_proverka, confidence = 0.85)
    if proverka:
        bot.send_message(message.chat.id, 'Все окна свёрнуты. Запускаю эмулятор.')
        pyautogui.sleep(1)
        path_bluestack = 'static/bluestack.JPG'
        bluestack = pyautogui.locateCenterOnScreen(path_bluestack, confidence = 0.95)
        pyautogui.doubleClick(bluestack)
        pyautogui.sleep(10)
        bot.send_message(message.chat.id, 'Эмулятор запускается')
        pyautogui.sleep(60)
        path_playmarket = 'static/playmarket.JPG'
        playmarket = pyautogui.locateCenterOnScreen(path_playmarket, confidence = 0.9)
        if playmarket:
            bot.send_message(message.chat.id, 'Эмулятор запущен. Запускаю игру.')
        path_rok = 'static/ROK.JPG'
        rok = pyautogui.locateCenterOnScreen(path_rok, confidence = 0.9)
        pyautogui.click(rok)
        pyautogui.sleep(30)
        path_fullscreen = 'static/fullscreen.JPG'
        fullscreen = pyautogui.locateCenterOnScreen(path_fullscreen, confidence = 0.9)
        print(fullscreen)
        pyautogui.click(fullscreen)
        pyautogui.sleep(5)
        photo = pyautogui.screenshot(imageFilename='image.JPG')
        with open('image.JPG', 'rb') as image:
            bot.send_photo(message.chat.id, image)
    else:
        bot.send_message(message.chat.id, 'Нужно свернуть все окна')

@bot.message_handler(commands=['status'])
def main(message):
    path_images = 'static/home_1.JPG'
    status = pyautogui.locateOnScreen(path_images, confidence = 0.9)
    if status:
        bot.send_message(message.chat.id, 'Отряд стоит в поле.')
    else:
        bot.send_message(message.chat.id, 'Отряд занят или он дома.')


@bot.message_handler(commands=['go'])
def attack(message):
    while keyboard.is_pressed("Esc") == False:
        path_images = 'static/home_1.JPG'
        status = pyautogui.locateOnScreen(path_images, confidence=0.9)
        if status:
            path_poisk = 'static/poisk.JPG'
            poisk = pyautogui.locateOnScreen(path_poisk, confidence = 0.9)
            pyautogui.sleep(1)
            pyautogui.click(poisk)
            pyautogui.sleep(1)
            path_knopka_poisk = 'static/knopka_poisk.JPG'
            knopka_poisk = pyautogui.locateOnScreen(path_knopka_poisk, confidence = 0.9)
            pyautogui.click(knopka_poisk)
            pyautogui.sleep(3)
            path_12 = 'static/12.JPG'
            varvar = pyautogui.locateOnScreen(path_12, confidence = 0.9)
            pyautogui.click(varvar)
            pyautogui.sleep(1)
            path_attack = 'static/attack.JPG'
            attack = pyautogui.locateOnScreen(path_attack, confidence = 0.9)
            pyautogui.click(attack)
            pyautogui.sleep(1)
            path_zastrel = 'static/zastrel.JPG'
            zastrel = pyautogui.locateOnScreen(path_zastrel, confidence = 0.9)
            pyautogui.click(zastrel)
            pyautogui.sleep(1)
            path_go = 'static/go.JPG'
            go = pyautogui.locateOnScreen(path_go,confidence = 0.9)
            pyautogui.click(go)
            bot.send_message(message.chat.id, 'Отряд на пути к варвару.')
            pyautogui.sleep(3)
        else:
            bot.send_message(message.chat.id, 'Отряд еще дерётся или идёт к варвару.')
            pyautogui.sleep(30)


@bot.message_handler(commands=['troop'])
def troopOut(message):
    bot.send_message(message.chat.id, 'Эту функцию ты еще не настроил 😂')
bot.polling(none_stop=True)