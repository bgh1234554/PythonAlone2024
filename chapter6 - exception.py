#예외 구문 정리
try:
    raise NotImplementedError #미구현 시 사용
except ValueError as exception:
    pass
except IndexError as exception:
    pass
except Exception as exception:
    pass
else: #예외가 없을 때
    pass
finally: #무조건 실행되는 것
    pass