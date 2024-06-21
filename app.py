from models.author import Author
from models.magazine import Magazine
from models.article import Article

def main():
    author1 = Author(1, "John Doe")
    author2 = Author(2, "Jane Smith")
    author3 = Author(3, "Alice Green")
    author4 = Author(4, "Bob Brown")
    author5 = Author(5, "Cathy White")

    magazine1 = Magazine(1, "Tech Today", "Technology")
    magazine2 = Magazine(2, "Health Weekly", "Health")
    magazine3 = Magazine(3, "Travel Explorer", "Travel")
    magazine4 = Magazine(4, "Science Daily", "Science")

    article1 = Article(author1.id, magazine1.id, "The Future of AI")
    article2 = Article(author2.id, magazine2.id, "Healthy Living")
    article3 = Article(author3.id, magazine3.id, "Exploring the World")
    article4 = Article(author3.id, magazine3.id, "Adventure Awaits")
    article5 = Article(author4.id, magazine4.id, "Physics Wonders")
    article6 = Article(author5.id, magazine4.id, "Chemistry Magic")

    print("Author 1 Articles:", author1.articles())
    print("Author 3 Articles:", author3.articles())
    print("Author 3 Magazines:", author3.magazines())

    print("Magazine 3 Articles:", magazine3.articles())
    print("Magazine 3 Contributors:", magazine3.contributors())
    print("Magazine 4 Article Titles:", magazine4.article_titles())
    print("Magazine 4 Contributing Authors:", magazine4.contributing_authors())

if __name__ == "__main__":
    main()
