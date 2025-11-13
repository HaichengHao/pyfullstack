# @Author: 百年
# @Date: 24.02.11
# @FileName: crawler_demo.py
# @Description: 演示在 Clash 规则模式下，部分请求走代理，部分不走

import httpx
import time

def main():
    print("🚀 开始测试混合代理请求...\n")

    # ============ 1. 不走代理：访问国内网站 ============
    print("1️⃣ 正在访问百度（不走代理）...")
    try:
        resp1 = httpx.get("https://www.baidu.com", timeout=10)
        if resp1.status_code == 200:
            title = resp1.text.split("<title>")[1].split("</title>")[0]
            print(f"✅ 成功！状态码: {resp1.status_code}")
            print(f"📄 页面标题: {title}\n")
        else:
            print(f"⚠️ 状态码异常: {resp1.status_code}\n")
    except Exception as e:
        print(f"❌ 访问百度失败: {e}\n")

    time.sleep(1)  # 小暂停，避免太快

    # ============ 2. 走代理：访问国外网站 ============
    print("2️⃣ 正在访问 Google（通过 Clash 代理）...")
    proxy_url = "http://127.0.0.1:7897"  # Clash 默认 HTTP 代理端口

    try:
        with httpx.Client(proxy=proxy_url, timeout=20) as client:
            resp2 = client.get("https://www.google.com")
            if resp2.status_code == 200:
                # 提取 Google 首页的部分内容（比如包含 "Google" 的关键词）
                snippet = resp2.text[:200].replace("\n", " ").strip()
                print(f"✅ 成功！状态码: {resp2.status_code}")
                print(f"📄 响应片段: {snippet}...\n")
            else:
                print(f"⚠️ 状态码异常: {resp2.status_code}\n")
    except httpx.ProxyError as e:
        print(f"❌ 代理错误（检查 Clash 是否运行）: {e}\n")
    except httpx.ConnectTimeout:
        print("❌ 连接超时（可能是节点问题或规则未覆盖 google.com）\n")
    except Exception as e:
        print(f"❌ 访问 Google 失败: {e}\n")

    print("🔚 测试结束。")

if __name__ == '__main__':
    main()