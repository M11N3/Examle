import re

text = '''{Name}, ваша запись измeнeна:
⌚️ {day_month} в {start_time}
👩 {master}
Услуги:
{services}
управление записью {record_link}
{name}, ваша запись измeнeна:
⌚️ {day_month} в {start_time}
👩 {master}
Услуги:
{services}
управление записью {record_link}
'''
list_keys = ["start_time", "day_month", "master", "services", "record_link", "name"]


def is_valid_brace(text):
    brace = re.findall(r"\{|\}", text)
    brace_stack = []

    if len(brace) % 2 != 0:
        return False

    for i in brace:
        if i == "{":
            brace_stack.append(i)
        else:
            try:
                brace_stack.remove("{")
            except ValueError:
                return False
    return True


def validate(text, available_keys):
    if not is_valid_brace(text):
        return "Missing closing or opening brace."

    keys_from_message = re.findall(r'\{(.*?)\}', text)
    invalid_keys = set(keys_from_message) - set(available_keys)
    if len(invalid_keys) != 0:
        return f"Keys: {invalid_keys} is invalid."


if __name__ == "__main__":
    print(validate(text, list_keys))
