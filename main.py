def calculator():
    values = input('Insira os valores que deseja calcular por exemplo 5+5: ')

    if not values:
        return 'Você não inseriu os valores.'

    try:
        primary = int(values[0])
        secondary = int(values[2])
        value = values[1]

        obj = {
            '+': primary + secondary,
            '-': primary - secondary,
            'x': primary * secondary,
            '/': primary / secondary
        }

        if not obj[value]:
            return 'Não foi possivel calcular.'

        return f'O resultado é: {int(obj[value])}'
    except ValueError:
        return 'Valores inválidos, lembre-se apenas números de 1 a 9.'


while True:
    cal = calculator()
    print(cal)
