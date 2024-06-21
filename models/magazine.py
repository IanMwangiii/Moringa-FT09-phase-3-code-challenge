import sqlite3

class Magazine:
    def __init__(self, id, name, category):
        self._id = id
        self._name = name
        self._category = category
        self.save()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    @name.setter
    def name(self, new_name):
        self._name = new_name
        self.update()

    @category.setter
    def category(self, new_category):
        self._category = new_category
        self.update()

    def save(self):
        connection = sqlite3.connect('magazine.db')
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO magazines (id, name, category)
            VALUES (?, ?, ?)
        ''', (self._id, self._name, self._category))
        connection.commit()
        connection.close()

    def update(self):
        connection = sqlite3.connect('magazine.db')
        cursor = connection.cursor()
        cursor.execute('''
            UPDATE magazines
            SET name = ?, category = ?
            WHERE id = ?
        ''', (self._name, self._category, self._id))
        connection.commit()
        connection.close()

    def articles(self):
        connection = sqlite3.connect('magazine.db')
        cursor = connection.cursor()
        cursor.execute('''
            SELECT * FROM articles WHERE magazine_id = ?
        ''', (self._id,))
        articles = cursor.fetchall()
        connection.close()
        return articles

    def contributors(self):
        connection = sqlite3.connect('magazine.db')
        cursor = connection.cursor()
        cursor.execute('''
            SELECT DISTINCT authors.* FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
        ''', (self._id,))
        contributors = cursor.fetchall()
        connection.close()
        return contributors

    def article_titles(self):
        connection = sqlite3.connect('magazine.db')
        cursor = connection.cursor()
        cursor.execute('''
            SELECT title FROM articles WHERE magazine_id = ?
        ''', (self._id,))
        titles = [row[0] for row in cursor.fetchall()]
        connection.close()
        return titles if titles else None

    def contributing_authors(self):
        connection = sqlite3.connect('magazine.db')
        cursor = connection.cursor()
        cursor.execute('''
            SELECT authors.*, COUNT(articles.id) as article_count FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
            GROUP BY authors.id
            HAVING article_count > 2
        ''', (self._id,))
        authors = cursor.fetchall()
        connection.close()
        return authors if authors else None
