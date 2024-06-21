import sqlite3

class Author:
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self.save()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def save(self):
        connection = sqlite3.connect('magazine.db')
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO authors (id, name)
            VALUES (?, ?)
        ''', (self._id, self._name))
        connection.commit()
        connection.close()

    def articles(self):
        connection = sqlite3.connect('magazine.db')
        cursor = connection.cursor()
        cursor.execute('''
            SELECT * FROM articles WHERE author_id = ?
        ''', (self._id,))
        articles = cursor.fetchall()
        connection.close()
        return articles

    def magazines(self):
        connection = sqlite3.connect('magazine.db')
        cursor = connection.cursor()
        cursor.execute('''
            SELECT DISTINCT magazines.* FROM magazines
            JOIN articles ON magazines.id = articles.magazine_id
            WHERE articles.author_id = ?
        ''', (self._id,))
        magazines = cursor.fetchall()
        connection.close()
        return magazines
