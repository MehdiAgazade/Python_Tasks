class Product:
    def __init__(self, name, count):
        self.product_name = name
        self.product_count = count

products = [Product("Iphone", 10), Product("Samsung", 20)]

def add_product():
    new_product_name = input("Mehsulun adını daxil edin: ").lower
    new_product_count = int(input("Mehsulun sayını daxil edin: "))
    new_product = Product(new_product_name, new_product_count)
    for i in range(0, len(products)):
        if products[i].product_name == new_product_name:
            products[i].product_count += new_product_count
        # else:
        #     print(new_product)
        
def show_all_products():
    for i in range(0, len(products)):
        print(f"{products[i].product_name}  -->  {products[i].product_count}")

def delete_product():
    name = input("Silmek istediyiniz mehsulun adini daxil edin: ").lower()
    new_deleted_product_count = int(input("Silmek istediyiniz mehsulun sayını daxil edin: "))
    # new_deleted_product = Product(name, new_deleted_product_count)
    for product in products:
        if product.product_name == name:
            if product.product_count >= new_deleted_product_count:
                product.product_count -= new_deleted_product_count
                print("Mehsul ugurla silindi")
            else:
                print("Kifayet qeder mehsul yoxdur") 

def show_deleted_all_produts():
    for i in range(0, len(products)):
        print(f"{products[i].name} --> {products[i].product_count}")

def menu():
    while True:
        print("1. Mehsul elave etmek\n2. Butun mehsullari gostermek\n3. Mehsul silmek\n4. Cixis etmek")
        selection = int(input("\nZehmet olmasa secim edin: "))

        match selection:
            case 1:
                add_product()
            case 2:
                show_all_products()
            case 3:
                delete_product()
            case 4: 
                print("\nCixis edildi")
                break
            case _:
                print("Yalnis daxil etdiniz. Zehmet olmasa yeniden daxil edin")

menu()