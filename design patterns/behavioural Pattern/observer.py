from abc import ABC, abstractmethod
"""
This module implements the Observer design pattern.
Classes:
    Observer(ABC): An abstract base class for observers that defines the update method.
    Subscriber(Observer): A concrete implementation of the Observer that prints received messages.
    Subject: A class that maintains a list of subscribers and notifies them of changes.
    NewsPublisher(Subject): A concrete implementation of the Subject that publishes news.
Usage:
"""

class Observer(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass
    
class Subscriber(Observer):
    def __init__(self, name: str):
        self.name = name
        
    def update(self, message: str) -> None:
        print(f'{self.name} received message: {message}')


class Subject:
    def __init__(self):
        self.subscribers = []
        
    def add_subscriber(self, subscriber: Observer) -> None:
        self.subscribers.append(subscriber)
        
    def remove_subscriber(self, subscriber: Observer) -> None:
        self.subscribers.remove(subscriber)
        
    def notify(self, message: str) -> None:
        for subscriber in self.subscribers:
            subscriber.update(message)
            
            
class NewsPublisher(Subject):
    def __init__(self):
        super().__init__()
        self.news = None
        
    def set_news(self, news: str) -> None:
        self.news = news
        self.notify(news)
        
        
if __name__ == "__main__":
    news_publisher = NewsPublisher()
    
    subscriber1 = Subscriber('Subscriber 1')
    subscriber2 = Subscriber('Subscriber 2')
    
    news_publisher.add_subscriber(subscriber1)
    news_publisher.add_subscriber(subscriber2)
    
    news_publisher.set_news('News 1')
    
    news_publisher.remove_subscriber(subscriber2)
    
    news_publisher.set_news('News 2')
    
    print('Done')
    
