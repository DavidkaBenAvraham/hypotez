ALTER TABLE hypotez_product MODIFY COLUMN id_product BIGINT auto_increment NOT NULL;
ALTER TABLE hypotez_product MODIFY COLUMN id_supplier BIGINT DEFAULT NULL NULL;
ALTER TABLE hypotez_product MODIFY COLUMN id_manufacturer BIGINT DEFAULT NULL NULL;
ALTER TABLE hypotez_product MODIFY COLUMN id_category_default BIGINT DEFAULT NULL NULL;
ALTER TABLE shalom_product MODIFY COLUMN id_product BIGINT auto_increment NOT NULL;
ALTER TABLE shalom_product MODIFY COLUMN id_supplier BIGINT DEFAULT NULL NULL;
ALTER TABLE shalom_product MODIFY COLUMN id_manufacturer BIGINT DEFAULT NULL NULL;
ALTER TABLE shalom_product MODIFY COLUMN id_category_default BIGINT DEFAULT NULL NULL;
