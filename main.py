from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Добро пожаловать!</h1><p>Попробуй перейти на /secret, /fact, /info, /news/, /calc/, /coin или /password</p>"

@app.route("/secret")
def secret():
    return "<h1>Ты нашёл тайную страницу!</h1>"

@app.route("/fact")
def fact_route():
    facts = [
        "Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.",
        "Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.",
        "Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.",
        "Согласно исследованию, проведенному в 2019 году, более 60% людей отвечают на рабочие сообщения в своих смартфонах в течение 15 минут после того, как они вышли с работы.",
        "Один из способов борьбы с технологической зависимостью - это поиск занятий, которые приносят удовольствие и улучшают настроение.",
        "Илон Маск утверждает, что социальные сети созданы для того, чтобы удерживать нас внутри платформы, чтобы мы тратили как можно больше времени на просмотр контента.",
        "Илон Маск также выступает за регулирование социальных сетей и защиту личных данных пользователей. Он утверждает, что социальные сети собирают огромное количество информации о нас, которую потом можно использовать для манипулирования нашими мыслями и поведением.",
        "Социальные сети имеют как позитивные, так и негативные стороны, и мы должны быть более осознанными в использовании этих платформ.",
    ]
    fact = random.choice(facts)
    return f"<h1>Случайный факт:</h1> {fact}"

@app.route("/info")
def info_route():
    return "Тут будет информация о тех зависимостях"

@app.route("/news/<number>")
def news_route(number):
    return f"Вы открыли новость под номером {number}"

@app.route("/calc/<number1>+<number2>")
def plus_route(number1, number2):
    return f"{number1} + {number2} = {int(number1) + int(number2)}"


@app.route("/coin")
def coin():
    result = random.choice(["Орел", "Решка"])
    return f"<h1>Бросок монетки:</h1><p>{result}</p>"

@app.route("/password")
def generate_password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    password = ""
    
    for _ in range(20):
        password += random.choice(chars)
    return f"<h1>Ваш новый пароль:</h1> {password}"

@app.route("/image")
def image():
    images = [
        "https://i.pinimg.com/736x/06/da/66/06da6684570eb84d669282ac706844a0.jpg",  # котик
        "https://i.ucrazy.org/files/pics/2021.04/photo16188129903.webp",  # мем
        "https://fact-news.com.ua/wp-content/uploads/7474758.jpg"   # космос
    ]
    selected_image = random.choice(images)
    return f"<h1>Вот случайная картинка!</h1><img src='{selected_image}' width='400'>"

@app.route("/mystery")
def mystery():
    riddle = "Я без языка, а говорю,\nБез крыльев — а летаю,\nБез ушей — а слышу.\nЧто это?"
    answer = "Эхо"
    return f"""
        <h1>Тайное послание</h1>
        <p>Вот тебе загадка:</p>
        <blockquote>{riddle}</blockquote>
        <details>
            <summary>Показать ответ</summary>
            <p><strong>{answer}</strong></p>
        </details>
    """

if __name__ == '__main__':
    app.run(debug = True)

