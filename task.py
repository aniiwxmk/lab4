import matplotlib.pyplot as plt

class Point_3:
    # Кількість створених екземплярів точки
    point_count = 0
    
    def __init__(self, x=0.0, y=0.0):
        # Дійсні координати точки на площині
        self.__x = 0.0
        self.__y = 0.0
        # Задаємо координати точки через метод, щоб використати обмеження [-100, 100]
        self.set_x(x)
        self.set_y(y)
        # Збільшуємо кількість створених екземплярів точки
        Point_3.point_count += 1
    
    def __del__(self):
        # Зменшуємо кількість створених екземплярів точки при видаленні
        Point_3.point_count -= 1
        print("Point_3 object destroyed!")
    
    @property
    def get_x(self):
        return self.__x
    
    @property
    def get_y(self):
        return self.__y
    
    def set_x(self, x):
        # Задаємо координату x з обмеженням від -100 до 100
        if -100 <= x <= 100:
            self.__x = x
        else:
            self.__x = 0.0
    
    def set_y(self, y):
        # Задаємо координату y з обмеженням від -100 до 100
        if -100 <= y <= 100:
            self.__y = y
        else:
            self.__y = 0.0
    
    @classmethod
    def get_point_count(cls):
        # Повертає кількість створених екземплярів точки
        return cls.point_count
    
    def shift(self, dx, dy):
        # Змінює координати точки на dx по x і dy по y
        self.set_x(self.__x + dx)
        self.set_y(self.__y + dy)

def main():
    # Задача 2: Виконання операцій з об'єктами класу
    # Створення списку з трьох точок
    points_list = [Point_3(2, 3), Point_3(-1, 0), Point_3(5, 8)]

    # Порахунок відстані між першою і третьою точкою
    distance = ((points_list[0].get_x - points_list[2].get_x)**2 + (points_list[0].get_y - points_list[2].get_y)**2)**0.5
    print(f"Відстань між першою і третьою точкою: {distance}")

    # Пересунення другої точки на 15 вліво
    points_list[1].shift(-15, 0)

    # Задача 3: Використання бібліотеки matplotlib
    # Відображення створених об'єктів до змін
    for point in points_list:
        plt.scatter(point.get_x, point.get_y, color='blue')

    plt.title('Точки до змін')
    plt.xlabel('Вісь X')
    plt.ylabel('Вісь Y')
    plt.grid(True)
    plt.show()

    # Відображення створених об'єктів після змін
    for point in points_list:
        plt.scatter(point.get_x, point.get_y, color='red')

    plt.title('Точки після змін')
    plt.xlabel('Вісь X')
    plt.ylabel('Вісь Y')
    plt.grid(True)
    plt.show()

    # Задача 4: Збереження координат точок у текстовому файлі
    file_path = 'coordinates.txt'
    with open(file_path, 'w') as file:
        for i, point in enumerate(points_list, start=1):
            if i % 2 != 0:
                file.write(f"{i}: {point.get_x}; {point.get_y}\n")
            else:
                file.write(f"{i}: {point.get_x}:{point.get_y}\n")

    print(f"Координати збережено у файлі: {file_path}")

if __name__ == "__main__":
    main()