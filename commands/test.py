import command_system


def test(content):
    filepath = "files/"
    message = "Test To Test"
    file = f"{filepath}{content}.jpg"
    return message, "", file


test_command = command_system.Command()

test_command.keys = ["/test"]
test_command.description = "напиши название файла после команды"
test_command.file = True
test_command.is_content = True
test_command.process = test
