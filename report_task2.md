# Аналіз продуктивності OOBTree vs dict

## Умови тестування

- Виконано 100 діапазонних запитів по ціні в межах [100; 300]
- Джерело даних: generated_items_data.csv

## Результати

- Загальний час виконання для **OOBTree**: 2.206 сек
- Загальний час виконання для **dict**: 0.603 сек

## Висновки

- Попри те, що `OOBTree` зазвичай ефективніший для відсортованих даних і діапазонів, у нашому експерименті він показав **гіршу продуктивність**.
- Це може бути зумовлено:
  - Витратами на об'єктну структуру дерева
  - Відсутністю великої кількості запитів з глибокою оптимізацією
- Для невеликих або середніх наборів даних стандартний `dict` може бути швидшим для простих фільтрів.

## Рекомендація

- Використовувати `dict` для простих завдань і меншого обсягу даних
- `OOBTree` виправдовує себе при:
  - великих обсягах (>100 тис. записів)
  - складних і частих діапазонних запитах
