def calculate_roi(results):
    for keys, values in results.items():
        roi = round((values['revenue'] / values['cost'] - 1) * 100, 2)
        values.update({'ROI': roi})
    return results
    
results = {'vk': {'revenue': 103, 'cost': 98},'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110}, 'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},}
calculate_roi(results)