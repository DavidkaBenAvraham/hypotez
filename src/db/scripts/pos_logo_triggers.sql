delimiter |
CREATE TRIGGER `shalom2hypotez_before_insert_pos_logo` BEFORE
INSERT
	ON
	`shalom_pos_logo`
	
FOR EACH ROW BEGIN
	
   INSERT
	INTO
	`hypotez_pos_logo` ( `id_pos_logo`,
	`title`,
	`link`,
	`image`,
	`description`,
	`porder`)
	VALUES(NEW.id_pos_logo,
	NEW.title,
	NEW.id_category,
	NEW.image,
	NEW.description,
	NEW.porder);
   END;
   |
   

delimiter |
CREATE TRIGGER `shalom2hypotez_before_update_pos_logo` BEFORE
UPDATE
	ON
	`shalom_pos_logo`
FOR EACH ROW BEGIN
   UPDATE
	`shalom_pos_logo`
SET
	
	`title` = NEW.title,
	`link` = NEW.id_category,
	`image` = NEW.image,
	`description` = NEW.description,
	`porder` = NEW.porder
	WHERE `id_pos_logo` = NEW.id_pos_logo
	;
   END;
   |
   