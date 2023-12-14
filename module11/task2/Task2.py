import random
from Student import Student


class Program:
    @staticmethod
    def main():
        students = [
            Student("Margaret Banks", "1", [random.uniform(2, 5) for _ in range(5)]),
            Student("Nancy Thompson", "1", [random.uniform(2, 5) for _ in range(5)]),
            Student("Lori Flores", "2", [random.uniform(2, 5) for _ in range(5)]),
            Student("Earl Smith", "2", [random.uniform(2, 5) for _ in range(5)]),
            Student("Sergio Reed", "3", [random.uniform(2, 5) for _ in range(5)]),
            Student("Michelle Robinson", "3", [random.uniform(2, 5) for _ in range(5)]),
            Student("Kathy Miller", "4", [random.uniform(2, 5) for _ in range(5)]),
            Student("Elizabeth Norman", "4", [random.uniform(2, 5) for _ in range(5)]),
            Student("Enrique Harris", "5", [random.uniform(2, 5) for _ in range(5)]),
            Student("Vincent Caldwell", "5", [random.uniform(2, 5) for _ in range(5)]),
        ]

        students = sorted(students, key=lambda student: student.get_average_grade())

        print("\n".join(map(str, students)))


if __name__ == '__main__':
    Program.main()
