from config.configer import Configer

# 示例使用
config = Configer("config.yaml")

# 访问存在的配置数据
db_host = config["database.host"]
db_port = config["database.port"]
db_username = config["database.username"]
db_password = config["database.password"]

print("Database Host:", db_host)  # 输出: localhost
print("Database Port:", db_port)  # 输出: 3306
print("Database Username:", db_username)  # 输出: root
print("Database Password:", db_password)  # 输出: 236383

# 访问不存在的键，应该触发异常并返回默认值
log_level = config.get("logging.level", default="default_log_level")
print(
    "Log Level:", log_level
)  # 输出: default_log_level，并且应该打印 KeyError 调试信息

# 直接使用 __getitem__ 方法访问不存在的键
log_config = config["logging"]
print("Log Config:", log_config)  # 输出: None，并且应该打印 KeyError 调试信息
