import smtplib
import os

login = os.getenv('login')
password = os.getenv('password')


text = ('''Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!\n
%website% — это новая версия онлайн-курса по программированию.
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя.\n
Как будет проходить ваше обучение на %website%?\n
→ Попрактикуешься на реальных кейсах.
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей.
Задачи не «сгорят» и не уйдут к другому. После окончания курса у тебя будет 2 месяца, чтобы догнать программу.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят.\n
Регистрируйся → %website%
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
'''.replace('%website%', 'dvmn.org')).replace('%friend_name%', 'Друг')
end_text = text.replace('%my_name%', 'Devman')


way_to_mail = ('''From: pm@cskorp.ru
To: sv@cskorp.ru
Subject: Рассылка Devman
Content-Type: text/plain; charset="UTF-8"; \n\n''' +
 end_text).encode('UTF-8')


server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login,password)
server.sendmail('pm@cskorp.ru','sv@cskorp.ru',way_to_mail)
server.quit()