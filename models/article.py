import sqlite3

class Article:
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        self.save()

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        connection = sqlite3.connect('magazine.db')
        cursor = connection.cursor()
        cursor.execute('''
            SELECT * FROM authors WHERE id = ?
        ''', (self._author,))
        author = cursor.fetchone()
        connection.close()
        return author

    @property
    def magazine(self):
        connection = sqlite3.connect('magazine.db')
        cursor = connection.cursor()
        cursor.execute('''
            SELECT * FROM magazines WHERE id = ?
        ''', (self._magazine,))
        magazine = cursor.fetchone()
        connection.close()
        return magazine

    def save(self):
        connection = sqlite3.connect('magazine.db')
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO articles (title, author_id, magazine_id)
            VALUES (?, ?, ?)
        ''', (self._title, self._author, self._magazine))
        connection.commit()
        connection.close()
