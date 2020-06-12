from twilio.rest import Client
from database import get_data, get_phone_numbers

our_number = '+13013217859'

client = Client('AC9a3018137a6b5dd128b44978ff218504', '7056b0ea90b7e5b1b46e071d1d5d9e60')

def create_message(suburb):
	data = get_data()
	for d in data:
		if d['Suburb'] == suburb:
			return f"There has been {d['CaseCount']} new cases of COVID19 in {suburb} today"


def send_messages()
	phone_no = get_phone_numbers()
	cases_data = get_data()

	for data in cases_data:
		for number in phone_no:
			if number['Postcode'] == data['Postcode']:
				for no in number['Phone Numbers']:
					client.messages.create(to=no, from_= our_number,body= create_message(data['Suburb']))