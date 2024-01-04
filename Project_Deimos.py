# Project Deimos
# Moons of Planets
# Written by Razorbacky
# 2024.01.05

# TODO: 잘못된 행성의 이름을 입력하더라도 조건문이 제대로 동작하지 않고, 바로 오류 코드 결과를 출력함.
# TODO: 위성의 이름을 입력하면 moons 조건문이 실행되어 ~~은 행성이 아닙니다. 결과를 출력함.
# TODO: 금성과 수성을 조회하면 행성이 아닙니다. 결과를 출력함.
# TODO: 위성이 없거나 아직 발견되지 않았습니다. 는 제대로 동작하지 않음.

import requests

def get_mop(planet):
    url = f"https://api.le-systeme-solaire.net/rest/bodies/{planet.lower()}"
    res_planet = requests.get(url)
    
    if res_planet.status_code == 200:
        data = res_planet.json()        
        if 'moons' in data:
            moons = data['moons']
            if moons:
                print(f"\n{planet}의 위성 :")
                for moon in moons:
                    print(moon['moon'], end=" ")
            else:
                print(f"{planet}은 행성이 아닙니다.")
        else:
            print(f"{planet}에는 위성이 없거나 아직 발견되지 않았습니다.")
    else:
        print("\033[31m" + (f'오류가 발생하였습니다.\n오류 : [{res_planet.status_code}]') + "\033[31m")

print('='*50)
print('Moons of Planets'.center(50))
print('='*50,'\n')

planet = input("행성의 이름을 입력하십시오.  : ")
get_mop(planet)