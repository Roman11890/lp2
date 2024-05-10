bimar_dict = {
            'doctor appointment':'your appointment is fixed today call to know time',
            'blood test': 'your appointment is fixed today, reports will be mailed by 2 days', 
            'x ray':'your appointment will be fixed as you visit', 
            'sonography':'your appointment  will be fixed as you visit' ,
}

# hospital ki appointment ya ko servise chaiye jese blood rep ,xray, sonography etc
def handle_request(user_input):
 if user_input.lower() == "Your responses are saved":
    return "Goodbye! Get well soon"
 elif user_input in bimar_dict:
    return bimar_dict[user_input]
 else:
    return "I'm sorry, I don't know how to help with that problem."
# Main loop to prompt user for input
while True:
 user_input = input("What service or consultancy do you want? Type 'exit' to quit. ")
 response = handle_request(user_input)
 print(response)