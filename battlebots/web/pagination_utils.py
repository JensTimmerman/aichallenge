from math import ceil

from flask import request


MATCHES_PAGINATION_WINDOW_SIZE = 50

class Paginated(object):
    def __init__(self, query, step=MATCHES_PAGINATION_WINDOW_SIZE):
        self.page = self.get_current_page()
        self.step = step

        fro, to = self.calculate_slice_range()
        self.items = query.slice(fro, to)
        self.total_item_count = query.count()


    @property
    def is_first_page(self):
        return self.current_page <= 1


    @property
    def is_last_page(self):
        return self.current_page == total_pages


    @property
    def total_pages(self):
        return int(ceil(self.total_item_count / float(self.step)))


    def get_current_page(self):
        try:
            page = int(request.args.get('p', 1))
        except ValueError:
            page = 1

        return page


    def calculate_slice_range(self):
        return self.step*(self.page-1), self.step*self.page


def paginate(query, step=MATCHES_PAGINATION_WINDOW_SIZE):
    return Paginated(query, step)
