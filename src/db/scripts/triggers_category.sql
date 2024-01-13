/*


					hypotez->shalom





*/

delimiter |
drop trigger if exists `hypotez2shalom_after_insert_hypotez_category`;
|
CREATE TRIGGER `hypotez2shalom_after_insert_hypotez_category` AFTER
INSERT
	ON
	`hypotez_category`
FOR EACH ROW BEGIN
   INSERT INTO   `shalom_category` (
`id_category`,
`id_parent`,
`id_shop_default`,
`level_depth`,
`nleft`,
`nright`,
`active`,
`date_add`,
`date_upd`,
`position`,
`is_root_category`)
values ( NEW.id_category,
NEW.id_parent,
NEW.id_shop_default,
NEW.level_depth,
NEW.nleft,
NEW.nright,
NEW.active,
NEW.`date_add`,
NEW.date_upd,
NEW.`position`,
NEW.is_root_category);
   END;
   |
   
delimiter |
drop trigger if exists `hypotez2shalom_after_update_hypotez_category`;
|
CREATE TRIGGER `hypotez2shalom_after_update_hypotez_category` AFTER
UPDATE
	ON
	`hypotez_category`
FOR EACH ROW BEGIN
   UPDATE  `shalom_category` SET

`id_parent`=NEW.id_parent,
`id_shop_default`=NEW.id_shop_default,
`level_depth`=NEW.level_depth,
`nleft`=NEW.nleft,
`nright`=NEW.nright,
-- `active`=NEW.active,
`date_add`=NEW.`date_add`,
`date_upd`=NEW.date_upd,
`position`=NEW.`position`,
`is_root_category`=NEW.is_root_category
	where `id_category`=NEW.id_category;

   END;
   |
   
   
delimiter |
drop trigger if exists `hypotez2shalom_after_delete_hypotez_category`;
|
CREATE TRIGGER `hypotez2shalom_after_delete_hypotez_category` AFTER
DELETE 
	ON
	`hypotez_category`
FOR EACH ROW BEGIN
   delete  from   `shalom_category` where  `id_category`= OLD.id_category;
   END;
   |
   
   
   
   
   
   
   
   

delimiter |
drop trigger if exists `hypotez2shalom_after_insert_hypotez_category_group`;
|
CREATE TRIGGER `hypotez2shalom_after_insert_hypotez_category_group` AFTER
INSERT
	ON
	`hypotez_category_group`
FOR EACH ROW BEGIN
   INSERT INTO   `shalom_category_group`(
`id_category`,
`id_group`)values(NEW.id_category,NEW.id_group);
   END;
   |
   

   
delimiter |
drop trigger if exists `hypotez2shalom_after_update_hypotez_category_group`;
|
CREATE TRIGGER `hypotez2shalom_after_update_hypotez_category_group` AFTER
update
	ON
	`hypotez_category_group`
FOR EACH ROW BEGIN
   UPDATE  `shalom_category_group` SET
    `id_category`=NEW.id_category,
	`id_group`=NEW.id_group
	where (`id_category`=old.id_category AND `id_group`=old.id_group);

   END;
   |
   

delimiter |
drop trigger if exists `hypotez2shalom_after_delete_hypotez_category_group`;
|
CREATE TRIGGER `hypotez2shalom_after_delete_hypotez_category_group` AFTER
DELETE 
	ON
	`hypotez_category_group`
FOR EACH ROW BEGIN
   delete
from
	`shalom_category_group`
where(
	`id_category`=old.id_category
	AND 
 	`id_group`=old.id_group);

   END;
|
   


drop trigger if exists `hypotez2shalom_after_insert_hypotez_category_lang`;
|
CREATE TRIGGER `hypotez2shalom_after_insert_hypotez_category_lang` AFTER
INSERT
	ON
	`hypotez_category_lang`

FOR EACH ROW BEGIN
   INSERT INTO   `shalom_category_lang` (
`id_category`,
`id_shop`,
`id_lang`,
`name`,
`description`,
`link_rewrite`,
`meta_title`,
`meta_keywords`,
`meta_description`)
values(
NEW.id_category,
NEW.id_shop,
NEW.id_lang,
NEW.name,
NEW.description,
NEW.link_rewrite,
NEW.meta_title,
NEW.meta_keywords,
NEW.meta_description
);

   END;
   |
   


delimiter |
drop trigger if exists `hypotez2shalom_after_update_hypotez_category_lang`;
|
CREATE TRIGGER `hypotez2shalom_after_update_hypotez_category_lang` AFTER
update
	ON
	`hypotez_category_lang`
FOR EACH ROW BEGIN
   UPDATE  `shalom_category_lang` SET
   `id_category`=new.id_category,
	`id_shop`=NEW.id_shop,
	`id_lang`=NEW.id_lang,
	`name`=NEW.name,
	`description`=NEW.description,
	`link_rewrite`=NEW.link_rewrite,
	`meta_title`=NEW.meta_title,
	`meta_keywords`=NEW.meta_keywords,
	`meta_description`=NEW.meta_description
	
	where (`id_category`=OLD.id_category
	and `id_lang`=OLD.id_lang
	and `id_shop`=OLD.id_shop);

   END;
   |
   
   
   
   
   
   

delimiter |
drop trigger if exists `hypotez2shalom_after_delete_hypotez_category_lang`;
|
CREATE TRIGGER `hypotez2shalom_after_delete_hypotez_category_lang` AFTER
DELETE 
	ON
	`hypotez_category_lang`
FOR EACH ROW BEGIN
   delete
from
	`shalom_category_lang`
where(
	`id_category`=old.id_category
	AND 
 	`id_shop`=old.id_shop
 	AND
	 `id_lang`=OLD.id_lang);

   END;
   |
   



delimiter |
drop trigger if exists `hypotez2shalom_after_insert_hypotez_category_product`;
|
CREATE TRIGGER `hypotez2shalom_after_insert_hypotez_category_product` AFTER
INSERT
	ON
	`hypotez_category_product`
FOR EACH ROW BEGIN
   INSERT INTO   `shalom_category_product` 
   (
`id_category`,
`id_product`,
`position`)
values(NEW.id_category,NEW.id_product,NEW.`position`);

   END;
   |
   
   
   

delimiter |
drop trigger if exists `hypotez2shalom_after_update_hypotez_category_product`;
|
CREATE TRIGGER `hypotez2shalom_after_update_hypotez_category_product` AFTER
update
	ON
	`hypotez_category_product`
FOR EACH ROW BEGIN
   UPDATE  `shalom_category_product` SET
	`id_category`= NEW.id_category,
	`id_product`= NEW.id_product,
	`position`= NEW.`position`
	where (`id_category`=OLD.id_category
	and `id_product`=OLD.id_product);

   END;
   |
   
   
   
   
   
   

delimiter |
drop trigger if exists `hypotez2shalom_after_delete_hypotez_category_product`;
|
CREATE TRIGGER `hypotez2shalom_after_delete_hypotez_category_product` AFTER
DELETE 
	ON
	`hypotez_category_product`
FOR EACH ROW BEGIN
   delete
from
	`shalom_category_product`
where(
	`id_category`=old.id_category
	AND 
 	`id_product`=old.id_product);

   END;
   |

   
   

delimiter |
drop trigger if exists `hypotez2shalom_after_insert_hypotez_category_shop`;
|
CREATE TRIGGER `hypotez2shalom_after_insert_hypotez_category_shop` AFTER
INSERT
	ON
	`hypotez_category_shop`
FOR EACH ROW BEGIN
   INSERT INTO   `shalom_category_shop` 
   (
	`id_category`,
	`id_shop`,
	`position`)
	values(NEW.id_category,NEW.id_shop,NEW.`position`);

   END;
   |
   
   
   

delimiter |
drop trigger if exists `hypotez2shalom_after_update_hypotez_category_shop`;
|
CREATE TRIGGER `hypotez2shalom_after_update_hypotez_category_shop` AFTER
update
	ON
	`hypotez_category_shop`
FOR EACH ROW BEGIN
   UPDATE  `shalom_category_shop` SET
	`id_category` = NEW.id_category,
	`id_shop` = NEW.id_shop,
	`position` = NEW.`position`
	where (`id_category`= OLD.id_category
	and `id_shop`= OLD.id_shop);

   END;
   |
   
   
   
   
   
   

delimiter |
drop trigger if exists `hypotez2shalom_after_delete_hypotez_category_shop`;
|
CREATE TRIGGER `hypotez2shalom_after_delete_hypotez_category_shop` AFTER
DELETE 
	ON
	`hypotez_category_shop`
FOR EACH ROW BEGIN
   delete
from
	`shalom_category_shop`
where(
	`id_category`=old.id_category
	AND 
 	`id_shop`=old.id_shop);

   END;
   |



   