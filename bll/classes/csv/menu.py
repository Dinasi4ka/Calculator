from bll.classes.csv.data_repository import DataRepository
from bll.classes.csv.data_strategy import ExtremeValuesStrategy
from bll.classes.csv.visualization import VisualizationFactory, export_visualization
import pandas as pd
import matplotlib.pyplot as plt

def filter_data(data):
    print("\nФільтрація даних:")
    print("1. За діапазоном дат")
    print("2. За мінімальним значенням температури")
    print("3. За максимальним значенням температури")
    print("4. Повернутися до головного меню")

    choice = input("Виберіть опцію (1-4): ")

    if choice == '1':
        start_date = input("Введіть початкову дату (yyyy-mm-dd): ")
        end_date = input("Введіть кінцеву дату (yyyy-mm-dd): ")
        data['date'] = pd.to_datetime(data['date'])  
        filtered_data = data[(data['date'] >= start_date) & (data['date'] <= end_date)]
        print(f"Дані відфільтровано за датами з {start_date} по {end_date}")
        return filtered_data
    elif choice == '2':
        min_temp = float(input("Введіть мінімальне значення температури: "))
        filtered_data = data[data['temp_max'] >= min_temp]
        print(f"Дані відфільтровано за мінімальним значенням температури: {min_temp}")
        return filtered_data
    elif choice == '3':
        max_temp = float(input("Введіть максимальне значення температури: "))
        filtered_data = data[data['temp_max'] <= max_temp]
        print(f"Дані відфільтровано за максимальним значенням температури: {max_temp}")
        return filtered_data
    elif choice == '4':
        return data  
    else:
        print("Невірний вибір. Спробуйте ще раз.")
        return data

def show_extreme_values(data):
    strategy = ExtremeValuesStrategy()
    extreme_values = strategy.process(data)
    print("Екстремальні точки по стовпцях:\n", extreme_values)

def visualization_choice(data):
    while True:
        print("\nВибір типу візуалізації:")
        print("1. Лінійний графік")
        print("2. Стовпчикова діаграма")
        print("3. Діаграма розсіювання")
        print("4. Відображення двох графіків разом")
        print("5. Повернутися до головного меню")

        choice = input("Виберіть опцію (1-5): ")

        if choice == '1':
            line_chart = VisualizationFactory.create_visualization('line', data)
            line_chart.plot('date', 'temp_max')
            plt.show()
            return line_chart  
        elif choice == '2':
            bar_chart = VisualizationFactory.create_visualization('bar', data)
            bar_chart.plot('date', 'temp_max')
            plt.show()
            return bar_chart
        elif choice == '3':
            scatter_plot = VisualizationFactory.create_visualization('scatter', data)
            scatter_plot.plot('temp_max', 'temp_min')
            plt.show()
            return scatter_plot
        elif choice == '4':
            fig, ax = plt.subplots(1, 2, figsize=(12, 6))

            ax[0].plot(data['date'], data['temp_max'], color='blue')
            ax[0].set_title("Лінійний графік")
            ax[0].set_xlabel("Дата")
            ax[0].set_ylabel("Макс. Температура")
            ax[0].tick_params(axis='x', rotation=45)

            ax[1].bar(data['date'], data['temp_max'], color='green')
            ax[1].set_title("Стовпчикова діаграма")
            ax[1].set_xlabel("Дата")
            ax[1].set_ylabel("Макс. Температура")
            ax[1].tick_params(axis='x', rotation=45)

            plt.tight_layout()
            plt.show()
            return fig  
        elif choice == '5':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")
        


def export_visualization_choice(visualization):
    print("\nВибір формату експорту:")
    print("1. PNG")
    print("2. SVG")
    print("3. Повернутися до попереднього меню")

    choice = input("Виберіть опцію (1-3): ")

    if choice == '1':
        filename = input("Введіть ім'я файлу (без розширення): ") + ".png"
        if isinstance(visualization, plt.Figure):
            visualization.savefig(filename, format='png', bbox_inches='tight', pad_inches=0.1)
        else:
            visualization.save(filename)
        print(f"Графік збережено як {filename}")
    elif choice == '2':
        filename = input("Введіть ім'я файлу (без розширення): ") + ".svg"
        if isinstance(visualization, plt.Figure):
            visualization.savefig(filename, format='svg', bbox_inches='tight', pad_inches=0.1)
        else:
            visualization.save(filename)
        print(f"Графік збережено як {filename}")
    elif choice == '3':
        return 
    else:
        print("Невірний вибір. Спробуйте ще раз.")

def menu(data):
    while True:
        print("\nМеню:")
        print("1. Показати екстремальні точки")
        print("2. Вибрати тип візуалізації")
        print("3. Фільтрувати дані")
        print("4. Вийти")

        choice = input("Виберіть опцію (1-4): ")

        if choice == '1':
            show_extreme_values(data)
        elif choice == '2':
            visualization = visualization_choice(data)
            if visualization:
                export_visualization_choice(visualization)  
        elif choice == '3':
            data = filter_data(data)  
        elif choice == '4':
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")
