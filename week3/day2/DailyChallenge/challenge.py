class Pagination:
    def __init__(self, items = None, page_size = 10):
        self.items = items if items is not None else []
        self.page_size = int(page_size) #number of items per page as integers if need be
        self.current_page = 1 # Initialize the current page to 1 (first page)
        self.total_pages = self.get_total_pages() # To calculate total number of pages

    def get_total_pages(self):
        # Calculate & return total number of pages.
        return (len(self.items) + self.page_size - 1) // self.page_size #self.page_size - 1 ensures that any partial page is counted as a full page.

    def get_visible_items(self):
        #Retrieve & return the List of items on the current page.
        start_index = (self.current_page - 1) * self.page_size
        end_index = start_index + self.page_size
        return self.items[start_index:end_index]

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
        return self

    def next_page(self):
        if self.current_page < self.total_pages:
            self.current_page += 1
        return self

    def first_page(self):
        self.currentPage = 1
        return self

    def last_page(self):
        self.current_page = self.total_pages
        return self

    def go_to_page(self, page_num):
        page_num = int(page_num) # To be sure the page number is an integer
        if page_num < 1: # Set currentPage to the closest valid page number
            self.currentPage = 1
        elif page_num > self.total_pages:
            self.currentPage = self.total_pages
        else:
            self.currentPage = page_num
        return self

alphabetList = list("abcdefghijklmnopqrstuvwxyz")

# Initialize the Pagination object with a list of items in 4 pages
p = Pagination(alphabetList, 4)

print("\nFirst page:", p.get_visible_items())  

p.next_page()
print("Next page:", p.get_visible_items())  

p.last_page()
print("Last page:", p.get_visible_items())  

p.go_to_page(3)
print("Page 3:", p.get_visible_items())  

p.prev_page()
print("Previous page:", p.get_visible_items())  

p.first_page().next_page().next_page()
print("Go to page 3:", p.get_visible_items()) 
