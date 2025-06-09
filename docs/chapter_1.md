# FastAPI 개발 환경 구축

### ✅ FastAPI 특징

- **비동기 지원**: `async`/`await` 기반으로 높은 성능 제공
- **자동 문서화**: Swagger (OpenAPI)와 ReDoc 문서 자동 생성
- **타입 힌트 기반**: 타입 안정성과 IDE 자동 완성 지원
- **빠른 개발**: 직관적인 코드와 빠른 API 구축
- **Pydantic 기반**: 데이터 검증 및 직렬화 자동화

---

### ✅ FastAPI vs Django vs Flask

| 항목        | FastAPI            | Django               | Flask              |
| ----------- | ------------------ | -------------------- | ------------------ |
| 성능        | 매우 빠름 (비동기) | 느림 (동기)          | 보통 (동기)        |
| 개발 속도   | 빠름               | 빠름                 | 빠름               |
| 문서화      | 자동 (Swagger)     | 수동                 | 수동               |
| 데이터 검증 | 자동 (Pydantic)    | Form 기반            | 수동 또는 외부 lib |
| 사용 목적   | API 서버 최적화    | 풀스택 웹 프레임워크 | 간단한 API 서버    |

---

### ✅ Starlette & Pydantic 장점

- **Starlette** (FastAPI의 core ASGI 서버):

  - 고성능 비동기 처리
  - WebSocket, 미들웨어, 라우팅 지원

- **Pydantic**:

  - 데이터 타입 검증 및 직렬화
  - 직관적이고 타입 안정성 제공

---

### ✅ uv로 FastAPI 개발 환경 구성

```bash
uv init app
source venv/bin/activate
uv add fastapi --extra standard
uv run fastapi dev
```

---

### ✅ Docker로 MySQL 실행 예시

```yaml
# docker-compose.yml
version: '3.8'
services:
  db:
    image: mysql:8
    container_name: mysql_local
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: $MYSQL_ROOT_PASSWORD
      MYSQL_DATABASE: $MYSQL_DATABASE
      MYSQL_USER: $MYSQL_USER
      MYSQL_PASSWORD: $MYSQL_PASSWORD
    ports:
      - '3306:3306'
    volumes:
      - mysql_data:/var/lib/mysql

volumes:
  mysql_data:
```
