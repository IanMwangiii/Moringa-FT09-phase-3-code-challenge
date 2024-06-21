import unittest
from models.author import Author
from models.magazine import Magazine
from models.article import Article
import sqlite3

class TestModels(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        connection = sqlite3.connect('magazine.db')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM articles')
        cursor.execute('DELETE FROM authors')
        cursor.execute('DELETE FROM magazines')
        connection.commit()
        connection.close()

    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.id, 1)
        self.assertEqual(author.name, "John Doe")

    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Today", "Technology")
        self.assertEqual(magazine.id, 1)
        self.assertEqual(magazine.name, "Tech Today")
        self.assertEqual(magazine.category, "Technology")

    def test_article_creation(self):
        author = Author(2, "Jane Smith")
        magazine = Magazine(2, "Health Weekly", "Health")
        article = Article(author.id, magazine.id, "Healthy Living")
        self.assertEqual(article.title, "Healthy Living")
        self.assertEqual(article.author[1], "Jane Smith")
        self.assertEqual(article.magazine[1], "Health Weekly")

    def test_author_articles(self):
        author = Author(3, "Alice Green")
        magazine = Magazine(3, "Travel Explorer", "Travel")
        article1 = Article(author.id, magazine.id, "Exploring the World")
        article2 = Article(author.id, magazine.id, "Adventure Awaits")
        self.assertEqual(len(author.articles()), 2)

    def test_magazine_contributors(self):
        author1 = Author(4, "Bob Brown")
        author2 = Author(5, "Cathy White")
        magazine = Magazine(4, "Science Daily", "Science")
        article1 = Article(author1.id, magazine.id, "Physics Wonders")
        article2 = Article(author2.id, magazine.id, "Chemistry Magic")
        self.assertEqual(len(magazine.contributors()), 2)

if __name__ == '__main__':
    unittest.main()
