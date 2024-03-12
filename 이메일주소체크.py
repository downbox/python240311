import re

# 정규 표현식을 사용하여 이메일 주소 유효성 검사 함수 정의
def check_email(email):
    # 이메일 주소 유효성을 확인하는 정규 표현식
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # 주어진 이메일 주소가 정규 표현식과 일치하는지 검사
    if re.search(pattern, email):
        return True
    else:
        return False

# 샘플 이메일 주소 목록
sample_emails = [
    "test.email+alex@leetcode.com",
    "test.email.leet+alex@code.com",
    "test.email@leetcode.com",
    "test@leetcode.com",
    "test@leetcode.co.uk",
    "invalid-email@",
    "invalid@invalid",
    "@no-local-part.com",
    "no-at-sign",
    "test.email@leetcode.comcom"
]

# 샘플 데이터에 대해 이메일 유효성 검사 실행 및 결과 출력
results = {email: check_email(email) for email in sample_emails}

# 검사 결과 출력
for email, is_valid in results.items():
    print(f"{email}: {'Valid' if is_valid else 'Invalid'}")
