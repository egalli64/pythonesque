"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 1: https://codingbat.com/python/Logic-1
alarm_clock: https://codingbat.com/prob/p119867
"""


def alarm_clock(day, vacation):
    """
    Parameters:
        day int [0=Sun .. 6=Sat]
        vacation bool
    return on weekdays "7:00" or "10:00" if vacation;
        on weekend "10:00" of "off" if vacation
    """
    if 1 <= day <= 5:
        return "10:00" if vacation else "7:00"
    else:
        return "off" if vacation else "10:00"
