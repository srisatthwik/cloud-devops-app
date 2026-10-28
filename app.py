import os

env = os.getenv("APP_ENV", "development")

if env == "production":
    import config_prod as config
else:
    import config_dev as config

print("Environment:", env)
print("Database:", config.DATABASE)
print("Debug:", config.DEBUG)