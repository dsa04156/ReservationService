# 베이스 이미지 설정
FROM python:3.9-slim-buster

# 작업 디렉토리 설정
WORKDIR /app

# 환경 변수 설정
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 의존성 설치
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql \
    libpq-dev

# 필요한 파일 복사
COPY requirements.txt .

# 파이썬 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY . .

# 컨테이너 실행 시 실행할 명령 설정
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]