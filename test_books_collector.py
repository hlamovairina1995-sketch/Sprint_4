import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем д,  # добавлве книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_genre(), имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize('genre', ['Фантастика','Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_success_true(self, collector, genre):
        collector.add_new_book('Война и мир')
        collector.set_book_genre('Война и мир', genre)
        assert collector.get_book_genre('Война и мир') == genre
    
    @pytest.mark.parametrize('name', ['А', 'А' * 40])
    def test_add_new_book_valid_name_length(self, collector, name):
        collector.add_new_book(name)
        assert collector.get_books_genre() == {name: ''}

    @pytest.mark.parametrize('name', ['', 'А' * 41])
    def test_add_new_book_invalid_name_length(self, collector, name):
        collector.add_new_book(name)
        assert collector.get_books_genre() == {}

    def test_add_new_book_duplicate_does_not_change_book(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.add_new_book('Гарри Поттер')
        books_genre = collector.get_books_genre()
        assert books_genre.get('Гарри Поттер') == 'Фантастика'

    def test_get_book_genre_new_book(self, collector):
        collector.add_new_book('Книга')
        assert collector.get_book_genre('Книга') == ''

    def test_get_books_with_specific_genre_success_true(self, collector):
        collector.add_new_book('Сияние 1')
        collector.set_book_genre('Сияние 1', 'Ужасы')
        collector.add_new_book('Сияние 2')
        collector.set_book_genre('Сияние 2', 'Ужасы')
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert 'Сияние 2' in collector.get_books_with_specific_genre('Ужасы')

    def test_get_books_for_children_success_true(self, collector):
        collector.add_new_book('Детская книга')
        collector.set_book_genre('Детская книга', 'Комедии')
        collector.add_new_book('Страшная книга')
        collector.set_book_genre('Страшная книга', 'Ужасы')
        children_books = collector.get_books_for_children()
        assert 'Детская книга' in children_books
        assert 'Страшная книга' not in children_books

    def test_get_list_of_favorites_books_empty_true(self, collector):
        assert collector.get_list_of_favorites_books() == []

    def test_add_book_in_favorites_success_true(self, collector):
        collector.add_new_book('Любимая книга')
        collector.add_book_in_favorites('Любимая книга')
        assert 'Любимая книга' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_success_true(self, collector):
        collector.add_new_book('Одиссея')
        collector.add_book_in_favorites('Одиссея')
        collector.delete_book_from_favorites('Одиссея')
        assert collector.get_list_of_favorites_books() == []

    def test_get_books_genre_returns_all_books_with_genres(self, collector):
        collector.add_new_book('Женщина в белом')
        collector.set_book_genre('Женщина в белом', 'Детективы')
        collector.add_new_book('Двенадцать стульев')
        collector.set_book_genre('Двенадцать стульев', 'Комедии')
        assert collector.get_books_genre() == {
            'Женщина в белом': 'Детективы',
            'Двенадцать стульев': 'Комедии',
        }
