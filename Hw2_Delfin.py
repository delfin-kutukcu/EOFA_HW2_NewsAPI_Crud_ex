from requests import get, post, put, delete
from pprint import pprint

API_KEY = 'bce93a376820411f9ed383c892d31415 '
BASE_URL = 'https://newsapi.org/v2'

def get_articles(params=None):
    endpoint = f'{BASE_URL}/everything'
    headers = {'X-Api-Key': API_KEY}
    response = get(url=endpoint, headers=headers, params=params)
    return response.json()

def create_article(article):
    print("Yeni makale ekleniyor...")
    pprint(article)

def update_article(article_id, new_data):
    print(f"{article_id} ID'li makale güncelleniyor...")
    pprint(new_data)

def delete_article(article_id):

    print(f"{article_id} ID'li makale siliniyor...")

def main():
    while True:
        print("\n1. Makaleleri Listele")
        print("2. Yazar İsmine Göre Makale Ara")
        print("3. Tarihe Göre Makale Ara")
        print("4. Yeni Makale Ekle")
        print("5. Makale Güncelle")
        print("6. Makale Sil")
        print("7. Çıkış")
        choice = input("Seçiminiz: ")

        if choice == '1':
            params = {'q': 'tesla', 'sortBy': 'publishedAt'}
            data = get_articles(params)
            pprint(data['articles'])

        elif choice == '2':
            author_name = input('Yazar İsmi: ')
            params = {'q': 'tesla', 'sortBy': 'publishedAt'}
            data = get_articles(params)
            for article in data['articles']:
                if article['author'] == author_name:
                    pprint(article)

        elif choice == '3':
            date = input('Tarih (YYYY-MM-DD): ')
            params = {'q': 'tesla', 'from': date, 'sortBy': 'publishedAt'}
            data = get_articles(params)
            pprint(data['articles'])

        elif choice == '4':
            new_article = {
                'author': input('Yazar İsmi: '),
                'title': input('Başlık: '),
                'content': input('İçerik: ')
            }
            create_article(new_article)

        elif choice == '5':
            article_id = input('Güncellenecek Makale ID: ')
            new_data = {
                'author': input('Yeni Yazar İsmi: '),
                'title': input('Yeni Başlık: '),
                'content': input('Yeni İçerik: ')
            }
            update_article(article_id, new_data)

        elif choice == '6':
            article_id = input('Silinecek Makale ID: ')
            delete_article(article_id)

        elif choice == '7':
            break

        else:
            print("Geçersiz seçim!")

if __name__ == "__main__":
    main()