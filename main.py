import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_timetable_management_system.settings')
django.setup()

from school.models import School, Class, Subject, Teacher, Student, Timetable

while True:
    print("1. Додати предмет")
    print("2. Додати вчителя")
    print("3. Додати клас")
    print("4. Додати учня")
    print("5. Додати предмет у розклад")
    print("6. Додати оцінку учню")
    print("7. Вийти")

    choise = int(input("Виберіть опцію (1-7): "))

    if choise == 1:
        print("\nДодавання предмета")
        subject_name = input("Введіть назву предмета: ")

        if not subject_name:
            print("Назва предмета не може бути порожньою!")
        elif Subject.objects.filter(name=subject_name).exists():
                print(f"Предмет '{subject_name}' вже існує!")
        else:
            subject = Subject(name=subject_name)
            subject.save()
            print(f"Предмет '{subject_name}' додано.")

    elif choise == 2:
        pass
    elif choise == 3:
        pass
    elif choise == 4:
        pass
    elif choise == 5:
        pass
    elif choise == 6:
        pass
    elif choise == 7:
        break
    else:
        print("Невірний вибір! Спробуйте ще раз!")