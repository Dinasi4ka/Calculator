import matplotlib.pyplot as plt

class Visualization():
    
    def __init__(self, data):
        self.data = data
        self.figure = None

    def plot(self, x_column, y_column):
        raise NotImplementedError("Метод повинен бути реалізований у підкласах")
    
    def save(self, filename):
        if self.figure:
            self.figure.savefig(filename, bbox_inches='tight', pad_inches=0.1)
            print(f"Графік збережено як {filename}")
        else:
            print("Спочатку потрібно створити графік перед збереженням.")

class LineChart(Visualization):
    
    def plot(self, x_column, y_column):
        self.figure, ax = plt.subplots()
        ax.plot(self.data[x_column], self.data[y_column])
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        ax.set_title("Лінійний графік")
        ax.tick_params(axis='x', rotation=45)

class BarChart(Visualization):
    
    def plot(self, x_column, y_column):
        self.figure, ax = plt.subplots()
        ax.bar(self.data[x_column], self.data[y_column])
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        ax.set_title("Стовпчикова діаграма")
        ax.tick_params(axis='x', rotation=45)

class ScatterPlot(Visualization):
    
    def plot(self, x_column, y_column):
        self.figure, ax = plt.subplots()
        ax.scatter(self.data[x_column], self.data[y_column])
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        ax.set_title("Діаграма розсіювання")
    

class CombinedCharts(Visualization):
    
    def plot(self, x_column, y_column1, y_column2):
        self.figure, axs = plt.subplots(1, 2, figsize=(15, 5))

        axs[0].plot(self.data[x_column], self.data[y_column1])
        axs[0].set_title(f"{y_column1} vs {x_column}")
        axs[0].set_xlabel(x_column)
        axs[0].set_ylabel(y_column1)
        
        axs[1].bar(self.data[x_column], self.data[y_column2])
        axs[1].set_title(f"{y_column2} vs {x_column}")
        axs[1].set_xlabel(x_column)
        axs[1].set_ylabel(y_column2)

        plt.tight_layout()

class VisualizationFactory:
    

    def create_visualization(visualization_type, data):
        if visualization_type == 'line':
            return LineChart(data)
        elif visualization_type == 'bar':
            return BarChart(data)
        elif visualization_type == 'scatter':
            return ScatterPlot(data)
        elif visualization_type == 'combined':
            return CombinedCharts(data)  
        else:
            raise ValueError(f"Невідомий тип візуалізації: {visualization_type}")

def export_visualization(visualization, filename):
    visualization.save(filename)



