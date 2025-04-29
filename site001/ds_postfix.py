import streamlit as st



def evaluate_postfix(expression):
    """후위 표기법 수식을 계산하는 함수"""
    stack = []

    for char in expression:
        if char.isdigit():  # 숫자는 스택에 push
            stack.append(int(char))
        else:  # 연산자는 pop 후 연산 수행
            if len(stack) < 2:
                return "수식 오류"
            b = stack.pop()
            a = stack.pop()

            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                if b == 0:
                    return "0으로 나눌 수 없음"
                stack.append(a / b)
            else:
                return "지원되지 않는 연산자"

    return stack[0] if len(stack) == 1 else "수식 오류"


# Streamlit UI 구성
st.title("🧮 후위 표기법 계산기")

# 사용자 입력 받기
expression = st.text_input("후위 표기법 수식을 입력하세요 (예: 35+2*) 한자리 숫자만 계산됨", "")

# 예제 버튼 추가
if st.button("예제 입력"):
    expression = "35+2*"
    st.session_state['expression'] = expression  # 예제 수식 자동 입력

if expression:
    result = evaluate_postfix(expression)
    st.success(f"계산 결과: {result}")
