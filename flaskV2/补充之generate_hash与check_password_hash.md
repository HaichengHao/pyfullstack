你提到的 `generate_password_hash` 和 `check_password_hash` 是 **Flask-Login** 或更准确地说是 **Werkzeug** 提供的安全密码哈希工具，比直接使用 `hashlib.sha256()` 更加安全和推荐。

---

## 🔐 为什么你应该用 `generate_password_hash` 而不是 `hashlib.sha256`？

### ❌ 使用 `hashlib.sha256(password).hexdigest()` 的问题：
```python
user.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
```
- **不加盐（salt）**：同一个密码永远生成相同的哈希值，容易被彩虹表攻击。
- **计算速度快**：攻击者可以快速暴力破解。
- **不安全！**

---

### ✅ 推荐方式：使用 `generate_password_hash` 和 `check_password_hash`

这两个函数来自 `werkzeug.security`，它们：
- 自动加盐（salt）
- 使用强哈希算法（默认 `pbkdf2:sha256`）
- 抗暴力破解能力强
- 是 Flask 生态中标准做法（尤其配合 Flask-Login）

---

## ✅ 正确使用方法

### 1. 导入
```python
from werkzeug.security import generate_password_hash, check_password_hash
```

### 2. 注册时：加密密码
```python
@user_bps.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')

        if password != repassword:
            return render_template('user/register.html', errorinfo='两次输入的密码不一致')

        # 使用 generate_password_hash 加密
        hashed_password = generate_password_hash(password)

        user = User(
            username=username,
            password=hashed_password,  # 存储的是带盐的哈希
            phone=phone
        )
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('user.login'))
    return render_template('user/register.html')
```

> 💡 `generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)`
> - `method`：可选其他算法，如 `pbkdf2:sha512`
> - `salt_length`：盐长度，默认 8，建议 16

---

### 3. 登录时：验证密码
```python
@user_bps.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('user/login.html')

    username = request.form.get('username')
    password = request.form.get('password')
    phone = request.form.get('phone')

    user = User.query.filter_by(username=username, phone=phone, isdelete=0).first()

    # 使用 check_password_hash 验证
    if user and check_password_hash(user.password, password):
        session['uname'] = username
        return render_template('user/index.html', users=user)
    else:
        return render_template('user/login.html', errorinfo='用户名、密码或手机号错误')
```

> ✅ `check_password_hash(hashed, raw_password)` 会自动提取存储的 salt 并进行比对。

---

## 🛠 数据库字段长度注意！

由于 `generate_password_hash` 生成的字符串较长（通常是 **60~87 个字符**），所以你的数据库模型中 `password` 字段必须足够长。

### 修改你的 User 模型：
```python
class User(db.Model):
    # ...
    password = db.Column(db.String(128), nullable=False)  # 至少 128，保险起见
```

> 原来用 `hashlib.sha256().hexdigest()` 是 64 位，现在建议扩展到 128。

---

## 🔄 如果你已有旧用户数据怎么办？

可以写一个迁移脚本，将老密码升级为新格式：

```python
# 示例：升级旧密码
for user in User.query.all():
    if len(user.password) == 64:  # 判断是否是 sha256 哈希
        user.password = generate_password_hash(user.password)  # 实际项目中需谨慎处理
db.session.commit()
```

但更安全的方式是在用户下次登录时检测并自动升级。

---

## ✅ 总结：你应该怎么做？

| 功能 | 推荐做法 |
|------|---------|
| **密码加密存储** | `generate_password_hash(password)` |
| **密码校验** | `check_password_hash(user.password, input_password)` |
| **数据库字段长度** | `String(128)` 或以上 |
| **不再使用** | `hashlib.sha256(...).hexdigest()` |

---

## ✅ 修改建议（替换你代码中的加密部分）

### 替换注册逻辑中的密码加密：
```python
# 旧的 ❌
user.password = hashlib.sha256(password.encode('utf-8')).hexdigest()

# 新的 ✅
user.password = generate_password_hash(password)
```

### 替换登录验证逻辑：
```python
# 旧的 ❌
password_enc = hashlib.sha256(password_raw.encode('utf-8')).hexdigest()
user = User.query.filter_by(username=username, password=password_enc, phone=phone).first()

# 新的 ✅
user = User.query.filter_by(username=username, phone=phone, isdelete=0).first()
if user and check_password_hash(user.password, password_raw):
    # 登录成功
```

---

✅ 完成以上修改后，你的系统密码安全性将大幅提升！

需要我帮你写一个完整的 `User` 模型示例或 Flask-Migrate 迁移脚本吗？