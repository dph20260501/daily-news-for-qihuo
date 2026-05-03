import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class FinancialNewsCollector:
    def __init__(self, url):
        self.url = url

    def collect_news(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            return []
        soup = BeautifulSoup(response.content, 'html.parser')
        news_items = soup.find_all('div', class_='news-item')
        news = []
        for item in news_items:
            title = item.find('h2').text.strip()
            link = item.find('a')['href']
            news.append({'title': title, 'link': link})
        return news

class EmailFormatter:
    def format_news(self, news):
        formatted_news = '<h1>Financial News</h1>'
        for item in news:
            formatted_news += f'<p><a href="{item['link']}">{item['title']}</a></p>'
        return formatted_news

class MailSender:
    def __init__(self, sender_email, receiver_email, smtp_server, smtp_port, password):
        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.password = password

    def send_email(self, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = self.receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.sender_email, self.password)
            server.send_message(msg)

if __name__ == '__main__':
    url = 'https://www.example.com/financial-news'
    collector = FinancialNewsCollector(url)
    news = collector.collect_news()
    formatter = EmailFormatter()
    email_body = formatter.format_news(news)
    mail_sender = MailSender('your_email@example.com', 'recipient@example.com', 'smtp.example.com', 587, 'your_password')
    mail_sender.send_email('Daily Financial News', email_body)