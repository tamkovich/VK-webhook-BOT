import command_system


def timetable():
    filepath = "files/"
    message = "Свежее расписание"
    file = f"{filepath}rude.jpg"
    return message, "", file


timetable_command = command_system.Command()

timetable_command.keys = ["расписание", "62492", "уроки", "пары"]
timetable_command.description = "Отошлю тебе расписание"
timetable_command.file = True
timetable_command.process = timetable
