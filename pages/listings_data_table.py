
class Listings:
    def __init__(self, listing_div):
        self.name = listing_div.find('.//td[1]').text
        self.position = listing_div.find('.//td[2]').text
        self.office = listing_div.find('.//td[3]').text
        self.age = int(listing_div.find('.//td[4]').text)
        self.start_date = listing_div.find('.//td[5]').text
        self.salary = listing_div.find('.//td[6]').text
        self.all = self.name, self.position, self.office, self.age, self.start_date, self.salary




