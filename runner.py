from tkinter import *
import json


def save_data():
    orcs = orcs_entry.get("1.0", "end-1c")
    orc_list = orcs.split("\n")

    dictionary = {
        "api_id": api_id.get(),
        "api_hash": api_hash.get(),
        "orcs": orc_list,
        "message": message.get(),
        "number_of_messages": number_of_messages.get()
    }

    json_object = json.dumps(dictionary, indent=4)

    with open("api_config.json", "w") as outfile:
        outfile.write(json_object)

    root.destroy()
    import main


root = Tk()
root.title("Spam the orcs")

api_id = StringVar()
api_hash = StringVar()
message = StringVar()
orcs = StringVar()
number_of_messages = StringVar()


api_id_label = Label(text="api_id:")
api_hash_label = Label(text="api_hash:")
message_label = Label(text="message:")
orcs_label = Label(text="orcs:")
number_of_messages_label = Label(text="numer of messages:")

api_id_label.grid(row=0, column=0, sticky="w")
api_hash_label.grid(row=1, column=0, sticky="w")
message_label.grid(row=2, column=0, sticky="w")
orcs_label.grid(row=3, column=0, sticky="w")
number_of_messages_label.grid(row=4, column=0, sticky="w")

api_id_entry = Entry(textvariable=api_id)
api_hash_entry = Entry(textvariable=api_hash)
message_entry = Entry(textvariable=message)
orcs_entry = Text(root, height=5, width=52)
number_of_messages_entry = Entry(textvariable=number_of_messages)

api_id_entry.grid(row=0, column=1, padx=5, pady=5)
api_hash_entry.grid(row=1, column=1, padx=5, pady=5)
message_entry.grid(row=2, column=1, padx=5, pady=5)
orcs_entry.grid(row=3, column=1, padx=5, pady=5)
number_of_messages_entry.grid(row=4, column=1, padx=5, pady=5)

message_button = Button(text="Save and SPAM!!!", command=save_data)
message_button.grid(row=4, column=1, padx=5, pady=5, sticky="e")

root.mainloop()