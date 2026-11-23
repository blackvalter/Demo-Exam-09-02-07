-- Synthetic lab fixtures. Run once after initialising an empty training database.
BEGIN;
INSERT INTO categories(category_name) VALUES ('Кроссовки'), ('Ботинки');
INSERT INTO manufacturers(manufacturer_name) VALUES ('Учебная фабрика');
INSERT INTO suppliers(supplier_name) VALUES ('Учебный поставщик А'), ('Учебный поставщик Б');
INSERT INTO pickup_points(address) VALUES ('Учебный пункт 1');
INSERT INTO users(full_name,login,password,role_name) VALUES
 ('Учебный Администратор','lab_admin','demo-only-admin','Администратор'),
 ('Учебный Менеджер','lab_manager','demo-only-manager','Менеджер'),
 ('Учебный Клиент','lab_client','demo-only-client','Авторизованный клиент');
INSERT INTO products
 (product_sku,product_name,price,current_discount,stock_quantity,description,category_id,manufacturer_id,supplier_id)
 VALUES
 ('LAB-100','Кроссовки Учебные',3200,10,12,'Лёгкая модель',1,1,1),
 ('LAB-200','Ботинки Учебные',4800,0,3,'Демисезонная модель',2,1,2),
 ('LAB-300','Кроссовки Городские',2900,0,0,'Городская модель',1,1,2);
INSERT INTO orders(status,order_date,delivery_date,pickup_point_id,client_user_id,order_code)
 VALUES ('Новый','2026-11-21','2026-11-25',1,3,111);
INSERT INTO order_items(order_id,product_sku,quantity) VALUES (1,'LAB-100',1);
COMMIT;
