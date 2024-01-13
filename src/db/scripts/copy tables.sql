
/* -------------------------- LANG ------------------------------- */
drop  table if exists shalom_lang;
create table if not exists shalom_lang like hypotez_lang;
delete from shalom_lang;
insert into shalom_lang select * from hypotez_lang;

drop table if exists shalom_lang_shop;
create table if not exists shalom_lang_shop like hypotez_lang_shop;
delete from shalom_lang_shop where id_shop > 1;
insert into shalom_lang_shop select * from hypotez_lang_shop where id_shop = 11;
-- insert into shalom_lang_shop select * from hypotez_lang_shop;




/* ------------------------- SHOP -------------------------------- */
drop table if exists shalom_lang_shop;
create table if not exists shalom_lang_shop like hypotez_lang_shop;
delete from shalom_shop  where id_shop > 1;
insert into shalom_shop select * from hypotez_shop where hypotez_shop.id_shop = 11;

drop table if exists shalom_shop_url;
create table if not exists shalom_shop_url like hypotez_shop_url;
delete from shalom_shop_url where id_shop != 1;
insert into shalom_shop_url select * from hypotez_shop_url where hypotez_shop_url.id_shop = 11;
-- insert into shalom_shop_url select * from hypotez_shop_url;

drop table if exists shalom_shop_group;
create table if not exists shalom_shop_group like hypotez_shop_group;
delete from shalom_shop_group;
insert into shalom_shop_group select * from hypotez_shop_group;



/* -------------------------- CURRENCY ------------------------------- */
drop table if exists shalom_currency;
create table if not exists shalom_currency like hypotez_currency;
delete from shalom_currency;
insert into shalom_currency select * from hypotez_currency;

drop table if exists shalom_currency_lang;
create table if not exists shalom_currency_lang like hypotez_currency_lang;
delete from shalom_currency_lang;
insert into shalom_currency_lang select * from hypotez_currency_lang;

-- drop table if exists shalom_currency_shop;
create table if not exists shalom_currency_shop like hypotez_currency_shop;
delete from shalom_currency_shop  where id_shop > 1;
insert into shalom_currency_shop select * from hypotez_currency_shop  where hypotez_currency_shop.id_shop = 11 ;
-- insert into shalom_currency_shop select * from hypotez_currency_shop;



/* ------------------------------ MODULE --------------------------- */

delete from shalom_module;
insert into shalom_module select * from hypotez_module;

delete from shalom_module_access;
insert into shalom_module_access select * from hypotez_module_access;

delete from shalom_module_carrier;
insert into shalom_module_carrier select * from hypotez_module_carrier;

delete from shalom_module_country;
insert into shalom_module_country select * from hypotez_module_country;

delete from shalom_module_group;
insert into shalom_module_group select * from hypotez_module_group;

delete from shalom_module_history;
insert into shalom_module_history select * from hypotez_module_history;

delete from shalom_module_preference;
insert into shalom_module_preference select * from hypotez_module_preference;

drop table if exists shalom_module_shop;
create table if not exists shalom_module_shop like hypotez_module_shop;
delete from shalom_module_shop  where id_shop > 1;
insert into shalom_module_shop select * from hypotez_module_shop  where hypotez_module_shop.id_shop = 11;


/* -------------------------------- TAB ----------------------------------------- */
drop table if exists shalom_tab;
create table if not exists shalom_tab like hypotez_tab;
delete from shalom_tab;
insert into shalom_tab select * from hypotez_tab;

drop table if exists shalom_tab_advice;
create table if not exists shalom_tab_advice like hypotez_tab_advice;
delete from shalom_tab_advice;
insert into shalom_tab_advice select * from hypotez_tab_advice;

drop table if exists shalom_tab_lang;
create table if not exists shalom_tab_lang like hypotez_tab_lang;
delete from shalom_tab_lang;
insert into shalom_tab_lang select * from hypotez_tab_lang;


/* -------------------------------- CONTACT ----------------------------------------- */
drop table if exists shalom_contact;
create table if not exists shalom_contact like hypotez_contact;
delete from shalom_contact;
 insert into shalom_contact select * from hypotez_contact;

drop table if exists shalom_contact_lang;
create table if not exists shalom_contact_lang like hypotez_contact_lang;
delete from shalom_contact_lang;
 insert into shalom_contact_lang select * from hypotez_contact_lang;

drop table if exists shalom_contact_shop;
create table if not exists shalom_contact_shop like hypotez_contact_shop;
delete from shalom_contact_shop where id_shop > 1;
insert into shalom_contact_shop select * from hypotez_contact_shop where id_shop = 11;
-- insert into shalom_contact_shop select * from hypotez_contact_shop;


/* -------------------------------- COUNTRY ----------------------------------------- */

drop table if exists shalom_country;
create table if not exists shalom_country like hypotez_country;
delete from shalom_country;
 insert into shalom_country select * from hypotez_country;

drop table if exists shalom_country_lang;
create table if not exists shalom_country_lang like hypotez_country_lang;
delete from shalom_country_lang;
 insert into shalom_country_lang select * from hypotez_country_lang;

drop table if exists shalom_country_shop;
create table if not exists shalom_country_shop like hypotez_country_shop;
delete from shalom_country_shop  where id_shop > 1;
insert into shalom_country_shop select * from hypotez_country_shop where id_shop = 11;
-- insert into shalom_country_shop select * from hypotez_country_shop;

drop table if exists shalom_currency;
create table if not exists shalom_currency like hypotez_currency;
delete from shalom_currency;
 insert into shalom_currency select * from hypotez_currency;

drop table if exists shalom_currency_lang;
create table if not exists shalom_currency_lang like hypotez_currency_lang;
delete from shalom_currency_lang;
 insert into shalom_currency_lang select * from hypotez_currency_lang;

drop table if exists shalom_currency_shop;
create table if not exists shalom_currency_shop like hypotez_currency_shop;
delete from shalom_currency_shop  where id_shop > 1;
insert into shalom_currency_shop select * from hypotez_currency_shop  where id_shop = 11;
-- insert into shalom_currency_shop select * from hypotez_currency_shop;


/* -------------------------------------- CMS -------------------------------------------------- */

drop table if exists shalom_cms;
create table if not exists shalom_cms like hypotez_cms;
delete from shalom_cms;
 insert into shalom_cms select * from hypotez_cms;

drop table if exists shalom_cms_category;
create table if not exists shalom_cms_category like hypotez_cms_category;
delete from shalom_cms_category;
 insert into shalom_cms_category select * from hypotez_cms_category;

drop table if exists shalom_cms_category_lang;
create table if not exists shalom_cms_category_lang like hypotez_cms_category_lang;
delete from shalom_cms_category_lang;
 insert into shalom_cms_category_lang select * from hypotez_cms_category_lang;

drop table if exists shalom_cms_category_shop;
create table if not exists shalom_cms_category_shop like hypotez_cms_category_shop;
delete from shalom_cms_category_shop  where id_shop > 1;
insert into shalom_cms_category_shop select * from hypotez_cms_category_shop where id_shop = 11;
-- insert into shalom_cms_category_shop select * from hypotez_cms_category_shop;

drop table if exists shalom_cms_lang;
create table if not exists shalom_cms_lang like hypotez_cms_lang;
delete from shalom_cms_lang;
 insert into shalom_cms_lang select * from hypotez_cms_lang;

drop table if exists shalom_cms_role;
create table if not exists shalom_cms_role like hypotez_cms_role;
delete from shalom_cms_role;
 insert into shalom_cms_role select * from hypotez_cms_role;

drop table if exists shalom_cms_role_lang;
create table if not exists shalom_cms_role_lang like hypotez_cms_role_lang;
delete from shalom_cms_role_lang;
 insert into shalom_cms_role_lang select * from hypotez_cms_role_lang;

drop table if exists shalom_cms_shop;
create table if not exists shalom_cms_shop like hypotez_cms_shop;
delete from shalom_cms_shop  where id_shop > 1;
insert into shalom_cms_shop select * from hypotez_cms_shop where id_shop = 11;
-- insert into shalom_cms_shop select * from hypotez_cms_shop;

/* ------------------------------------- HOOK ------------------------------------ */

drop table if exists shalom_hook;
create table if not exists shalom_hook like hypotez_hook;
delete from shalom_hook;
 insert into shalom_hook select * from hypotez_hook;

drop table if exists shalom_hook_alias;
create table if not exists shalom_hook_alias like hypotez_hook_alias;
delete from shalom_hook_alias;
 insert into shalom_hook_alias select * from hypotez_hook_alias;


drop table if exists shalom_hook_module;
create table if not exists shalom_hook_module like hypotez_hook_module;
delete from shalom_hook_module where id_shop >1;
 insert into shalom_hook_module select * from hypotez_hook_module where id_shop = 11;


drop table if exists shalom_hook_module_exceptions;
create table if not exists shalom_hook_module_exceptions like hypotez_hook_module_exceptions;
delete from shalom_hook_module_exceptions where id_shop >1;;
 insert into shalom_hook_module_exceptions select * from hypotez_hook_module_exceptions where id_shop = 11;


/* ---------------------------------------- FB ---------------------------------------*/
drop table if exists shalom_fb_category_match;
create table if not exists shalom_fb_category_match like hypotez_fb_category_match;
delete from shalom_fb_category_match;
 insert into shalom_fb_category_match select * from hypotez_fb_category_match;


/* -------------------------------- IMAGE ----------------------------------------- */
drop table if exists shalom_image;
create table if not exists shalom_image like hypotez_image;
delete from shalom_image;
 insert into shalom_image select * from hypotez_image;

drop table if exists shalom_image_shop;
create table if not exists shalom_image_shop like hypotez_image_shop;
delete from shalom_image_shop where id_shop >1;
 insert into shalom_image_shop select * from hypotez_image_shop where id_shop = 11;

drop table if exists shalom_image_type;
create table if not exists shalom_image_type like hypotez_image_type;
delete from shalom_image_type;
 insert into shalom_image_type select * from hypotez_image_type;


/* -------------------------------- INFO ----------------------------------------- */
drop table if exists shalom_info;
create table if not exists shalom_info like hypotez_info;
delete from shalom_info;
 insert into shalom_info select * from hypotez_info;

drop table if exists shalom_info_shop;
create table if not exists shalom_info_shop like hypotez_info_shop;
delete from shalom_info_shop where id_shop >1;
 insert into shalom_info_shop select * from hypotez_info_shop where id_shop = 11;

drop table if exists shalom_info_lang;
create table if not exists shalom_info_lang like hypotez_info_lang;
delete from shalom_info_lang;
 insert into shalom_info_lang select * from hypotez_info_lang;


/* -------------------------------- POS STATICBLOCK ------------------------------------------------ */
drop table if exists shalom_pos_staticblock_shop;
create table if not exists shalom_pos_staticblock_shop like hypotez_pos_staticblock_shop;
delete from shalom_pos_staticblock_shop where id_shop > 1;
 insert into shalom_pos_staticblock_shop select * from hypotez_pos_staticblock_shop  where id_shop = 11;

drop table if exists shalom_poslistcategories;
create table if not exists shalom_poslistcategories like hypotez_poslistcategories;
delete from shalom_poslistcategories where id_shop > 1;
 insert into shalom_poslistcategories select * from hypotez_poslistcategories  where id_shop = 11;


drop table if exists shalom_posmegamenu_item_shop;
create table if not exists shalom_posmegamenu_item_shop like hypotez_posmegamenu_item_shop;
delete from shalom_posmegamenu_item_shop where id_shop > 1;
insert into shalom_posmegamenu_item_shop select * from hypotez_posmegamenu_item_shop  where id_shop = 11;

/* ------------------------- CE --------------------------------------------------------------------- */
create table if not exists shalom_ce_content like hypotez_ce_content;
delete from shalom_ce_content;
insert into shalom_ce_content select * from hypotez_ce_content;

create table if not exists shalom_ce_content_lang like hypotez_ce_content_lang;
delete from shalom_ce_content_lang;
insert into shalom_ce_content_lang select * from hypotez_ce_content_lang;

create table if not exists shalom_ce_content_shop like hypotez_ce_content_shop;
delete from shalom_ce_content_shop;
insert into shalom_ce_content_shop select * from hypotez_ce_content_shop;

create table if not exists shalom_ce_meta like hypotez_ce_meta;
delete from shalom_ce_meta;
insert into shalom_ce_meta select * from hypotez_ce_meta;

create table if not exists shalom_ce_revision like hypotez_ce_revision;
delete from shalom_ce_revision;
insert into shalom_ce_revision select * from hypotez_ce_revision;

create table if not exists shalom_ce_template like hypotez_ce_template;
delete from shalom_ce_template;
insert into shalom_ce_template select * from hypotez_ce_template;

create table if not exists shalom_ce_theme like hypotez_ce_theme;
delete from shalom_ce_theme;
insert into shalom_ce_theme select * from hypotez_ce_theme;

drop table shalom_ce_theme_lang;
create table if not exists shalom_ce_theme_lang like hypotez_ce_theme_lang;
delete from shalom_ce_theme_lang;
insert into shalom_ce_theme_lang select * from hypotez_ce_theme_lang;

create table if not exists shalom_ce_theme_shop like hypotez_ce_theme_shop;
delete from shalom_ce_theme_shop;
insert into shalom_ce_theme_shop select * from hypotez_ce_theme_shop;


