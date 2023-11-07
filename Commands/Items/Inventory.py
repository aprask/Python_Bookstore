from Commands.Items.Item import Item, Book, CD, DVD


class Inventory:
    in_stock = []
    sold_stock = []
    selection_id: int

    in_stock.append(Book("Narnia", True, 15.99, 0, 300))
    in_stock.append(Book("LOTR", True, 5000, 1, 10000))
    in_stock.append(Book("Animal Farm", True, 1.99, 2, 250))
    in_stock.append(Book("The Iliad", True, 40.25, 3, 800))
    in_stock.append(Book("The Bible", True, 1500000, 4, 999999))

    in_stock.append(CD("Thriller", True, 8.95, 5, 250))
    in_stock.append(CD("Hotel California", True, 6.95, 6, 100))
    in_stock.append(CD("Back in Black", True, 2.99, 7, 150))
    in_stock.append(CD("The Planets", True, 150.75, 8, 50000))
    in_stock.append(CD("Ride of the Valkyries", True, 250.25, 9, 250))

    in_stock.append(DVD("Star Wars", True, 8.95, 10, 600))
    in_stock.append(DVD("Hotel California", True, 10.55, 11, 550))
    in_stock.append(DVD("Back in Black", True, 10.75, 12, 1000))
    in_stock.append(DVD("The Planets", True, 25.25, 13, 1025))
    in_stock.append(DVD("Ride of the Valkyries", True, 12.25, 14, 1202))

