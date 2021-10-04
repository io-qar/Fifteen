import pytest

def test_is_solvable():
	assert modelBoard.is_solvable() == True

def test_info():
	"""Метод, тестирующий корректный вывод информации о доске."""
	assert modelBoard.info() == "Ваше поле:3 на 3, и имеет размер 80"
	
def test_get_empty_neighbor():
	"""
	Функция, тестирующая наличие индекса пустой клетки
	на момент начала работы приложения.
	"""
	assert controllerBoard.get_empty_neighbor(1) != 0
	
def test_get_inv_count():
	assert controllerBoard.get_inv_count() != 0
	
def test_model_init():
	...
	
if __name__ == '__main__':
	pytest.main()
