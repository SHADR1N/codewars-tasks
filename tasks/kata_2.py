

def format_duration(seconds):
    if seconds == 0:
        return "now"

    years = seconds // (365 * 24 * 3600)
    days = (seconds // (24 * 3600)) % 365
    hours = (seconds // 3600) % 24
    minutes = (seconds // 60) % 60
    seconds = seconds % 60

    time_units = []
    if years > 0:
        time_units.append("{} year{}".format(years, 's' if years > 1 else ''))
    if days > 0:
        time_units.append("{} day{}".format(days, 's' if days > 1 else ''))
    if hours > 0:
        time_units.append("{} hour{}".format(hours, 's' if hours > 1 else ''))
    if minutes > 0:
        time_units.append("{} minute{}".format(minutes, 's' if minutes > 1 else ''))
    if seconds > 0:
        time_units.append("{} second{}".format(seconds, 's' if seconds > 1 else ''))

    if len(time_units) == 1:
        return time_units[0]
    elif len(time_units) == 2:
        return time_units[0] + " and " + time_units[1]
    else:
        return ", ".join(time_units[:-1]) + " and " + time_units[-1]
