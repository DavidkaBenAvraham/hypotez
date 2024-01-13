delimiter |
CREATE TRIGGER `shalom2hypotez_for_insert_pos_logo` FOR
INSERT
	ON
	`shalom_pos_logo`
FOR EACH ROW BEGIN
   INSERT INTO   `shalom_pos_logo` SET
`id_category` = NEW.id_category,
`id_parent` = NEW.id_parent,
`id_shop_default` = NEW.id_shop_default,
`level_depth` = NEW.level_depth,
`nleft` = NEW.nleft,
`nright` = NEW.nright,
`active` = NEW.active,
`date_add` = NEW.date_add,
`date_upd` = NEW.date_upd,
`position` = NEW.position,
`is_root_category` = NEW.is_root_category;
   END;
   |
   

delimiter |
CREATE TRIGGER `hypotez2shalom_after_update_hypotez_category` AFTER
UPDATE
	ON
	`hypotez_category`
FOR EACH ROW BEGIN
   UPDATE  `shalom_category` SET

`id_parent` = NEW.id_parent,
`id_shop_default` = NEW.id_shop_default,
`level_depth` = NEW.level_depth,
`nleft` = NEW.nleft,
`nright` = NEW.nright,
-- `active` = NEW.active,
`date_add` = NEW.date_add,
`date_upd` = NEW.date_upd,
`position` = NEW.position,
`is_root_category` = NEW.is_root_category
	where `id_category` = NEW.id_category;

   END;
   |