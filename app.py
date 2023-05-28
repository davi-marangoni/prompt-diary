from database import add_event, list_events


menu = """Please select one of the options below:

1) Add an new event.
2) View event's.
3) Exit.

Your selection: """

print("Welcome to the Prompt Diary!")
def prompt_new_event():
    event_content = input("What was the event? ")
    event_data = input("When did it happen (yyyy-mm-dd hh:mm:ss)? ")

    add_event(event_content, event_data)

def view_events(events):
    for event in events:
        print(f"{event[2]}\n {event[1]}\n\n")


while (user_input := input(menu)) != "3":
    if user_input == "1":
        prompt_new_event()
    elif user_input == "2":
        view_events(list_events())
    else:
        print("\nInvalid option, please select another option!\n")










