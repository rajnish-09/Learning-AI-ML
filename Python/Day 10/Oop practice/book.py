# Create Book class with title, author, list of reviews attributes with method to add, count and display reviews

class Book:
    def __init__(self, title, author, reviews):
        self.title = title
        self.author = author
        self.reviews = reviews

    def add_review(self, review):
        self.reviews.append(review)

    def count_review(self):
        print(f"Total reviews: {len(self.reviews)}")

    def display_reviews(self):
        print(f'All reviews: {self.reviews}')
    
b1 = Book("Atomic habit", 'Hari', [])
b1.add_review('It was good')
b1.add_review('It was good')
b1.add_review('It was good')
b1.add_review('It was good')
b1.add_review('I really loved it')
b1.count_review()
b1.display_reviews()