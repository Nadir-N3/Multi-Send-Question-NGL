import requests
import uuid
import datetime
import colorama
from colorama import Fore, Style
from pyfiglet import Figlet

colorama.init()

def generate_cookie():
    stripe_mid = str(uuid.uuid4()) + str(uuid.uuid4())[:8]
    stripe_sid = str(uuid.uuid4()) + str(uuid.uuid4())[:8]
    ga = f"GA1.1.{random.randint(1000000000, 9999999999)}.{int(datetime.datetime.now().timestamp())}"
    ga_5dv = f"GS2.1.s{int(datetime.datetime.now().timestamp())}$o1$g1$t{int(datetime.datetime.now().timestamp())+7}$j{random.randint(40, 60)}$l0$h0"
    device_id = str(uuid.uuid4())
    mixpanel = f"%7B%22distinct_id%22%3A%22%24device%3A{device_id}%22%2C%22%24device_id%22%3A%22{device_id}%22%2C%22%24initial_referrer%22%3A%22%24direct%22%2C%22%24initial_referring_domain%22%3A%22%24direct%22%2C%22__mps%22%3A%7B%7D%2C%22__mpso%22%3A%7B%22%24initial_referrer%22%3A%22%24direct%22%2C%22%24initial_referring_domain%22%3A%22%24direct%22%7D%2C%22__mpus%22%3A%7B%7D%2C%22__mpa%22%3A%7B%7D%2C%22__mpu%22%3A%7B%7D%2C%22__mpr%22%3A%5B%5D%2C%22__mpap%22%3A%5B%5D%7D"
    return f"_ga={ga}; __stripe_mid={stripe_mid}; __stripe_sid={stripe_sid}; mp_e8e1a30fe6d7dacfa1353b45d6093a00_mixpanel={mixpanel}; _ga_5DV1ZR5ZHG={ga_5dv}"

def read_questions():
    try:
        with open("question.txt", "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"{Fore.RED}✗ File question.txt tidak ditemukan!{Style.RESET_ALL}")
        return []

def submit_question(username, question, device_id):
    url = "https://ngl.link/api/submit"
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "ja,en-US;q=0.9,en;q=0.8",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "cookie": generate_cookie(),
        "origin": "https://ngl.link",
        "priority": "u=1, i",
        "referer": f"https://ngl.link/{username}",
        "sec-ch-ua": '"Not;A=Brand";v="99", "Microsoft Edge";v="139", "Chromium";v="139"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0",
        "x-requested-with": "XMLHttpRequest"
    }
    data = {
        "username": username,
        "question": question,
        "deviceId": str(uuid.uuid4()),
        "gameSlug": "",
        "referrer": f"username={username}&question={question}&deviceId={device_id}&gameSlug=&referrer="
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        print(f"{Fore.GREEN}✔ Pertanyaan '{question}' berhasil dikirim untuk {username}!{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}✗ Gagal mengirim pertanyaan '{question}' untuk {username}!{Style.RESET_ALL}")

def main():
    figlet = Figlet(font='standard')
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"""{Fore.LIGHTBLUE_EX}{figlet.renderText('NADIR.FX')}{Fore.MAGENTA}Welcome to Nadir Terminal{Fore.GREEN}\nReady to hack the world?{Fore.YELLOW}\nCurrent time: {current_time}{Style.RESET_ALL}\n""")
    user_input = input(f"{Fore.GREEN}Masukkan link atau username: {Style.RESET_ALL}").strip()
    username = user_input.split('/')[-1] if 'ngl.link' in user_input else user_input
    if not username:
        print(f"{Fore.RED}✗ Username tidak boleh kosong!{Style.RESET_ALL}")
        return
    questions = read_questions()
    if not questions:
        print(f"{Fore.RED}✗ Tidak ada pertanyaan di question.txt!{Style.RESET_ALL}")
        return
    device_id = str(uuid.uuid4())
    for question in questions:
        submit_question(username, question, device_id)

if __name__ == "__main__":
    import random
    main()
