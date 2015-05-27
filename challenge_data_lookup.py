def create_lookup(autosuggestion_list):
    max_count = 1000000
    count = 0
    count_safety = 0
    letters_typed = 0
    max_len = 0
    while 1:
        something = 0
        letters_typed = letters_typed + 1
        print format(letters_typed)
        x = 0
        while 1:
            entry = autosuggestion_list[x][0]
            max_len = max([max_len, len(entry)])
            if len(entry) >= letters_typed:
                lookup_letters = entry[0:letters_typed]
                something = something + 1
                count = count + 1
            x = x + 1
            count_safety = count_safety + 1
            if count_safety > max_count:
                print 'breakout 1'
                break
            if x >= len(autosuggestion_list):
                print 'breakout 2'
                break
        if count_safety > max_count:
            print 'breakout 3'
            break
        if something == 0:
            print 'breakout 4'
            break
    print format(something)
    print format(count)
    print format(count_safety)
    return max_len