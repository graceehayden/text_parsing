import operator
# import dateutil
# from dateutil.parser import parse


class Person():

    def __init__(self, last_name='', first_name='', gender='', fav_color='', dob=''):

        self.last_name = last_name.strip().lstrip()
        self.first_name = first_name.strip().lstrip()

        gender = gender.strip().lstrip()
        if gender == 'M' or gender == 'Male':
            self.gender = 'Male'
        elif gender == 'F' or gender == 'Female':
            self.gender = 'Female'
        else:
            self.gender = 'Unknown'

        self.fav_color = fav_color.strip().lstrip()
        self.dob = dob.strip().lstrip()
        self.line = [self.last_name + self.first_name + self.gender +
                     self.dob + self.fav_color]

    def make_line(self):
        return self.line

    def format_date(self):
        # self.date.replace("-", "/")
        try:
            parsed_date = parse(self.date, dayfirst=True)
        except TypeError:
            pass
        try:
            parsed_date = parse(self.date)
        except TypeError:
            pass
        self.date = parsed_date

    def sort_by_gen_ln(self):
        '''sort by gender (females before males) then by last name ascending'''
        sorted_line = sorted(self.line, key=operator.itemgetter(2, 0))
        return sorted_line

    def sort_by_dob_ln(self):
        ''' sort by birth date, ascending then by last name ascending '''
        sorted_line = sorted(self.line, key=operator.itemgetter(4, 0))
        return sorted_line

    def sort_by_ln_desc(self):
        ''' sort by last name, descending '''
        sorted_line = sorted(self.line, key=operator.itemgetter(0), reverse=True)
        return sorted_line


def parse_text():
    ''' Parses three text files with different formats. Adds all lines to
    common list. Orders lines and formats data for printing.
    '''
    comma_lines = process_file("comma.txt", ',')
    processed_comma_lines = process_comma_file(comma_lines)

    pipe_lines = process_file("pipe.txt", '|')
    processed_pipe_lines = process_pipe_file(pipe_lines)

    space_lines = process_file("space.txt", ' ')
    processed_space_lines = process_space_file(space_lines)

    persons_list = processed_comma_lines + processed_pipe_lines + processed_space_lines

    output_1_sorted = []
    for person in persons_list:
        line = person.sort_by_gen_ln()
        output_1_sorted.append(line)

    output_2_sorted = []
    for person in persons_list:
        line = person.sort_by_gen_ln()
        output_2_sorted.append(line)

    output_3_sorted = []
    for person in persons_list:
        line = person.sort_by_gen_ln()
        output_3_sorted.append(line)

    print('Output 1:')
    for line in output_1_sorted:
        print(line)
    print('Output 2:')
    for line in output_2_sorted:
        print(line)
    print('Output 3:')
    for line in output_3_sorted:
        print(line)


def process_file(file, delimiter):
    raw_data = []
    with open(file, "r") as file:
        for line in file:
            line.split(delimiter)
            raw_data.append(line.strip())
    return raw_data


def process_comma_file(raw_data):
    list = []
    for line in raw_data:
        line.split()
        list.append(Person(last_name=raw_data[0],
                       first_name=raw_data[1],
                       gender=raw_data[2],
                       fav_color=raw_data[3],
                       dob=raw_data[4]))
    return list


def process_pipe_file(raw_data):
    list = []
    for line in raw_data:
        list.append(Person(last_name=line[0],
                           first_name=line[1],
                           gender=line[3],
                           fav_color=line[4],
                           dob=line[5]))
    return list


def process_space_file(raw_data):
    list = []
    for line in raw_data:
        list.append(Person(last_name=line[0],
                           first_name=line[1],
                           gender=line[3],
                           dob=line[4],
                           fav_color=line[5]))
    return list


if __name__ == '__main__':
    parse_text()
