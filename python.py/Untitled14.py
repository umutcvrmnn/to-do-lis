#!/usr/bin/env python
# coding: utf-8

# In[ ]:



to_do_lists = {}  

def add_list(to_do_lists):
    category = input("Liste adini giriniz: ")
    if category not in to_do_lists:
        to_do_lists[category] = {}
        print(f"'{category}' Liste başariyla oluşturuldu.")
    else:
        print(f"'{category}' Liste zaten mevcut.")

def add_task(to_do_lists):
    category = input("Hangi Listeye eklemek istersiniz? ")
    if category in to_do_lists:
        task_list = to_do_lists[category]
        task_name = input("Yazilacak Maddeyi girin: ")
        if task_list:
            to_do_lists[category][task_name] = []
        else:
            to_do_lists[category] = {task_name: []}
        print("Madde başariyla eklendi.")
    else:
        print("Belirtilen kategori bulunamadi.")

def add_subtask(to_do_lists):
    category = input("Hangi kategorideki göreve alt görev eklemek istersiniz? ")
    if category in to_do_lists:
        task_name = input("Alt görevi eklemek istediğiniz görevi girin: ")
        if task_name in to_do_lists[category]:
            subtask_name = input("Alt görevi girin: ")
            to_do_lists[category][task_name].append(subtask_name)
            print("Alt görev başariyla eklendi.")
        else:
            print("Belirtilen görev bulunamadi.")
    else:
        print("Belirtilen kategori bulunamadi.")
        
def show_tasks(to_do_lists):
    print("Kategoriler ve Görevler: ")
    for category, tasks in to_do_lists.items():
        print(category + ":")
        for task, subtasks in tasks.items():
            print("- " + task)
            if subtasks:
                print("  Alt Görevler:")
                for subtask in subtasks:
                    print("  - " + subtask)



# Ana döngü
while True:
    print("\nTo-Do List Uygulamasi")
    print("1. Liste Ekle")
    print("2. Madde Ekle")
    print("3. Alt Görev Ekle")
    print("4. Listeleri Göster")
    print("5. Liste Sil")
    print("6. Çikiş")
    choice = input("Seçiminiz (1/2/3/4/5/6): ")
    
    if choice == "1":
        add_list(to_do_lists)
    elif choice == "2":
        add_task(to_do_lists)
    elif choice == "3":
        add_subtask(to_do_lists)
    elif choice == "4":
        show_tasks(to_do_lists)
    elif choice == "5":
        delete_task(to_do_lists)
    elif choice == "6":
        print("Uygulamadan çikiliyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")


# In[ ]:




