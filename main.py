import func

print("==========================")
print("| 1.경성대 맛집 100곳  |")
print("| 2. 경성대 맛집 50곳 |")
print("| 3. 경성대 맛집 10곳|")
print("| 4. 경성대 맛집 추천|")
print("==========================")

n = input("[원하는 번호를 입력하세요.]: ")
print(f"당신이 입력한 번호는? {n}")

search_query = "경성대 맛집"

if n == "1":
    func.m100(search_query)
elif n == "2":
    func.m50(search_query)
elif n == "3":
    func.m10(search_query)
elif n == "4":
    func.m_random(search_query)
else:
    print("잘못된 번호를 입력하셨습니다.")