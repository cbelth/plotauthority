def check_args(values_list, colors, alphas):
    if colors and len(colors) != len(values_list):
        print('There must be one color for each value.')
        return False
    if len(alphas) != len(values_list):
        print('There must be one alpha for each value.')
        return False
    return True
