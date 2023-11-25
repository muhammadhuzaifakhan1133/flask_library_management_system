from .add_book import add_book_bp
from .search_book import search_book_bp
from .borrow_book import borrow_book_bp
from .mark_book_returned import mark_book_returned_bp
from .action_to_book_request import action_to_book_request_bp

books_router_list = []
books_router_list.append(add_book_bp)
books_router_list.append(search_book_bp)
books_router_list.append(borrow_book_bp)
books_router_list.append(action_to_book_request_bp)
books_router_list.append(mark_book_returned_bp)