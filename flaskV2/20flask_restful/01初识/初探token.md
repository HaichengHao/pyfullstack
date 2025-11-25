是的！在 **前后端分离 + Flask-RESTful** 架构中，**使用 Token（如 JWT）是最推荐、最主流的做法**。它无状态、天然支持跨域、适合多端（Web/App/小程序），且与 RESTful 风格完美契合。

下面给你一个 **完整、可运行、带注释的简单例子**，包含：

- 用户登录 → 返回 JWT Token  
- 受保护接口 → 需携带 Token 才能访问  
- 使用 `Flask-RESTful` 的 CBV（基于类的视图）

---

## 📁 项目结构（极简版）

```
restful_jwt_demo/
├── app.py
└── requirements.txt
```

---

## 1️⃣ 安装依赖（`requirements.txt`）

```txt
Flask
Flask-RESTful
PyJWT
```

安装：
```bash
pip install -r requirements.txt
```

---

## 2️⃣ 核心代码（`app.py`）

```python
# app.py
from flask import Flask, request, jsonify, g
from flask_restful import Api, Resource
import jwt
from datetime import datetime, timedelta
from functools import wraps

# ----------------------------
# 配置
# ----------------------------
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-super-secret-jwt-key'  # 实际项目用环境变量！
api = Api(app)

# 模拟用户数据库（实际用 SQLAlchemy）
USERS = {
    "admin": "123456"
}

# ----------------------------
# 工具函数：生成 JWT Token
# ----------------------------
def generate_token(username):
    payload = {
        'username': username,
        'exp': datetime.utcnow() + timedelta(hours=24)  # 24小时过期
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return token

# ----------------------------
# 装饰器：验证 Token
# ----------------------------
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # 从 Header 中获取 Authorization: <token>
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        
        if not token:
            return {'message': 'Token is missing!'}, 401
        
        try:
            # 解码 Token
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            g.current_user = data['username']  # 存入 Flask 全局 g 对象
        except jwt.ExpiredSignatureError:
            return {'message': 'Token has expired!'}, 401
        except jwt.InvalidTokenError:
            return {'message': 'Token is invalid!'}, 401
        
        return f(*args, **kwargs)
    return decorated

# ----------------------------
# 资源类：登录
# ----------------------------
class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {'message': 'Username and password required!'}, 400

        # 验证用户（实际项目查数据库）
        if username in USERS and USERS[username] == password:
            token = generate_token(username)
            return {
                'message': 'Login successful!',
                'token': token  # 前端保存这个 token
            }, 200
        else:
            return {'message': 'Invalid credentials!'}, 401

# ----------------------------
# 资源类：受保护的用户信息接口
# ----------------------------
class UserProfile(Resource):
    method_decorators = [token_required]  # ← 应用 token 验证装饰器

    def get(self):
        return {
            'message': f'Hello, {g.current_user}!',
            'user_info': {
                'username': g.current_user,
                'role': 'admin'  # 示例数据
            }
        }, 200

# ----------------------------
# 注册路由
# ----------------------------
api.add_resource(Login, '/api/login')
api.add_resource(UserProfile, '/api/profile')

# ----------------------------
# 启动
# ----------------------------
if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

---

## 3️⃣ 如何测试？

### ✅ 步骤 1：登录获取 Token

```bash
curl -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "123456"}'
```

✅ 成功响应：
```json
{
  "message": "Login successful!",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.xxxxx"
}
```

### ✅ 步骤 2：用 Token 访问受保护接口

```bash
curl -X GET http://localhost:5000/api/profile \
  -H "Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.xxxxx"
```

✅ 成功响应：
```json
{
  "message": "Hello, admin!",
  "user_info": {
    "username": "admin",
    "role": "admin"
  }
}
```

### ❌ 错误情况测试：
- 不带 Token → `401 Token is missing!`
- 错误 Token → `401 Token is invalid!`
- 过期 Token → `401 Token has expired!`

---

## 💻 前端如何使用？（以 Axios 为例）

```js
// 登录
const res = await axios.post('/api/login', {
  username: 'admin',
  password: '123456'
});
localStorage.setItem('token', res.data.token);

// 请求受保护接口
const profileRes = await axios.get('/api/profile', {
  headers: {
    'Authorization': localStorage.getItem('token')
  }
});
console.log(profileRes.data);
```

> ✅ 前端只需在每次请求的 `headers` 中带上 `Authorization: <token>` 即可。

---

## 🔒 安全增强建议（生产环境）

1. **密钥不要写死**：
   ```python
   app.config['SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
   ```

2. **Token 存储更安全**：
   - Web 端：优先存 **内存**（如 Vuex/Pinia state），避免 XSS 盗取
   - 或存 **HttpOnly Cookie**（需后端 `set_cookie`，前端无法读但自动发送）

3. **添加刷新 Token 机制**（本例省略，适合进阶）

---

## ✅ 总结

| 功能 | 实现方式 |
|------|--------|
| 登录 | `POST /api/login` → 返回 JWT |
| 认证 | 请求头 `Authorization: <token>` |
| 保护接口 | `method_decorators = [token_required]` |
| 用户信息 | 从 `g.current_user` 获取 |

这个例子足够简单，但包含了 **前后端分离 + RESTful + JWT 认证** 的所有核心要素。你可以在此基础上扩展用户注册、数据库集成、角色权限等功能。

现在，你已经掌握了现代 Flask RESTful API 的标准认证方式！🎉