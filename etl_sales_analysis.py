import csv

def transform_data(data):
    products_total = {}
    clients_total = {}

    for row in data:
        product = row['Produto']
        client = row['Cliente']
        value = float(row['Valor'])
        quantity = int(row['Quantidade'])

        # Calculating total sales per product and client
        products_total[product] = products_total.get(product, 0) + value
        clients_total[client] = clients_total.get(client, 0) + value * quantity

    # Generating insights
    insights = []
    insights.append("Total Sales per Product:")
    for product, total in products_total.items():
        insights.append(f"- {product}: R${total:.2f}")

    insights.append("\nTotal Sales per Client:")
    for client, total in clients_total.items():
        insights.append(f"- {client}: R${total:.2f}")

    return "\n".join(insights)

def main():
    csv_file_path = 'vendas.csv'

    with open(csv_file_path, 'r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        data = list(csv_reader)

    insights = transform_data(data)

    # Saving insights to a text file
    with open('sales_insights.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(insights)

if __name__ == "__main__":
    main()
