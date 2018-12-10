import operator


def parse_text():
    ''' Pareses three text files with different formats. Adds all lines to
    common list. Orders lines and formats data for printing.
    Comma-separated text format: LN, FN, gen, M/D/Y, fav color
    Pipe-separated text format: LN, FN, MI, gen, fav color, M-D-Y
    Space-separated text format:  Format: LN, FN, MI, gen, M-D-Y, fav color
    '''
    split_lines = []
    with open("comma.txt", "r") as comma_file:
        for line in comma_file:
            line = line.split(',')
            split_lines.append(line)

    with open("pipe.txt", "r") as pipe_file:  # Format:
        pipe_lines = []
        for line in pipe_file:
            line = line.split("|")
            del line[2]
            line[4] = line[4].replace("-", "/") # date display
            pipe_lines.append(line)
        split_lines.extend(pipe_lines)

    # switch order of color, DOB, so it's DOB, color for comma and pipe texts
    for line in split_lines:
        line[3], line[4] = line[4], line[3]

    with open("space.txt", "r") as space_file: #
        space_lines = []
        for line in space_file:
            line = line.split(" ")
            del line[2]
            dob = line[3].lstrip()
            line[3] = line[3].replace("-", "/") # date display
            space_lines.append(line)
        split_lines.extend(space_lines)

    formatted_lines = []
    for line in split_lines:
        last_name = line[0].strip().lstrip()
        first_name = line[1].strip().lstrip()
        gender = line[2].strip().lstrip()
        dob_mdcy = line[3].strip().lstrip()
        fav_color = line[4].strip().lstrip()
        formatted_line = [last_name, first_name, gender, dob_mdcy, fav_color]

        formatted_lines.append(formatted_line)

    for line in formatted_lines:  # translate gender for display
        line[2] = translate_gender(line[2])

    # sort by gender (females before males) then by last name ascending
    output_1_sorted_lines = sorted(formatted_lines, key=operator.itemgetter(2, 0))
    # sort by birth date, ascending then by last name ascending
    output_2_sorted_lines = sorted(formatted_lines, key=operator.itemgetter(4, 0))
    # sort by last name, descending
    output_3_sorted_lines = sorted(formatted_lines, key=operator.itemgetter(0),
                                  reverse=True)

    output_1_parsed = []
    for line in output_1_sorted_lines:
        output_1_parsed.append(' '.join(line))

    output_2_parsed = []
    for line in output_2_sorted_lines:
        output_2_parsed.append(' '.join(line))

    output_3_parsed = []
    for line in output_3_sorted_lines:
        output_3_parsed.append(' '.join(line))

    print('Output 1:')
    for line in output_1_parsed:
        print(line)
    print('Output 2:')
    for line in output_2_parsed:
        print(line)
    print('Output 3:')
    for line in output_3_parsed:
        print(line)


def translate_gender(gender):
    if gender == 'M' or gender == 'Male':
        return 'Male'
    elif gender == 'F' or gender == 'Female':
        return 'Female'
    else:
        return 'Unknown'


if __name__ == '__main__':
    parse_text()
