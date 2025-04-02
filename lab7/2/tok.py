from yandex_music import Client

client = Client.from_credentials("", "ТВОЙ_ПАРОЛЬ")
print(client.token)  # Скопируй этот токен
