delimiter |
CREATE TRIGGER `hypotez2shalom_AFTER_INSERT_SHOP` AFTER
INSERT
	ON
	`kikat_shop`
	
FOR EACH ROW BEGIN
	
   INSERT
	INTO `shalom_shop`
	(
`id_shop`,
`id_shop_group`,
`name`,
`color`,
`id_category`,
`theme_name`,
`active`,
`deleted`)
	VALUES(
	NEW.id_shop,
NEW.id_shop_group,
NEW.name,
NEW.color
NEW.id_ca,tegory
NEW.themename,
NEW.active,
NEW.deleted) WHERE NEW.id_shop > 1;
   END;
   |
   

delimiter |
CREATE TRIGGER `hypotez2shalom_AFTER_UPDATE_SHOP` AFTER
UPDATE
	ON
	`kikat_shop`
	
FOR EACH ROW BEGIN
	
   UPDATE
	 UPDATE
	`shalom_shop`
SET
	`id_shop` = NEW.id_shop,
`id_shop_group` = NEW.id_shop_group,
`name` = NEW.name,
`color` = NEW.color,
`id_category` = NEW.id_category,
`theme_name` = NEW.theme_name,
`active` = NEW.active,
`deleted` = NEW.deleted
WHERE
	NEW.id_shop > 1
	;
   END;
   |
  
   
delimiter |
CREATE TRIGGER `hypotez2shalom_AFTER_DELETE_SHOP` AFTER
DELETE 
	ON
	`hypotez_shop`
FOR EACH ROW BEGIN
   delete
from
	`shalom_shop`
WHERE old.id_shop > 1

   END
   
   
delimiter |
CREATE TRIGGER `hypotez2shalom_AFTER_INSERT_SHOP_GROUP` AFTER
INSERT
	ON
	`kikat_shop_group`
	
FOR EACH ROW BEGIN
	
   INSERT
	INTO 
	`shalom_shop_group`
	(
	`id_shop_group`,
`name`,
`color`,
`share_customer`,
`share_order`,
`share_stock`,
`active`
`deleted`
	VALUES(
	NEW.id_shop_group
NEW.name
NEW.color
NEW.share_customer
NEW.share_order
NEW.share_stock
NEW.active
NEW.deleted);
   END;
   |
   

delimiter |
CREATE TRIGGER `hypotez2shalom_AFTER_UPDATE_SHOP_GROUP` AFTER
UPDATE
	ON
	`kikat_shop_group`
	
FOR EACH ROW BEGIN
	
   UPDATE
	 UPDATE
	`shalom_shop`
SET
	`id_shop` = NEW.id_shop
`id_shop_group` = NEW.id_shop_group
`name` = NEW.name
`color` = NEW.color
`id_category` = NEW.id_category
`theme_name` = NEW.theme_name
`active` = NEW.active
`deleted` = NEW.deleted
WHERE
	NEW.id_shop > 1
	;
   END;
   |
  
   
delimiter |
CREATE TRIGGER `hypotez2shalom_AFTER_DELETE_SHOP` AFTER
DELETE 
	ON
	`hypotez_shop`
FOR EACH ROW BEGIN
   delete
from
	`shalom_shop`
WHERE old.id_shop > 1

   END
   