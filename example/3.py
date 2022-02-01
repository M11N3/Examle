json_new = {
    'company_id':   111111,
    'resource': 'record',
    'resource_id': 406155061,
    'status': 'create',
    'data': {
        'id': 11111111,
        'company_id': 111111,
        'services': [
            {
                'id': 90005656,
                'title': 'Стрижка',
                'cost': 1500,
                'cost_per_unit': 1500,
                'first_cost': 1500,
                'amount': 1,
            }
        ],
        'goods_transactions': [],
        'staff': {
            'id': 1819441,
            'name': 'Мастер'
        },
        'client': {
            'id': 130345867,
            'name': 'Клиент',
            'phone': '79111111111',
            'success_visits_count': 2,
            'fail_visits_count': 0
        },
        'clients_count': 1,
        'datetime': '2022-01-25T13:00:00+03:00',
        'create_date': '2022-01-22T00:54:00+03:00',
        'online': False,
        'attendance': 2,
        'confirmed': 1,
        'seance_length': 3600,
        'length': 3600,
        'master_request': 1,
        'visit_id': 346427049,
        'created_user_id': 10573443,
        'deleted': False,
        'paid_full': 1,
        'last_change_date': '2022-01-22T00:54:00+03:00',
        'record_labels': '',
        'date': '2022-01-22 10:00:00'
    }
}

json_old = {
    'company_id':   111111,
    'resource': 'record',
    'resource_id': 406155061,
    'status': 'create',
    'data': {
        'id': 11111111,
        'company_id': 111111,
        'services': [
            {
                'id': 22222225,
                'title': 'Стрика',
                'cost': 1500,
                'cost_per_unit': 1500,
                'first_cost': 1500,
                'amount': 1
            },
            {
                'id': 22222225,
                'title': 'Стрика',
                'cost': 1500,
                'cost_per_unit': 1500,
                'first_cost': 1500,
                'amount': 1
            }

        ],
        'goods_transactions': [],
        'staff': {
            'id': 1812441,
            'name': 'Мастер'
        },
        'client': {
            'id': 130345867,
            'name': 'Клиент',
            'phone': '79111111111',
            'success_visits_count': 2,
            'fail_visits_count': 0
        },
        'clients_count': 1,
        'datetime': '2022-01-25T13:00:00+03:20',
        'create_date': '2022-01-22T00:54:00+03:00',
        'online': False,
        'attendance': 2,
        'confirmed': 1,
        'seance_length': 3600,
        'length': 3600,
        'master_request': 1,
        'visit_id': 346427049,
        'created_user_id': 10573443,
        'deleted': False,
        'paid_full': 1,
        'last_change_date': '2022-01-22T00:54:00+03:00',
        'record_labels': '',
        'date': '2022-01-22 10:00:02'
    }
}


def get_value_by_path(some_dict, path):
    """Возвращает значение для вложенного словаря"""
    elem = some_dict
    try:
        for x in path:
            elem = elem.get(x)
        return elem
    except AttributeError:
        return None


def get_paths_by_dict(some_dict, path=()):
    """ Возвращает все пути для вложенных элементов словаря (не углубляется в массивы элементов) """
    for key, value in some_dict.items():
        key_path = path + (key,)
        yield key_path
        if hasattr(value, "items"):
            yield from get_paths_by_dict(value, key_path)


def diff(json_old, json_new, diff_list):
    """ Возвращает разницу в полях json указанные в diff_list

    Формат вывода если поле изменилось {field_name: new_data}
    Если поля не изменились возвращает пустой словарь {}
    """
    result = dict()
    # Получаем все пути для вложений данной структуры и оставляем только те, которые есть в diff_list
    path_list = [path for path in get_paths_by_dict(json_new) if path[-1] in diff_list]

    # Проходимся по всем путям и сравнимаем старые и новые данные
    for path in path_list:
        if get_value_by_path(json_old, path) != get_value_by_path(json_new, path):
            result[path[-1]] = get_value_by_path(json_new, path)

    return result


if __name__ == "__main__":
    diff_list = ["services", "staff", "datetime"]
    print(diff(json_old, json_new, diff_list))
