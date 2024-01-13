
delete from shalom_lang;
insert into shalom_lang select * from hypotez_lang;

delete from shalom_lang_shop;
insert into shalom_lang_shop select * from hypotez_lang_shop;

delete from shalom_shop  where id_shop > 1;
insert into shalom_shop select * from hypotez_shop where hypotez_shop.id_shop > 1;

delete from shalom_shop_url where id_shop != 1;
insert into shalom_shop_url select * from hypotez_shop_url where hypotez_shop_url.id_shop > 1;

delete from shalom_shop_group;
insert into shalom_shop_group select * from hypotez_shop_group ;

create table if not exists shalom_currency like hypotez_currency;
delete from shalom_currency;
insert into shalom_currency select * from hypotez_currency ;

create table if not exists shalom_currency_lang like hypotez_currency_lang;
delete from shalom_currency_lang;
insert into shalom_currency_lang select * from hypotez_currency_lang ;

create table if not exists shalom_currency_shop like hypotez_currency_shop;
delete from shalom_currency_shop;
insert into shalom_currency_shop select * from hypotez_currency_shop ;