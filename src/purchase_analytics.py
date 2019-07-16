def prod_to_dept():
    
    # Define empty dictionary to map products to departments
    prod_dept = {}

    with open('../input/products.csv','r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        #next(csv_reader)
        for line in csv_reader:
           product_id = line['product_id']
           department_id = int(line['department_id'])
           if product_id not in prod_dept:
                 prod_dept[product_id] = department_id
    return prod_dept

def final_report(prod_dept): 
    
    # Create output dictionary for final report that calculates orders
    
    output = {}

    with open('../input/order_products.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            product_id = line['product_id']
            department_id = prod_dept[product_id]
            if department_id not in output:
                output[department_id] = {'number_of_orders': 0, 'number_of_first_orders': 0}
            output[department_id]['number_of_orders'] += 1
            if line['reordered'] == '0':
                output[department_id]['number_of_first_orders'] += 1
    return output

def dept_wise_sort():
    
    # Bring together and write out to report.csv file
    
    prod_dept = prod_to_dept()
    output = final_report(prod_dept)  
    dept_wise_sort = sorted(list(output.keys()))
    with open('github_report.csv', mode='w') as csv_file:
        fieldnames = ['department_id', 'number_of_orders', 'number_of_first_orders', 'percentage']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for department_id in dept_wise_sort:
            no_orders = output[department_id]['number_of_orders']
            no_first_orders = output[department_id]['number_of_first_orders']
            perc = '%.2f' % (no_first_orders / no_orders)
            writer.writerow({'department_id': department_id, 'number_of_orders': no_orders,
                        'number_of_first_orders': no_first_orders, 'percentage': perc})
if __name__ == '__main__':
     dept_wise_sort()