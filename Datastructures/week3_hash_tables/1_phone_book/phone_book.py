# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else: # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result

# using a dictionary for the phone book hashing problem
class PhoneBook:
    def __init__(self):
        # dictionary initializer
        self.pb = {}

        # to track number of records
        self.counter = 0

    def add_number(self, number, name):
        # phone book structure [key=number, value name]
        self.pb[number] = name
        self.counter += 1

    def find(self, number):
        # returns not found if not in list alaready
        value = self.pb.get(number, "not found")
        return value

    def delete(self, number):
        if number in self.pb.keys():
            # decrement counter
            self.counter -= 1

            # delete
            a = self.pb.pop(number)

    def process_queries(self, queries):
        result = []
        for cur_query in queries:
            if cur_query.type == 'add':
                self.add_number(cur_query.number, cur_query.name)
            elif cur_query.type == 'del':
                self.delete(cur_query.number)
            else:
                response = self.find(cur_query.number)
                result.append(response)
        return result

if __name__ == '__main__':
    # initialize phone bool
    pb = PhoneBook()
    write_responses(pb.process_queries(read_queries()))

