import operator
from datetime import datetime

class Person():

    def __init__(self, last_name='', first_name='', gender='', fav_color='', dob=''):

        self.last_name = last_name
        self.first_name = first_name

        gender = gender
        if gender == 'M' or gender == 'Male':
            self.gender = 'Male'
        elif gender == 'F' or gender == 'Female':
            self.gender = 'Female'
        else:
            self.gender = 'Unknown'

        self.fav_color = fav_color

        formatted_date = datetime.strptime(dob, '%m/%d/%Y')
        self.dob = formatted_date.strftime('%m/%d/%Y')

        self.line = [self.last_name, self.first_name, self.gender,
                    self.dob, self.fav_color]

    def sort_by_gen_ln(self):
        '''sort by gender (females before males) then by last name ascending'''
        sorted_line = sorted(self.line, key=operator.itemgetter(2, 0))
        return sorted_line

    def sort_by_dob_ln(self):
        ''' sort by birth date, ascending then by last name ascending '''
        sorted_line = sorted(self.line, key=operator.itemgetter(3, 0))
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
    processed_comma_lines = process_comma_file(comma_lines, ',')

    pipe_lines = process_file("pipe.txt", '|')
    processed_pipe_lines = process_pipe_file(pipe_lines, '|')

    space_lines = process_file("space.txt", ' ')
    processed_space_lines = process_space_file(space_lines, ' ')

    persons_list = processed_comma_lines + processed_pipe_lines + processed_space_lines

    output_1_sorted = []
    output_2_sorted = []
    output_3_sorted = []
    for line in persons_list:
        output_1_sorted.append(line.sort_by_gen_ln())
        # output_2_sorted.append(line.sort_by_dob_ln())
        output_3_sorted.append(line.sort_by_ln_desc())

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
    ''' read text and split into a list of a list of strings '''
    raw_data = []
    with open(file, "r") as file:
        raw_data = [line.split(delimiter) for line in file]
    return raw_data


def process_comma_file(raw_data, delimiter):
    list = []
    for word in raw_data:
        line = [x.strip() for x in word]
        list.append(Person(last_name=line[0],
                       first_name=line[1],
                       gender=line[2],
                       fav_color=line[3],
                       dob=line[4]))
    return list


def process_pipe_file(raw_data, delimiter):
    list = []
    for word in raw_data:
        line = [x.strip() for x in word]
        line[5] = line[5].replace("-", "/")
        list.append(Person(last_name=line[0],
                           first_name=line[1],
                           gender=line[3],
                           fav_color=line[4],
                           dob=line[5]))
    return list


def process_space_file(raw_data, delimiter):
    list = []
    for word in raw_data:
        line = [x.strip() for x in word]
        line[4] = line[4].replace("-", "/")
        list.append(Person(last_name=line[0],
                           first_name=line[1],
                           gender=line[3],
                           dob=line[4],
                           fav_color=line[5]))
    return list


# def sort_by_gen_ln(list):
#     '''sort by gender (females before males) then by last name ascending'''
#     sorted_lines = sorted(list, key=operator.itemgetter(2, 0))
#     return sorted_lines
#
# def sort_by_dob_ln(list):
#     ''' sort by birth date, ascending then by last name ascending '''
#     sorted_lines = sorted(list, key=operator.itemgetter(0))
#     return sorted_lines
#
# def sort_by_ln_desc(list):
#     ''' sort by last name, descending '''
#     sorted_lines = sorted(list, key=operator.itemgetter(0), reverse=True)
#     return sorted_lines

if __name__ == '__main__':
    parse_text()
