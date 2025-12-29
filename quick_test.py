# 创建一个个人信息卡片
print("=== 个人信息收集 ===")

# 收集信息
name = input("你的姓名: ")
age = input("你的年龄: ")
city = input("你所在的城市: ")

# 使用f-string创建格式化字符串
card = f"""
========================
        个人信息卡
========================
姓名: {name}
年龄: {age}
城市: {city}
========================
"""

# 打印卡片
print(card)

# 询问是否保存
save = input("是否保存到文件？(y/n): ")

if save == 'y':
    # 保存到文件
    with open("my_info.txt", "w", encoding="utf-8") as f:
        f.write(card)
    print("✅ 信息已保存到 my_info.txt")
else:
    print("❌ 未保存")