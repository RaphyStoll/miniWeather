import time


class CacheManager:
    def __init__(self, expiration_time=900):  # 15 minutes par défaut
        self.cache = {}
        self.expiration_time = expiration_time

    def get(self, key, fetch_func, *args, **kwargs):
        current_time = time.time()
        if (
            key in self.cache
            and (current_time - self.cache[key]["timestamp"]) < self.expiration_time
        ):
            print("Récupéré depuis le cache")
            return self.cache[key]["data"]
        else:
            print("Récupéré depuis la source")
            data = fetch_func(*args, **kwargs)
            self.cache[key] = {"data": data, "timestamp": current_time}
            return data

    def clear(self):
        self.cache.clear()
