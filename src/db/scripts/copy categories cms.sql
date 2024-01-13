/*
delete from hypotez_category;
insert into hypotez_category select * from shalom_phones_category;

delete from hypotez_category_group;
insert into hypotez_category_group select * from shalom_phones_category_group;

delete from hypotez_category_lang;
insert into hypotez_category_lang select * from shalom_phones_category_lang;

delete from hypotez_category_product;
insert into hypotez_category_product select * from shalom_phones_category_product;

delete from hypotez_category_shop;
insert into hypotez_category_shop select * from shalom_phones_category_shop;
*/



delete from ps_category;
insert into ps_category select * from shalom_phones_category;

delete from ps_category_group;
insert into ps_category_group select * from shalom_phones_category_group;

delete from ps_category_lang;
insert into ps_category_lang select * from shalom_phones_category_lang;

delete from ps_category_product;
insert into ps_category_product select * from shalom_phones_category_product;

delete from ps_category_shop;
insert into ps_category_shop select * from shalom_phones_category_shop;




/*
insert into hypotez_category_shop select 
id_category,
2,
`position` from shalom_phones_category_shop;
*/