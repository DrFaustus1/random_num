class MarsURLEncoder:

    def __init__(self):
        self.link_storage = dict()

    def encode(self, long_url):
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        start_name = 'https://ma.rs/'
        hashed_long_url = str(hash(long_url))[1:]
        self.link_storage[hashed_long_url] = long_url
        return start_name + hashed_long_url




    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        full_link_end = short_url.replace('https://ma.rs/', '')
        return str(self.link_storage[full_link_end])

            
first = MarsURLEncoder()
print(first.encode('https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html'))
print(first.decode('https://ma.rs/35560118789049708'))