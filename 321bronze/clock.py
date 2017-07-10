
clock_nums = ['oh', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['oh', 'ten', 'twenty', 'thirty', 'forty', 'fifty']

def talk(hours, minutes):
    #input checks
    if not hours.isdigit() or not minutes.isdigit():
        return ''
    if int(hours) > 23 or int(minutes) > 59:
        return ''

    time_of_day = 'am' if int(hours) // 12 < 1 else 'pm'
    hours_parsed = clock_nums[int(hours) % 12] if (hours != '00' and hours != '12') else 'twelve'
    if minutes[0] == '1':
        minutes_parsed = teens[int(minutes) % 10]
    elif minutes != '00':
        minutes_parsed = tens[int(minutes[0])] + ' ' + clock_nums[int(minutes[1])]
    else:
        minutes_parsed = ''
    return "It's %s %s %s" % (hours_parsed, minutes_parsed, time_of_day)

time = input("What time is it? ")
try:
    hours, minutes = time.split(':')
    print(talk(hours, minutes))
except Exception as ex:
    print('Check your input!')