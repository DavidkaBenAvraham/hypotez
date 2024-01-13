
delete from hypotez_category;
insert into hypotez_category select * from ego_category;

delete from hypotez_category_group;
insert into hypotez_category_group select * from ego_category_group;

delete from hypotez_category_lang;
insert into hypotez_category_lang select * from ego_category_lang;

delete from hypotez_category_product;
insert into hypotez_category_product select * from ego_category_product;

delete from hypotez_category_shop;
insert into hypotez_category_shop select * from ego_category_shop;
