from .add_book import add_book_bp
from .search_book import search_book_bp

books_router_list = []
books_router_list.append(add_book_bp)
books_router_list.append(search_book_bp)